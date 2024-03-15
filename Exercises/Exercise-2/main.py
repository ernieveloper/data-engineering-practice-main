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

                #df = df.append({'Name': name, 'Last Modified': last_modified, 'Size': size, 'Description': description}, ignore_index=True)
                #df_new_row = pd.DataFrame({'Name': name, 'Last Modified': last_modified, 'Size': size, 'Description': description}, ignore_index=True)
                #Adding the new rows to the datafram using a list and then concatenating them to the data fram. 
                #https://stackoverflow.com/questions/70837397/good-alternative-to-pandas-append-method-now-that-it-is-being-deprecated#:~:text=append%20was%20deprecated%20because%3A%20%22Series,'t%20be
                df = pd.concat([df,pd.DataFrame.from_records([{'Name': name, 'Last Modified': last_modified, 'Size': size, 'Description': description }])])
        df.head()

    else:
        print("Failed to fetch the webpage. Status code:", response.status_code)
    pass


if __name__ == "__main__":
    main()
