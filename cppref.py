#!/usr/bin/python3
from sys import argv

from bs4 import BeautifulSoup
import requests

def search_to_text(query):
	url = f"https://en.cppreference.com/mwiki/index.php?title=Special%3ASearch&search={query}"
	if "list" in query:
		url = "https://en.cppreference.com/w/cpp/container/list"
	r = requests.get(url)
	return r.text

def text_to_read(text):
	soup = BeautifulSoup(text, 'html.parser')
	
	all_content_c = soup.find(id="mw-content-text")
	all_content = all_content_c.get_text()

	ps = []
	for i in all_content_c.find_all("p"):
		ps.append(i.get_text())
	readable = ps[2:]#absolute garbage
	return readable

def search_to_read(query):
	return text_to_read( search_to_text( query ) ) 

if __name__ == '__main__':
	
	res = search_to_read( argv[1] )
	print()
	print(res)
	print()