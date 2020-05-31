#!/usr/bin/python3
from sys import argv

from bs4 import BeautifulSoup
import requests


#
def search_to_text(query):
	url = f"https://en.cppreference.com/mwiki/index.php?title=Special%3ASearch&search={query}"
	if "list" in query:
		url = "https://en.cppreference.com/w/cpp/container/list"
	r = requests.get(url)
	return r.text

def extract_content(soup):
	jobs = []
	for div in soup.find_all(name='div', attrs={'class':'row'}):
		for a in div.find_all(name='a', attrs={'data-tn-element':'jobTitle'}):
			jobs.append(a['title'])
	return jobs

def text_to_read(text):
	soup = BeautifulSoup(text, 'html.parser')
	readable = soup
	content = []
	for div in soup.find_all(name='div', attrs={'class':'t-dsc'}):
		for a in div.find_all(name='div', attrs={'class':'t-dsc-member-div'}):
			content.append(a['t-lines'])
	#more work to do
	content = soup.get_text()
	readable = content[content.find("[edit] std::list"):]
	xx = readable.find("Retrieved from \"https://en.cppreference.com/mwiki/index.php?title=cpp\"")
	readable = readable[:xx]
	return readable 

if __name__ == '__main__':
	print( 
		text_to_read( 
			search_to_text( argv[1] ) ) )