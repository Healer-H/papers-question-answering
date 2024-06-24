import requests
import os
from bs4 import BeautifulSoup

def download_arxiv_papers(query, max_results=500, download_path='data/papers'):
    os.makedirs(download_path, exist_ok=True)
    url = f"http://export.arxiv.org/api/query?search_query={query}&sortBy=submittedDate&sortOrder=descending&start=0&max_results={max_results}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "xml")

    entries = soup.find_all("entry")
    for entry in entries:
        pdf_link = entry.find("link", {"title": "pdf"})['href']
        paper_id = entry.find("id").text.split('/')[-1]
        title = entry.find("title").text.strip().replace('\n', ' ')

        pdf_response = requests.get(pdf_link, stream=True)
        with open(f"{download_path}/{paper_id}_{title}.pdf", 'wb') as f:
            for chunk in pdf_response.iter_content(chunk_size=1024):
                f.write(chunk)
        print(f"Downloaded: {title}")

query = "cat:cs.AI+OR+cat:cs.LG+OR+cat:cs.CL+OR+cat:cs.CV+OR+cat:cs.NE"
download_arxiv_papers(query, max_results=500)
