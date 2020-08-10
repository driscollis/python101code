import urllib.request

def download_file(url):
    urllib.request.urlretrieve(url, "code.zip")

def alternate_download(url):
    with urllib.request.urlopen(url) as response:
        data = response.read()

    with open("code2.zip", "wb") as code:
        code.write(data)

if __name__ == '__main__':
    url = 'http://www.blog.pythonlibrary.org/wp-content/uploads/2012/06/wxDbViewer.zip'
    download_file(url)