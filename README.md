# ted_talk_video_downloader

[![codecov](https://codecov.io/gh/WagnoLeaoSergio/ted_talk_video_downloader/branch/main/graph/badge.svg?token=ted_talk_video_downloader_token_here)](https://codecov.io/gh/WagnoLeaoSergio/ted_talk_video_downloader)
[![CI](https://github.com/WagnoLeaoSergio/ted_talk_video_downloader/actions/workflows/main.yml/badge.svg)](https://github.com/WagnoLeaoSergio/ted_talk_video_downloader/actions/workflows/main.yml)

Awesome ted_talk_video_downloader created by WagnoLeaoSergio

## Install it from PyPI

```bash
pip install ted_talk_video_downloader
```

## Usage

```py
from ted_talk_video_downloader.downloader import TED_Downloader

ted_downloader = TED_Downloader()
ted_downloader.process_mp4_filename("https://www.ted.com/talks/bozoma_saint_john_the_creative_power_of_your_intuition/up-next")
ted_downloader.download_and_save("new_video", "~/Downloads")
```

```bash
$ python -m ted_talk_video_downloader
#or
$ ted_talk_video_downloader
```

## Development

Read the [CONTRIBUTING.md](CONTRIBUTING.md) file.
