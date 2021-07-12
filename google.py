import requests
from  csv import writer
from bs4 import BeautifulSoup

link = "https://www.google.com/search?q=" + "python"

headerParams = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}

response = requests.get(link, headers = headerParams)

soup = BeautifulSoup(response.content, "html.parser")

results = soup.find_all('div', class_="yuRUbf" )



with open("Search.csv", 'w') as csv_file:
  csv_writer = writer(csv_file)
  csv_writer.writerow(['Name', 'Description', 'link'])

  for result in results:
    link = result.find("a")['href']
    text = result.find("h3").string
    description = result.next_sibling.find("span").text

    csv_writer.writerow([text, description, link])  
