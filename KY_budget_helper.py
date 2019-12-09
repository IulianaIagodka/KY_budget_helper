#import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import urllib.request
from bs4 import BeautifulSoup

# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

def main():

    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    client = gspread.authorize(creds)

    # specify the url
    url = 'https://finance.i.ua/'
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)

    # parse the html using beautiful soup and store in variable `soup`
    soup = BeautifulSoup(response, 'html.parser')

    # get the index price
    list_d_avr = []
    table = soup.find('table', attrs={'class': 'table table-data -important'})
    '''rows = table.find_all('tr')
    for tr in rows:
        cols = tr.find_all('td')
        p = cols[0].text.strip()
        #d = cols[1].text.strip()'''
        print(table)
        #print(d)
    #price = d_avr_buy[1,1].text
    #print (price)

    # Find a workbook by name and open the first sheet
    # Make sure you use the right name here.
    sheet = client.open("pythontest").sheet1

    cell = sheet.cell(1, 2).value
    sheet.update_cell(1, 2, price)  # Update one cell
    #print(cell)

if __name__ == '__main__':
    main()
