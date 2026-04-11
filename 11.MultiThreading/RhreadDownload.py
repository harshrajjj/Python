import threading
import time
import requests

def download_file(url):
    print(f"Starting download from {url}...")
    response = requests.get(url)
    print(f"Finished downloading from {url}. Content length: {len(response.content)} bytes.")

urls = [
    "https://httpbin.org/jpeg",
    "https://httpbin.org/png",
    "https://httpbin.org/svg"
]

start = time.time()
threads = []
for url in urls:
    t = threading.Thread(target=download_file, args=(url,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

end = time.time()
print(f"Total time taken: {end - start:.2f} seconds")

print("All threads finished")