# multion.py
import os
import webbrowser
import requests
from cryptography.fernet import Fernet
from deprecated import deprecated

# from requests_oauthlib import OAuth2Session
import json
import time
import base64
import uuid
from PIL import Image
from io import BytesIO
from IPython.display import Video


class _Multion:
    def __init__(self, token_file="multion_token.enc", secrets_file="secrets.json"):
        self.token = None
        self.client_id = self.register_client()
        self.token_file = token_file
        self.api_url = "https://api.multion.ai/public/api/v1"

        self._api_key = os.getenv("MULTION_API_KEY")  # Add this line

        self.load_secrets(secrets_file)
        self.generate_fernet_key()
        self.create_multion_directory()

        # Load token if it exists
        self.load_token()

    @property
    def api_key(self):
        # Get the API key from the instance variable or the environment variable
        return self._api_key if self._api_key else os.getenv("MULTION_API_KEY")

    @api_key.setter
    def api_key(self, value):
        # Allow setting the API key manually and in the environment variable
        self._api_key = value
        if value:
            os.environ["MULTION_API_KEY"] = value

    def load_secrets(self, secrets_file):
        secrets_file = os.path.join(os.path.dirname(__file__), secrets_file)
        with open(secrets_file, "r") as f:
            secrets = json.load(f)

        self.fernet_key = secrets.get("FERNET_KEY")
        if self.fernet_key is None:
            self.fernet_key = Fernet.generate_key().decode()
            secrets["FERNET_KEY"] = self.fernet_key
            with open(secrets_file, "w") as f:
                json.dump(secrets, f, indent=4)

    def generate_fernet_key(self):
        self.fernet_key = self.fernet_key.encode()
        self.fernet = Fernet(self.fernet_key)

    def create_multion_directory(self):
        # Create a .multion directory in the user's home folder if it doesn't exist
        # This is also compatible with Google Colab
        self.home_dir = os.path.expanduser("~")
        self.multion_dir = os.path.join(self.home_dir, ".multion")
        try:
            os.makedirs(self.multion_dir, exist_ok=True)
        except PermissionError:
            # In case of restricted permissions in the home directory
            # (like on Google Colab),
            # we use a temporary directory
            import tempfile

            self.multion_dir = tempfile.mkdtemp()

        self.token_file = os.path.join(self.multion_dir, "multion_token.enc")
        self.is_remote = False

    def verify_user(self, use_api=False):
        """
        Verify the user by checking the validity of the API key or token.

        :param use_api: A boolean indicating whether to use the API key for verification.
        :return: True if the user is verified, False otherwise.
        """
        headers = {}
        if use_api:
            if self.api_key is not None:
                headers["X_MULTION_API_KEY"] = self.api_key
            else:
                return False
        if self.token is not None:
            headers["Authorization"] = f"Bearer {self.token['access_token']}"
        if not headers:
            return False

        url = f"{self.api_url}/verify_user"
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            if "status" in data:
                return data["status"]
            else:
                print(f"Status not found, {data}")
        else:
            print(f"An error occurred while verifying user: {str(response)}")
            return False

    def login(self, use_api=False, multion_api_key=None):
        """
        Log in to the Multion service using an API key or by obtaining a new token.

        :param use_api: A boolean indicating whether to use the API key for login.
        :param multion_api_key: An optional API key to use for login.
        """
        if multion_api_key:
            self.api_key = multion_api_key
        elif self.api_key is None:
            self.api_key = os.getenv("MULTION_API_KEY")

        if use_api:
            valid_api_key = self.verify_user(use_api)
            if valid_api_key:
                print("Logged in using API key.")
                return
            else:
                self.issue_api_key()
                return

        valid_token = self.verify_user()
        if valid_token:
            print("Logged in.")
            return

        # Create a unique client id
        self.client_id = self.register_client()
        authorization_url = self.get_auth_url()

        try:
            # Try to open the authorization URL in a new browser tab
            webbrowser.open(authorization_url)
        except webbrowser.Error:
            # If an error occurs, print the authorization URL
            print(
                "Please visit this URL to authorize the application: "
                + authorization_url
            )

        # Poll the server for the token
        attempts = 0
        while attempts < 5:
            data = self.get_token()
            if data:
                self.token = data
                self.save_token()  # Save the token after updating it
                break
            attempts += 1
            time.sleep(1)  # Wait before the next poll

    def issue_api_key(self):
        """
        Directs the user to the URL where they can generate an API key, and prompts them to enter it.
        The API key is then stored in the instance for future use.
        """
        # Get the authorization URL
        app_url = "https://app.multion.ai/api-keys"
        print("Please visit this URL to generate an API Key: " + app_url)

        try:
            # Try to open the authorization URL in a new browser tab
            webbrowser.open(app_url)
        except webbrowser.Error:
            # If an error occurs, print the authorization URL
            print("Please visit this URL to generate an API Key: " + app_url)

        # Wait for user input to get the API key
        self.api_key = input("Please enter your API Key: ")

    def register_client(self):
        """
        Generates a unique client identifier based on the MAC address of the device.

        This identifier is used to register the client with the backend service.
        The MAC address is converted to a UUID which is then returned.

        Returns:
            UUID: A unique identifier for the client device.
        """
        # Get the MAC address and use it to generate a UUID
        mac_num = uuid.getnode()
        mac = ":".join(("%012X" % mac_num)[i : i + 2] for i in range(0, 12, 2))
        device_uuid = uuid.uuid5(uuid.NAMESPACE_DNS, mac)
        # print(device_uuid)

        # TODO: Register the client with the backend to the user
        return device_uuid

    def load_token(self):
        if os.path.exists(self.token_file) and os.path.getsize(self.token_file) > 0:
            with open(self.token_file, "rb") as f:
                try:
                    encrypted_token = f.read()
                    decrypted_token = self.fernet.decrypt(encrypted_token).decode()
                    self.token = json.loads(decrypted_token)
                except json.JSONDecodeError:
                    print("Error reading token from file. The file might be corrupted.")
                    self.token = None

    def save_token(self):
        encrypted_token = self.fernet.encrypt(json.dumps(self.token).encode())
        with open(self.token_file, "wb") as f:
            f.write(encrypted_token)

    def refresh_token(self):
        def token_saver(token):
            self.token = token
            self.save_token()

        response = requests.post(
            f"{self.api_url}/refresh_token?client_id={self.client_id}"
        )
        if response.status_code == 200:
            data = response.json()
            if "access_token" in data:
                token = data["access_token"]
                token_saver(token)
            else:
                print(f"Token not found, {data}")
        else:
            print(f"An error occurred while refreshing token: {str(response)}")

    def set_headers(self):
        headers = {}
        if self.api_key is not None:
            headers["X_MULTION_API_KEY"] = self.api_key
        if self.token is not None:
            headers["Authorization"] = f"Bearer {self.token['access_token']}"
        return headers

    def parse_stream_chunks(self, response):
        for chunk in response.iter_lines():
            if chunk:
                decoded_chunk = chunk.decode('utf-8')
                json_str = decoded_chunk.replace('data: ', '')
                data = json.loads(json_str)
                yield data

    def post(self, url, data, canStream = False):
        if self.token is None and self.api_key is None:
            raise Exception(
                "You must log in or provide an API key before making API calls."
            )

        headers = self.set_headers()

        MAX_ATTEMPTS = 3
        attempts = 0
        while attempts < MAX_ATTEMPTS:  # tries up to 3 times
            try:
                stream = False
                if 'stream' in data.keys() and data['stream']:
                    stream = True
                response = requests.post(url, json=data, headers=headers, stream=stream)
                if stream and canStream:
                    return self.parse_stream_chunks(response)
            except requests.exceptions.RequestException as e:
                print(f"Request failed due to an error: {e}")
                break

            if response.ok:  # checks if status_code is 200-400
                try:
                    return response.json()["response"]["data"]
                except json.JSONDecodeError:
                    print("JSONDecodeError: The server didn't respond with valid JSON.")
                break  # if response is valid then exit loop
            elif response.status_code == 401:  # token has expired
                print("Invalid token. Refreshing...")
                self.refresh_token()  # Refresh the token
                # Update the authorization header
                headers["Authorization"] = f"Bearer {self.token['access_token']}"
            elif response.status_code == 404:  # server not connected
                print(
                    """Server Disconnected. Please press connect in the
                      Multion extension popup"""
                )
            else:
                print(f"Request failed with status code: {response.status_code}")
                print(f"Response text: {response.text}")

            # If we've not returned by now, sleep before the next attempt
            time.sleep(1)  # you may want to increase this value depending on the API

            # Increment the attempts counter
            attempts += 1

        # If we've exhausted all attempts and not returned, raise an error
        if attempts == MAX_ATTEMPTS:
            print(f"Request failed with status code: {response.status_code}")
            print(f"Response text: {response.text}")
            raise Exception("Failed to get a valid response after 5 attempts")

    def get(self):
        if self.token is None and self.api_key is None:
            raise Exception(
                "You must log in or provide an API key before making API calls."
            )

        headers = self.set_headers()
        url = f"{self.api_url}/sessions"
        response = requests.get(url, headers=headers)
        return response.json()

    def delete(self, url):
        if self.token is None and self.api_key is None:
            raise Exception(
                "You must log in or provide an API key before making API calls."
            )

        headers = self.set_headers()
        response = requests.delete(url, headers=headers)
        if response.ok:  # checks if status_code is 200-400
            try:
                return response.json()["response"]["data"]
            except Exception as e:
                print(f"ERROR: {e}")
        else:
            print(f"Failed to close session. Status code: {response.status_code}")

    def browse(self, data):
        if self.token is None and self.api_key is None:
            raise Exception(
                "You must log in or provide an API key before making API calls."
            )

        headers = self.set_headers()
        url = f"{self.api_url}/browse"

        try:
            response = requests.post(url, json=data, headers=headers)
        except requests.exceptions.RequestException as e:
            print(f"Request failed due to an error: {e}")

        if response.ok:  # checks if status_code is 200-400
            try:
                return response.json()
            except json.JSONDecodeError:
                print("JSONDecodeError: The server didn't respond with valid JSON.")

        elif response.status_code == 401:  # token has expired
            print("Invalid token. Refreshing...")
            self.refresh_token()  # Refresh the token
            # Update the authorization header
            headers["Authorization"] = f"Bearer {self.token['access_token']}"
        elif response.status_code == 404:  # server not connected
            print(
                """Server Disconnected. Please press connect in the
                Multion extension popup"""
            )
        else:
            print(f"Request failed with status code: {response.status_code}")
            print(f"Response text: {response.text}")

    def new_session(self, data):
        print(
            "WARNING: 'new_session' is deprecated and will be removed in a future version. Use 'create_session' instead."
        )
        url = f"{self.api_url}/sessions"
        # print("running new session")
        return self.post(url, data)

    def create_session(self, data):
        url = f"{self.api_url}/session"
        # print("running create session")
        return self.post(url, data)

    # def update_session(self, sessionId, data):
    #     print(
    #         "WARNING: 'update_session' is deprecated and will be removed in a future version. Use 'step_session' instead."
    #     )
    #     url = f"{self.api_url}/session/{sessionId}"
    #     # print("session updated")
    #     return self.post(url, data)

    def step_session(self, sessionId, data):
        url = f"{self.api_url}/session/{sessionId}"
        # print("session stepped")
        return self.post(url, data, canStream=True)

    def close_session(self, sessionId):
        url = f"{self.api_url}/session/{sessionId}"
        # print("session closed")
        return self.delete(url)

    def close_sessions(self):
        url = f"{self.api_url}/sessions"
        # print("all sessions closed")
        return self.delete(url)

    def list_sessions(self):
        return self.get()

    def get_auth_url(self):
        response = requests.get(
            f"{self.api_url}/authorization_url?client_id={self.client_id}"
        )
        if response.status_code == 200:
            data = response.json()
            if "authorization_url" in data:
                return data["authorization_url"]
            else:
                print(f"Token not found, {data}")
                return None
        else:
            print("Failed to get authorization url")
            return None

    def get_token(self):
        if self.token is not None and self.token["expires_at"] > time.time():
            return self.token

        response = requests.get(f"{self.api_url}/get_token?client_id={self.client_id}")
        if response.status_code == 200:
            data = response.json()
            if "access_token" in data:
                return data["access_token"]
            else:
                # print(f"Token not found, {data}")
                return None
        else:
            print("Failed to get token")
            return None

    def delete_token(self):
        if self.token:
            self.token = None
        if os.path.exists("multion_token.txt"):
            os.remove("multion_token.txt")
        else:
            print("No active session found. Access token has already been revoked.")

    def get_screenshot(self, response, height=None, width=None):
        screenshot = response["screenshot"]

        # Check if screenshot is a URL
        if screenshot.startswith("http://") or screenshot.startswith("https://"):
            # screenshot is a URL
            response = requests.get(screenshot)
            if response.status_code != 200:
                print(f"Failed to retrieve image from {screenshot}")
                return None
            img_bytes = response.content
        else:
            # screenshot is a base64 string
            base64_img_bytes = screenshot.replace("data:image/png;base64,", "")
            base64_img_bytes += "=" * ((4 - len(base64_img_bytes) % 4) % 4)
            img_bytes = base64.b64decode(base64_img_bytes)

        # Create a BytesIO object and read the image bytes
        img_io = BytesIO(img_bytes)
        # Convert BytesIO into Image
        img = Image.open(img_io)

        # Get the original image dimensions
        original_width, original_height = img.size

        if height is not None and width is None:
            # If only the height is provided, calculate the width while
            #  preserving the aspect ratio
            width = int((height / original_height) * original_width)

        elif width is not None and height is None:
            # If only the width is provided, calculate the height while
            #  preserving the aspect ratio
            height = int((width / original_width) * original_height)

        # Resize the image if either dimension was provided
        if height is not None and width is not None:
            new_dimensions = (width, height)  # width, height
            img = img.resize(new_dimensions, Image.LANCZOS)

        # Return the image
        return img

    def get_remote(self):
        if self.token is None and self.api_key is None:
            raise Exception(
                "You must log in or provide an API key before making API calls."
            )

        headers = self.set_headers()
        response = requests.get(f"{self.api_url}/is_remote", headers=headers)
        if response.status_code == 200:
            data = response.json()
            return data["is_remote"]
        else:
            print("Failed to get token")
            return False

    def set_remote(self, value: bool):
        if self.token is None and self.api_key is None:
            raise Exception(
                "You must log in or provide an API key before making API calls."
            )

        headers = self.set_headers()
        data = {"value": value}
        url = f"{self.api_url}/is_remote"
        response = requests.post(url, json=data, headers=headers)
        if response.ok:  # checks if status_code is 200-400
            try:
                data = response.json()
                self.is_remote = data["is_remote"]
                return data["is_remote"]
            except json.JSONDecodeError:
                print("JSONDecodeError: The server didn't respond with valid JSON.")
        else:
            print("Failed set remote")

    def get_video(self, session_id: str):
        if self.is_remote:
            response = requests.get(
                f"{self.api_url}/sessionVideo/{session_id}", stream=True
            )
            if response.status_code == 200:
                # Save the video stream to a file
                with open("video.webm", "wb") as f:
                    for chunk in response.iter_content(chunk_size=1024):
                        if chunk:
                            f.write(chunk)
                # Display the video using IPython display
                return Video("video.webm")
            else:
                print("Failed to get video")
                return None
        else:
            print("Not in remote mode")
            return None

    def set_api_url(self, url: str):
        self.api_url = url


