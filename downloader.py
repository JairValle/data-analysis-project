#from datetime import datetime
import requests
import csv


# FUNTIONS
def get_dataframe_url (url_data):
    url = url_base
    response = requests.get(url)
    if response.status_code == 200:
        return response.csv()
    return None


def download_data_frame(data_frame_url):
    response = requests.get(data_frame_url)
    if response.status_code == 200:
        response_content = response.content
        filename = f'Descargas/{data_frame_filename()}.csv'
        with open(filename, 'wb') as data:
            csv.write(response_content)
            return filename
    return None


def data_frame_filename():
    now = datetime.now()
    Covid = f'Covid2020_+{now}'
    return Covid

# Variables
url_base = 'http://galileoguzman.com/data/covid19_tweets.csv'
#url_base =  input('Escribe la dirección de la pagína web: ')

data_frame = get_dataframe_url(url_base)
download_data_frame(data_frame)
