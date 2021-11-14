"""
ted_talk_video_downloader base module.

This is the principal module of the ted_talk_video_downloader project.
here you put your main classes and objects.
"""
import os
import re
import requests
from bs4 import BeautifulSoup
from typing import Any


class TED_Downloader:
    """
    Downloader class of the TED videos.

    Parameters
    ----------
    output_path: (str) Path where the video will be saved.
    Saves on the current folder by default.
    """
    def __init__(self, output_path: str = None) -> None:
        self.output_path = output_path
        self.mp4_url: str = ""

    def process_mp4_filename(self, url: str) -> str:
        """
        Validates the URL provided and extracts the video's MP4 file name.

        Arguments
        ---------
        url: (str) The url path for the video's page.

        Returns
        __________
        A string containing the file name of the video.
        """
        if 'https://www.ted.com/talks' not in url:
            error_message = "Error! This website is not from TED Talks!"
            print(error_message)
            return error_message

        response: requests.Response = requests.get(url)
        if not response.ok:
            error_message = "Error! Cannot access page!"
            print(error_message)
            return error_message

        soup = BeautifulSoup(response.content, features="html.parser")
        result: Any = None
        for value in soup.findAll("script"):
            if(re.search("talkPage.init", str(value))) is not None:
                result = str(value)
        result_mp4: Any = re.search("(?P<url>https?://[^\\s]+)(mp4)", result)
        mp4_url = result_mp4.group("url").split('"')[0]
        self.mp4_url = mp4_url
        return mp4_url

    def download_and_save(
            self,
            video_name: str,
            output_path: str
    ) -> bool:
        """
        Downloads and saves the video in the specified path.

        Arguments
        --------
        video_name: (str) If provided it will rename the file
        if the specified name.

        output_path: (str) If provided it will save the video
        in the specified path, ignoring the path specified
        in the object's parameters.
        """
        if not self.mp4_url:
            print("Error! No video url specified!")
            return False
        if not os.path.exists(output_path):
            print("Error! Output path invalid!")
            return False

        print(f"Downloading video from :{self.mp4_url}")

        print(f"Storing video as: {video_name}")
        file_name = f"{video_name}.mp4"

        try:
            video_response: requests.Response = requests.get(self.mp4_url)
        except (
            requests.exceptions.Timeout,
            requests.exceptions.InvalidURL,
            requests.exceptions.ConnectionError
        ):
            print("Error! Cannot download the video!")
            return False

        out_filename: str = os.path.join(output_path, file_name)
        print(f"Video saved on {out_filename}")

        with open(out_filename, 'wb') as video_file:
            video_file.write(video_response.content)

        return True
