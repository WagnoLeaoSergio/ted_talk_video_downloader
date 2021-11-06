import argparse  # pragma: no cover

from .downloader import TED_Downloader  # pragma: no cover

def main() -> None:  # pragma: no cover
    """
    The main function executes on commands:
    `python -m ted_talk_video_downloader` and `$ ted_talk_video_downloader `.

    This is the program's entry point.
    """
    parser = argparse.ArgumentParser(
        description="ted_talk_video_downloader.",
        epilog="Write the url of the video to download it.",
    )
    parser.add_argument(
        "url",
        type=str,
        help="The URL for the video.",
    )
    args = parser.parse_args()

    ted_downloader = TED_Downloader()
    ted_downloader.process_mp4_filename(args.url)
    ted_downloader.download_and_save()

if __name__ == "__main__":  # pragma: no cover
    main()
