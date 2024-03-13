import httpx
import aiofiles
from typing import Union
from io import BufferedReader


class AsyncIdentityAPI:
    """
    Asynchronous client for the IdentityAPI endpoint.

    This class provides asynchronous methods to interact with Idegrity's Identity Endpoints.

    Attributes:
        user_id (int): The user ID for authentication.
        key (str): The API key for authentication.
        key_secret (str): The API key secret for authentication.
        endpoint_url (str): The URL of the verification endpoint.
    """

    def __init__(
        self,
        user_id: int,
        key: str,
        key_secret: str,
        endpoint_url: str = "https://api.idegrity.com",
    ):
        """
        Initializes the AsyncIdentityAPI client with authentication details and endpoint URL.

        Parameters:
            user_id (int): The user ID for authentication.
            key (str): The API key for authentication.
            key_secret (str): The API key secret for authentication.
            endpoint_url (str): The URL of the verification endpoint. Defaults to "https://api.idegrity.com".
        """
        self.user_id = user_id
        self.key = key
        self.key_secret = key_secret
        self.endpoint_url = endpoint_url

    async def verify_images(
        self,
        id_image: Union[str, BufferedReader],
        face_image: Union[str, BufferedReader],
        response_format: str = "json",  # New parameter for specifying response format
    ):
        """
        Asynchronously uploads ID and face images to the verification endpoint.

        This method accepts either file paths or file-like objects (e.g., io.BytesIO instances)
        for the ID and face images, and uploads them using multipart/form-data. It allows specifying
        the desired response format ('json' or 'toml').

        Parameters:
            id_image (Union[str, BufferedReader]): The ID image file path or file-like object.
            face_image (Union[str, BufferedReader]): The face image file path or file-like object.
            response_format (str): Desired response format ('json' or 'toml'). Defaults to 'json'.

        Returns:
            dict or str: The response from the server if the upload was successful, format depends on response_format.

        Raises:
            ValueError: If an unsupported file type is provided.
            httpx.HTTPStatusError: For responses indicating HTTP error statuses.
            httpx.RequestError: For network-related issues.
            Exception: For other unforeseen issues.
        """
        timeout = httpx.Timeout(connect=5.0, read=30.0, write=20.0, pool=15.0)

        files = {}

        # Helper function to prepare a file for upload
        async def prepare_file(file_path_or_obj):
            if isinstance(file_path_or_obj, str):
                async with aiofiles.open(file_path_or_obj, "rb") as f:
                    content = await f.read()
                return (file_path_or_obj, content, "image/png")
            elif isinstance(file_path_or_obj, BufferedReader):
                return (
                    "uploaded_image.png",
                    await file_path_or_obj.read(),
                    "image/png",
                )
            else:
                raise ValueError("Unsupported file type provided.")

        # Prepare files for upload
        files["id_image"] = await prepare_file(id_image)
        files["face_image"] = await prepare_file(face_image)

        headers = {
            "Accept": (
                "application/json" if response_format == "json" else "application/toml"
            ),
            "X-User-ID": str(self.user_id),
            "X-Key": self.key,
            "X-Key-Secret": self.key_secret,
        }

        try:
            async with httpx.AsyncClient(timeout=timeout) as client:
                response = await client.post(
                    f"{self.endpoint_url}/verify", files=files, headers=headers
                )

                if response.status_code == 200 or 400 <= response.status_code < 500:
                    if response_format == "json":
                        return response.json()
                    else:  # Assuming 'toml' or other formats will be plain text
                        return response.text
                else:
                    response.raise_for_status()
        except httpx.HTTPStatusError as e:
            # Handle HTTP errors (e.g., 400, 404, 500)
            print(f"HTTP error occurred: {e}")
        except httpx.RequestError as e:
            # Handle request issues, such as network problems
            print(f"Request error occurred: {e}")
        except Exception as e:
            # Handle other possible errors
            print(f"An unexpected error occurred: {e}")
