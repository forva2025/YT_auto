#Import the required libraries
import requests
from bs4 import BeautifulSoup
#Link to the subreddit of your choice
url = 'https://i.reddit.com/r/shortscarystories/random'
#Set a random useragent to avoid suspicion
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
#Go the the url and get the sites data, allow redirects to get random story
response = requests.get(url, headers=headers, allow_redirects=True)
#Use BS4 (BeautifulSoup4 HTML library) to read the data
soup = BeautifulSoup(response.text, 'html.parser')
# Get the main body text of the post
main_text = soup.find('div', {'class': 'usertext-body'}).text.strip()
# Write the title and main text to a file
with open('video_script.txt', 'w') as f:
    f.write(main_text + '\n')


















# -- https://cracked.io/Evil-Corporation