# Create a Multion instance
_multion_instance = _Multion()


# Delegate the api_key getter and setter to _multion_instance
@property
def api_key():
    global _multion_instance
    return _multion_instance.api_key


@api_key.setter
def api_key(value):
    global _multion_instance
    _multion_instance.api_key = value


# Expose the login and post methods at the module level
def login(use_api=False, multion_api_key=None):
    _multion_instance.login(use_api, multion_api_key)


def post(url, data):
    return _multion_instance.post(url, data)


def get():
    return _multion_instance.get()


def browse(data):
    """
    Browse the web using MultiOn by calling the high-level browse API endpoint.

    Args:
        data (dict): A dictionary containing the parameters for the browsing operation.

            - cmd (str): A detailed and specific natural language instruction for guiding the web browsing experience.
            - url (str, optional): The initial URL to start the browsing session, defaults to the current URL if not provided.
            - maxSteps (int, optional): The maximum number of steps the browsing operation should attempt, defaults to a predefined value `20` if not specified.
            - stream (bool, optional): A flag indicating whether to stream the browsing session, enabling real-time updates.
            - modelArgs (dict, optional): A dictionary containing additional arguments for the model that will be used during the browsing session.

    Returns:
        dict: A dictionary containing the results of the browsing operation. It includes the following keys:

            - status (str): The current status of the browsing operation.
            - lastUrl (str): The last URL visited during the browsing session.
            - content (str): The content of the last visited page, typically in HTML format.
            - screenshot (str): A base64 encoded string representing a screenshot of the last visited page.
    """
    return _multion_instance.browse(data)


