
import os
import requests
from bs4 import BeautifulSoup
import json


url = "https://en.wikipedia.org/wiki/History_of_Mexico"

def get_citations_needed_count(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    return len(soup.find_all("a",title="Wikipedia:Citation needed"))
 
def get_citations_needed_report(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
  
    new1=soup.find_all("sup",class_="noprint")
    repo={}
    for key ,post in  enumerate(new1) :
        repo[f"paragraph number {key+1}"]=post.parent.text
    return repo
    
if __name__=="__main__":
    print(get_citations_needed_count(url))
    print(get_citations_needed_report(url))
    json_data = json.dumps(get_citations_needed_report(url))
    with open('report_citations_needed.json', 'w') as file :
    
        file.write(json_data)