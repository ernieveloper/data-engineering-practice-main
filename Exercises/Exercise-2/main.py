import requests
import pandas
from bs4 import BeautifulSoup

def main():
    # your code here

    url = "https://www.ncei.noaa.gov/data/local-climatological-data/access/2021/"

    #Fetch the web page content

    response = requests.get(url)

    if response.status_code == 200:
        #Parse the HTML content
        soup = BeautifulSoup(response.content,'html.parser')

        #Find all links on the page
        links = soup.find_all('a')

        #Extract href attribute from each link
        for link in links:
            href = link.get('href')
            print(href)
    else:
        print("Failed to fetch the webpage. Status code:", response.status_code)
    pass


if __name__ == "__main__":
    main()