@deprecated
def new_session(data):
    """
    Create a new browsing session based on a user's command or request.

    The command should include the full info required for the session.
    Optionally include an url (defaults to google.com if no better option) to start the session.

    Args:
        data (dict): The data containing the input command and optional URL.

    Returns:
        dict: The result of the session creation including sessionId, status, url, screenshot, and message.
    """
    return _multion_instance.new_session(data)


@deprecated
def update_session(sessionId, data):
    """
    Update an existing browsing session with a new command based on a user's command or request to search.

    Optionally include an url to update the session.

    Args:
        sessionId (str): The ID of the session to be updated.
        data (dict): The data containing the input command and optional URL.

    Returns:
        dict: The result of the session update including sessionId, status, url, screenshot, and message.
    """
    return _multion_instance.update_session(sessionId, data)


def create_session(data):
    """
    Create a new browsing session based on a user's command or request.

    Args:
        data (dict): The data containing the input command and optional URL.

    Returns:
        dict: The result of the session creation including sessionId, status, url, screenshot, and message.
    """
    return _multion_instance.create_session(data)


def step_session(sessionId, data):
    """
    Step an existing browsing session with a new command based on a user's command or request.

    Args:
        sessionId (str): The ID of the session to be updated.
        data (dict): The data containing the input command and optional URL.

    Returns:
        dict: The result of the session update including sessionId, status, url, screenshot, and message.
    """
    return _multion_instance.step_session(sessionId, data)


