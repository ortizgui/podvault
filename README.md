# PodVault

This script is designed to facilitate the backup of podcast episodes that you enjoy. It downloads episodes from a specified RSS feed URL, allows you to filter episodes by title, and keeps track of downloaded and failed episodes to avoid duplicates.

## Features

- Downloads podcast episodes from an RSS feed.
- Filters episodes by title using a regular expression.
- Logs downloaded and failed episodes to separate files.
- Supports environment variables for configuration.

## Requirements

- Python 3.x
- `requests` library
- `feedparser` library
- `python-dotenv` library

## Installation

1. Clone the repository:
    ```sh
    git clone <repository_url>
    cd <repository_directory>
    ```

2. Install the required libraries:
    ```sh
    pip install requests feedparser python-dotenv
    ```

3. Create a `.env` file in the same directory as the script with the following content:
    ```dotenv
    PODCAST_RSS_URL=https://podcast.rss/feed
    DOWNLOAD_LOCATION=/path/to/download/directory
    TITLE_FILTER=.*
    ```

## Usage

Run the script:
```sh
python main.py
```

The script will prompt for the RSS feed URL, download location, and title filter if they are not set in the `.env` file.

## Configuration

You can configure the script using environment variables or by editing the `.env` file.

- `PODCAST_RSS_URL`: The URL of the podcast RSS feed.
- `DOWNLOAD_LOCATION`: The directory where episodes will be downloaded.
- `TITLE_FILTER`: A regular expression to filter episode titles. Default is `.*` to match all titles.

## Logging

The script logs downloaded and failed episodes to text files in the download directory:

- `downloaded_episodes.txt`: Contains titles of successfully downloaded episodes.
- `failed_episodes.txt`: Contains titles of episodes that failed to download.

## Example

Example `.env` file:
```dotenv
PODCAST_RSS_URL=https://api.jovemnerd.com.br/feed-nerdcast/
DOWNLOAD_LOCATION=/path/you/want/to/download
TITLE_FILTER=NerdCast.*
```

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.