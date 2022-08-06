import http.client
import requests

urls = ['https://www.google.com/', 'https://www.facebook.com/']

def check_connection(urls):
    for each in urls:    
        data = requests.get(each)
        print(data.status_code)

check_connection(urls)


