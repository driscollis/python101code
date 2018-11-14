import os
import threading
import urllib.request

from queue import Queue

class Downloader(threading.Thread):
    """Threaded File Downloader"""

    def __init__(self, queue):
        """Initialize the thread"""
        threading.Thread.__init__(self)
        self.queue = queue
    
    def run(self):
        """Run the thread"""
        while True:
            # gets the url from the queue
            url = self.queue.get()
            
            # download the file
            self.download_file(url)

            # send a signal to the queue that the job is done
            self.queue.task_done()
            
    def download_file(self, url):
        """Download the file"""
        handle = urllib.request.urlopen(url)
        fname = os.path.basename(url)
        with open(fname, "wb") as f:
            while True:
                chunk = handle.read(1024)
                if not chunk: break
                f.write(chunk)
                
def main(urls):
    """
    Run the program
    """
    queue = Queue()
    
    # create a thread pool and give them a queue
    for i in range(5):
        t = Downloader(queue)
        t.setDaemon(True)
        t.start()
        
    # give the queue some data
    for url in urls:
        queue.put(url)
    
    # wait for the queue to finish
    queue.join()
    
if __name__ == "__main__":
    urls = ["http://www.irs.gov/pub/irs-pdf/f1040.pdf",
            "http://www.irs.gov/pub/irs-pdf/f1040a.pdf",
            "http://www.irs.gov/pub/irs-pdf/f1040ez.pdf",
            "http://www.irs.gov/pub/irs-pdf/f1040es.pdf",
            "http://www.irs.gov/pub/irs-pdf/f1040sb.pdf"]
    main(urls)