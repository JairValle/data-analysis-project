#from datetime import datetime
import requests


# CONSTANTS
URL_BASE='http://galileoguzman.com/data/covid19_tweets.csv'


# FUNTIONS

def download_data_frame(data_frame_url):
    response = requests.get(data_frame_url)
    if response.status_code == 200:
        response_content = response.content
        filename = f'tmp/{data_frame_filename()}.csv'
        with open(filename, 'wb') as image:
            image.write(response_content)
            return filename
    return None


def data_frame_filename():
    now = datetime.now()
    Covid = f'Covid2020_+{now}'
    return Covid


