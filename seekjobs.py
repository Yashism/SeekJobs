from bs4 import BeautifulSoup
import requests
import re


URL = "https://boards.greenhouse.io/embed/job_board?for=coursera"
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

urls = []
for link in soup.findAll('a'):
    urls.append(link.get('href'))

jobs = []
for i in range(len(urls)):
    getid = re.split("=", urls[i])
    MainURL = "https://boards.greenhouse.io/embed/job_app?for=coursera&token=" + getid[1]
    page = requests.get(MainURL)
    soup = BeautifulSoup(page.content, 'html.parser')
    JobTitle = soup.find('h1', class_='app-title')
    JobCompany = soup.find('span', class_='company-name')
    JobLocation = soup.find('div', class_='location')
    JobDescription = soup.find('div', id='content')
    jobs.append(JobTitle.text)
    jobs.append(JobCompany.text)
    jobs.append(JobLocation.text)
    jobs.append(JobDescription.text)
    
    
for i in range(len(jobs)):
    print(jobs[i])

    
    

