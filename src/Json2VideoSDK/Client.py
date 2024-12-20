import requests
from typing import Dict, List

from .src.Movie import Movie


class Client:
    """
    A client for interacting with the JSON2Video API.
    """

    def __init__(self, api_key: str, base_url: str = "https://api.json2video.com/v2"):
        self.api_key = api_key
        self.base_url = base_url
        self.headers = {
            "x-api-key": self.api_key,
            "Content-Type": "application/json",
        }

    def get_movies(self, project_id: str) -> List[Dict]:
        """
        Gets the status of your movies for a given project ID.

        Args:
            project_id (str): The ID of the project.

        Returns:
            List[Dict]: A list of movie dictionaries from the API.  Returns an empty list if no movies are found.
                      Raises an exception for other errors.
        """
        url = f"{self.base_url}/movies?project={project_id}"

        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
            return response.json()
        except requests.exceptions.RequestException as e:
            print(
                f"Error fetching movies: {e}"
            )  # Enhanced error handling with details. Consider logging instead of print.
            # You could return an empty list or re-raise the exception depending on your needs
            return []

    def create_movie(self, movie: Movie) -> Dict:  # More descriptive method name
        """
        Creates a new movie rendering job.

        Args:
            movie (Movie): A Movie object representing the movie to create.

        Returns:
            Dict: The JSON response from the API. Raises an exception for errors.
        """
        url = f"{self.base_url}/movies"

        try:
            response = requests.post(url, headers=self.headers, json=movie)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error creating movie: {e}")  # Enhanced error handling
            raise  # Re-raise to signal an error to the calling function
