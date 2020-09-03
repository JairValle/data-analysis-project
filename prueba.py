import requests
import csv

# data = requests.get('http://galileoguzman.com/data/covid19_tweets.csv')
# cr = csv.reader(data)

# for row in cr:
#     print row


url = 'http://galileoguzman.com/data/covid19_tweets.csv'
response = requests.get(url)        

with open('Descargas/data_frame_covid.csv', 'w') as f:
    writer = csv.writer(f)
    for line in response.iter_lines():
        writer.writerow(line.decode('utf-8').split(','))