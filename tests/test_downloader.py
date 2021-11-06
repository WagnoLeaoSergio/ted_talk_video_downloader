import re
import pytest

from ted_talk_video_downloader import TED_Downloader

@pytest.fixture
def Downloader_Instance():
    return TED_Downloader()

def test_process_mp4_filename_valid_url(Downloader_Instance):
    valid_url = "https://www.ted.com/talks/bozoma_saint_john_the_creative_power_of_your_intuition/up-next"
    result = Downloader_Instance.process_mp4_filename(valid_url)
    is_valid = re.match(".*[.mp4].*$", result) 
    assert is_valid

def test_process_mp4_filename_bad_response(Downloader_Instance):
    invalid_url = "https://www.ted.com/talks/adwwadawdwadwad"
    result = Downloader_Instance.process_mp4_filename(invalid_url)
    assert result == "Error! Cannot access page!"

def test_process_mp4_filename_invalid_url(Downloader_Instance):
    not_ted_website_url = "https://www.google.com"
    result = Downloader_Instance.process_mp4_filename(not_ted_website_url)
    assert result == "Error! This website is not from TED Talks!"


def test_download_and_save_no_filename(Downloader_Instance):
    result = Downloader_Instance.download_and_save()
    assert not result

def test_download_and_save_bad_response(Downloader_Instance):
    valid_url = "https://www.ted.com/talks/bozoma_saint_john_the_creative_power_of_your_intuition/up-next"
    Downloader_Instance.mp4_url = "https://awdawfwaf.com"
    result = Downloader_Instance.download_and_save()
    assert not result