def close_session(sessionId):
    """
    Close an existing browsing session.

    Args:
        sessionId (str): The ID of the session to be closed.

    Returns:
        dict: The result of the session closure including sessionId, status, url, screenshot, and message.
    """
    return _multion_instance.close_session(sessionId)


def close_sessions():
    """
    Close all existing browsing sessions.

    Returns:
        dict: The result of the sessions closure including a list of sessionIds, their status, and messages.
    """
    return _multion_instance.close_sessions()


def list_sessions():
    """
    List all active browsing sessions.

    Returns:
        list: A list of active sessions, each containing sessionId, status, url, and other relevant information.
    """
    return _multion_instance.list_sessions()


def delete_token():
    """
    Delete the current authentication token.
    """
    _multion_instance.delete_token()


def get_screenshot(response, height=None, width=None):
    """
    Get a screenshot from the given response object.

    Args:
        response: The response object to capture as a screenshot.
        height (optional): The height of the screenshot in pixels.
        width (optional): The width of the screenshot in pixels.

    Returns:
        The screenshot image.
    """
    return _multion_instance.get_screenshot(response, height, width)


def refresh_token():
    """
    Refresh the current authentication token.
    """
    _multion_instance.refresh_token()


def get_token():
    """
    Retrieve the current authentication token.

    Returns:
        The current authentication token.
    """
    return _multion_instance.get_token()


def get_remote():
    """
    Get the current remote state.

    Returns:
        The current remote state as a boolean.
    """
    return _multion_instance.get_remote()


def set_remote(value: bool):
    """
    Set the remote state.

    Args:
        value (bool): The new value for the remote state.
    """
    return _multion_instance.set_remote(value)


def get_video(session_id: str):
    """
    Get the video for the given session ID.

    Args:
        session_id (str): The session ID to retrieve the video for.

    Returns:
        The video associated with the given session ID.
    """
    return _multion_instance.get_video(session_id)


def set_api_url(url: str):
    """
    Set the API URL.

    Args:
        url (str): The new API URL to be set.
    """
    _multion_instance.set_api_url(url)


# api_key = property(api_key, api_key)
