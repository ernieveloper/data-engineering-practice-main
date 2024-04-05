import requests
import pandas as pd
from bs4 import BeautifulSoup

def file_download (file_uri):

    import os

    global directory
    
    #Create download directoy if it does not exist
    directory = "Exercises\\Exercise-2\\downloads"
    os.makedirs(directory, exist_ok=True)

    # Use os.path.basename to get the filename from the URL
    file_name = os.path.basename(file_uri)
        
    # Use os.path.join to create a platform-independent file path
    save_path = os.path.join('Exercises','Exercise-2','downloads', file_name)

    # Check if the file already exists locally, if it exists then print a message and 
    # stop the flow of the funciton.
    if os.path.exists(save_path):
        print(f"File '{file_name}' already exists locally. Skipping download.")
        return
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

def main():
    # your code here

    url = "https://www.ncei.noaa.gov/data/local-climatological-data/access/2021/"

    #Fetch the web page content

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content,"html.parser")

        # Defining the dataframe
        df = pd.DataFrame(columns=['Name', 'Last Modified', 'Size', 'Description'])

        # Collecting Ddata
        for row in soup.find_all('tr'):    
            # Find all data for each column
            columns = row.find_all('td')
            
            if(columns != []):
                name = columns[0].text.strip()
                last_modified = columns[1].text.strip()
                size = columns[2].text.strip()
                description = columns[3].text.strip()
                
                #Add the new rows to the datafram using a list and then concatenating them to the data frame. 
                #https://stackoverflow.com/questions/70837397/good-alternative-to-pandas-append-method-now-that-it-is-being-deprecated#:~:text=append%20was%20deprecated%20because%3A%20%22Series,'t%20be
                df = pd.concat([df,pd.DataFrame.from_records([{'Name': name, 'Last Modified': last_modified, 'Size': size, 'Description': description }])])
                
                #Setting a progressive index for the dataframe
                df.reset_index(drop=True, inplace=True)
        
        print(df.head())
        print('')

        #Look for the value 'Last Modified' column value '2024-01-19 10:08'
        result = df[df['Last Modified'] == '2024-01-19 10:45']
        print(len(result), "records for the Last Modified value 2024-01-19 10:45")
        print('')
        print(result)

        #Create download link for the row with index 3
        print('')
        file_name = df.loc[3,'Name']
        file_uri = url + file_name
        print("We will download the fist file that corresponds to the date 2024-01-19",file_uri)
        print('')
        print("Downloading the File")
        file_download(file_uri)

        df2 = pd.read_csv(f"{directory}\\{file_name}")
        
    pass

if __name__ == "__main__":
    main()
