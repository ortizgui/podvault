import os
import re
import requests
import feedparser
from dotenv import load_dotenv

def sanitize_filename(filename):
    """
    Sanitize the filename by removing or replacing special characters to make it safe for saving.
    """
    sanitized_filename = re.sub(r'[<>:"/\\|?*]', '_', filename)
    return sanitized_filename

def download_file(url, save_path):
    """
    Downloads a file from the specified URL to the given save path.
    """
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()

        with open(save_path, "wb") as file:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)

        print(f"Downloaded: {save_path}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to download {url}: {e}")

def download_podcast_episodes(rss_feed_url, download_location, title_filter):
    """
    Downloads all episodes from a podcast RSS feed to the specified location if their titles match the filter.
    """
    feed = feedparser.parse(rss_feed_url)
    os.makedirs(download_location, exist_ok=True)

    for entry in feed.entries:
        if re.match(title_filter, entry.title):
            episode_url = entry.enclosures[0].href if entry.enclosures else None
            episode_title = sanitize_filename(entry.title)

            if episode_url:
                file_extension = os.path.splitext(episode_url)[1]
                if not file_extension:
                    file_extension = ".mp3"

                save_path = os.path.join(download_location, f"{episode_title}{file_extension}")
                print(f"Downloading: {episode_title}")
                download_file(episode_url, save_path)
            else:
                print(f"No downloadable content found for: {episode_title}")
        else:
            print(f"Skipping: {entry.title} (Title does not match filter '{title_filter}')")

if __name__ == "__main__":
    load_dotenv()

    podcast_rss_url = os.getenv("PODCAST_RSS_URL") or input("Enter the RSS feed URL: ")
    download_location = os.getenv("DOWNLOAD_LOCATION") or input("Enter the download location: ")
    title_filter = os.getenv("TITLE_FILTER", ".*") or input("Enter the title filter (default is '.*' to match all): ")

    download_podcast_episodes(podcast_rss_url, download_location, title_filter)