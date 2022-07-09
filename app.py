import http.client

def check_connection(urls):
    try:
        for url in urls:
            connection =  http.client.HTTPConnection(f"{url}")
            connection.request('GET', '/')
            response = connection.getresponse()
            print(f"App: {url}, Status: {response.status} and reason: {response.reason}")
            if response.status == 200:
                print(f"Successfull response code")
            else:
                print(f"App:{url} looks down with status: {response.status} and reason: {response.reason}, please check the application")
    except Exception as e:
        print("an error occured")
    connection.close()

urls = ["www.google.com", "www.facebook.com", "www.twitter.com"]

check_connection(urls)


