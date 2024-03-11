import requests
import pandas as pd
from bs4 import BeautifulSoup

def main():
    # your code here

    url = "https://www.ncei.noaa.gov/data/local-climatological-data/access/2021/"

    #Fetch the web page content

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content,"html.parser")
        # Finding the table
        #table = soup.find('table')

        # Defining the dataframe
        df = pd.DataFrame(columns=['Name', 'Last Modified', 'Size', 'Description'])

        # Collecting Ddata
        for row in soup.find_all('tr'):    
            # Find all data for each column
            columns = row.find_all('td')
            
            if(columns != []):
                name = columns[0].text.strip()
                print(name)
                last_modified = columns[1].text.strip()
                size = columns[2].span.text[0].strip('&0.')
                description = columns[3].span.text[0].strip('&0.')

                df = df.append({'Name': name, 'Last Modified': last_modified, 'Size': size, 'Description': description}, ignore_index=True)

        df.head()

    else:
        print("Failed to fetch the webpage. Status code:", response.status_code)
    pass


if __name__ == "__main__":
    main()
