import requests
import os

download_uris = [
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q2.zip",
]

def main():
    # your code here
        
    os.makedirs("Exercises/Exercise-1/downloads", exist_ok=True)

    for file_uri in download_uris:
        # Use os.path.basename to get the filename from the URL
        file_name = os.path.basename(file_uri)
    
        # Use os.path.join to create a platform-independent file path
        save_path = os.path.join('Exercises','Exercise-1','downloads', file_name)

        # Check if the file already exists locally
        if os.path.exists(save_path):
            print(f"File '{file_name}' already exists locally. Skipping download.")
            continue  # Skip to the next iteration
    
        # Use try-except to handle potential exceptions during the request
        try:
            with requests.get(file_uri, stream=True) as response:
                response.raise_for_status()  # Raise an error for bad responses (e.g., 404)

                with open(save_path, 'wb') as file:

                    # Iterate over the response content to download the file in chunks
                    for chunk in response.iter_content(chunk_size=8192):
                        if chunk:  # Filter out keep-alive new chunks
                            file.write(chunk)

            print(f"File '{file_name}' downloaded successfully to '{save_path}'.")
        except requests.exceptions.RequestException as e:
            print(f"Error downloading file '{file_name}': {e}")


if __name__ == "__main__":
    main()
