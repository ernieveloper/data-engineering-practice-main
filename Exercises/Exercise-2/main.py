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
                last_modified = columns[1].text.strip()
                size = columns[2].text.strip()
                #size = columns[2].span.text[0].strip('&0.')
                #description = columns[3].span.text[0].strip('&0.')
                description = columns[3].text.strip()
                #Add the new rows to the datafram using a list and then concatenating them to the data fram. 
                #https://stackoverflow.com/questions/70837397/good-alternative-to-pandas-append-method-now-that-it-is-being-deprecated#:~:text=append%20was%20deprecated%20because%3A%20%22Series,'t%20be
                df = pd.concat([df,pd.DataFrame.from_records([{'Name': name, 'Last Modified': last_modified, 'Size': size, 'Description': description }])])
        #print(df.head())
        #Look for the value 'Last Modified' column value '2024-01-19 10:08'
        result = df[df['Last Modified'] == '2024-01-19 10:08']
        print(result)

    else:
        print("Failed to fetch the webpage. Status code:", response.status_code)
    pass

if __name__ == "__main__":
    main()
