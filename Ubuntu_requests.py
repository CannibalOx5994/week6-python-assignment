import os
import requests

def fetch_image():
    url = input("Enter the image URL: ").strip()

    # Make sure directory exists
    save_dir = "Fetched_Images"
    os.makedirs(save_dir, exist_ok=True)

    try:
        # Fetch the image
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Raises HTTPError if bad response

        # Try to extract filename
        filename = os.path.basename(url)
        if not filename or "." not in filename:
            filename = "downloaded_image.jpg"

        filepath = os.path.join(save_dir, filename)

        # Save image in binary mode
        with open(filepath, "wb") as f:
            f.write(response.content)

        print(f"✅ Image successfully saved as: {filepath}")

    except requests.exceptions.RequestException as e:
        print("⚠️ Error fetching the image:", e)

if __name__ == "__main__":
    fetch_image()
