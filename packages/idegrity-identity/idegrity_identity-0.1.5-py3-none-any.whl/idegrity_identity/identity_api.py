import requests
from typing import Union
import mimetypes
from io import BufferedReader


class IdentityAPI:
    """
    Synchronous client for the IdentityAPI endpoint.

    This class provides synchronous methods to interact with Idegrity's Identity Endpoints

    Attributes:
        user_id (int): The user ID for authentication.
        key (str): The API key for authentication.
        key_secret (str): The API key secret for authentication.
        endpoint_url (str): The URL of the verification endpoint.
        timeout (float): The timeout in seconds for the network request.
    """

    def __init__(
        self,
        user_id: int,
        key: str,
        key_secret: str,
        endpoint_url: str = "https://api.idegrity.com",
        timeout: float = 30.0,  # Added a timeout parameter with a default value of 30 seconds
    ):
        """
        Initializes the IdentityAPI client with authentication details and endpoint URL.

        Parameters:
            user_id (int): The user ID for authentication.
            key (str): The API key for authentication.
            key_secret (str): The API key secret for authentication.
            endpoint_url (str): The URL of the verification endpoint. Defaults to "https://api.idegrity.com".
            timeout (float): The timeout in seconds for the network request. Defaults to 30.0 seconds.
        """
        self.user_id = user_id
        self.key = key
        self.key_secret = key_secret
        self.endpoint_url = endpoint_url
        self.timeout = timeout

    def verify_images(
        self,
        id_image: Union[str, BufferedReader],
        face_image: Union[str, BufferedReader],
        response_format: str = "json",  # Added parameter for specifying response format
    ):
        """
        Uploads ID and face images to the verification endpoint synchronously.

        Accepts either file paths or file-like objects (e.g., io.BytesIO instances) for
        the ID and face images, uploading them using multipart/form-data. Allows specifying
        the desired response format ('json' or 'toml').

        Parameters:
            id_image (Union[str, BufferedReader]): The ID image file path or file-like object.
            face_image (Union[str, BufferedReader]): The face image file path or file-like object.
            response_format (str): Desired response format ('json' or 'toml'). Defaults to 'json'.

        Returns:
            dict or str: The response from the server if the upload was successful, format depends on response_format.

        Raises:
            ValueError: If an unsupported file type is provided.
            requests.HTTPError: For responses indicating HTTP error statuses.
            requests.RequestException: For network-related issues.
            Exception: For other unforeseen issues.
        """
        files = {}
        headers = {
            "Accept": (
                "application/json" if response_format == "json" else "application/toml"
            ),
            "X-User-ID": str(self.user_id),
            "X-Key": self.key,
            "X-Key-Secret": self.key_secret,
        }

        # Prepare file data as before
        def prepare_file(file_path_or_obj, filename):
            if isinstance(file_path_or_obj, str):
                content = open(file_path_or_obj, "rb")
                mime_type, _ = mimetypes.guess_type(file_path_or_obj)
            elif isinstance(file_path_or_obj, BufferedReader):
                content = file_path_or_obj
                mime_type = "image/png"
            else:
                raise ValueError("Unsupported file type provided.")
            return (filename, content, mime_type)

        files["id_image"] = prepare_file(id_image, "id_image.png")
        files["face_image"] = prepare_file(face_image, "face_image.png")

        try:
            response = requests.post(
                f"{self.endpoint_url}/verify",
                files=files,
                headers=headers,
                timeout=self.timeout,
            )
            if response.status_code == 200 or 400 <= response.status_code < 500:
                if response_format == "json":
                    return response.json()
                else:  # Assuming 'toml' or other formats will be plain text
                    return response.text
            else:
                response.raise_for_status()
        except requests.HTTPError as e:
            print(f"HTTP error occurred: {e}")
        except requests.RequestException as e:
            print(f"Request error occurred: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        finally:
            # Ensure to close the file objects if you opened them
            for _, file_data, _ in files.values():
                if hasattr(file_data, "close"):
                    file_data.close()
