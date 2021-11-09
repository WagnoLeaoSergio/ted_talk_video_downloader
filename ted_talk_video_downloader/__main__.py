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
        help="The URL for the video's website.",
    )
    parser.add_argument(
        "--name",
        type=str,
        help="Name of the video when saved.",
        default="new_video",
        required=False
    )
    parser.add_argument(
        "--output",
        type=str,
        help="Path where the video will be saved.",
        default="~/Downloads",
        required=False
    )
    parser.add_argument(
        "--quality",
        type=str,
        help="Set the video's quality (if available)",
        default="240p",
        choices=["240p", "320p", "480p"],
        required=False
    )
    args = parser.parse_args()

    ted_downloader = TED_Downloader()
    ted_downloader.process_mp4_filename(args.url)
    ted_downloader.download_and_save()


if __name__ == "__main__":  # pragma: no cover
    main()
