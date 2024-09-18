import os
import re
import requests
import feedparser

def sanitize_filename(filename):
    """
    Sanitize the filename by removing or replacing special characters to make it safe for saving.
    """
    # Remove or replace any special characters that are not safe for filenames
    sanitized_filename = re.sub(r'[<>:"/\\|?*]', '_', filename)
    return sanitized_filename

def download_file(url, save_path):
    """
    Downloads a file from the specified URL to the given save path.
    """
    try:
        # Send HTTP GET request to the URL
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Download the file in chunks
        with open(save_path, "wb") as file:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)

        print(f"Downloaded: {save_path}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to download {url}: {e}")

def download_podcast_episodes(rss_feed_url, download_location):
    """
    Downloads all episodes from a podcast RSS feed to the specified location if their titles start with 'NerdCast'.
    """
    # Parse the RSS feed
    feed = feedparser.parse(rss_feed_url)

    # Ensure the download location exists
    os.makedirs(download_location, exist_ok=True)

    # Iterate over all episodes in the RSS feed
    for entry in feed.entries:
        # Check if the episode title starts with 'NerdCast'
        if entry.title.startswith("NerdCast"):
            # Extract the episode URL and title
            episode_url = entry.enclosures[0].href if entry.enclosures else None
            episode_title = sanitize_filename(entry.title)  # Sanitize the episode title

            if episode_url:
                # Determine the file extension from the URL or default to .mp3
                file_extension = os.path.splitext(episode_url)[1]
                if not file_extension:
                    file_extension = ".mp3"

                # Define the save path for the episode
                save_path = os.path.join(download_location, f"{episode_title}{file_extension}")

                # Download the episode
                print(f"Downloading: {episode_title}")
                download_file(episode_url, save_path)
            else:
                print(f"No downloadable content found for: {episode_title}")
        else:
            print(f"Skipping: {entry.title} (Title does not start with 'NerdCast')")

if __name__ == "__main__":
    # Define the RSS feed URL for the podcast
    podcast_rss_url = "https://api.jovemnerd.com.br/feed-nerdcast/"  # Replace with the actual RSS feed URL

    # Define the custom location on your PC where you want to save the episodes
    download_location = "D:\workspaces\git\podcast_downloader\download"  # Replace with your desired path

    # Start downloading podcast episodes
    download_podcast_episodes(podcast_rss_url, download_location)
