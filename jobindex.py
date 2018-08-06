from requests import get
from bs4 import BeautifulSoup
import re
import time

starturl = 'https://www.jobindex.dk/jobsoegning'
response = get(starturl)

html_soup = BeautifulSoup(response.text, 'html.parser')
type(html_soup)
page_container = html_soup.find('div', class_ = 'jix_pagination_pages')
pages = page_container.find_all('a')
max = int(pages[len(pages)-2].text)
print (max)
t0 = time.time()
numberofjobs = 0


for pageNumber in range(1, 2):
    url = 'https://www.jobindex.dk/jobsoegning?page=' + str(pageNumber)


    response = get(url)

    html_soup = BeautifulSoup(response.text, 'html.parser')
    type(html_soup)
    print('paid job')
    job_containers = html_soup.find_all('div', class_ = 'PaidJob')
    print(len(job_containers))
    numberofjobs += len(job_containers)
    if (len(job_containers) > 0):
        for job in job_containers:
            job.find('div', class_="jix_toolbar jix_appetizer_toolbar").decompose()
            title = job.find('b')
            print ('TITLE: '+ title.text)
            text = job.find_all('p')
            desctext = ''
            for para in text:
                desctext += para.get_text()
            for element in job.find_all('li'):
                desctext += element.get_text()
            print('DESC: ' + desctext.strip().replace('\r', '').replace('\n', ''))

    print('free')
    
    job_containers = html_soup.find_all('div', class_ = 'jix_robotjob')
    print(len(job_containers))
    if (len(job_containers) > 0):
        for job in job_containers:
            title = job.find('strong')
            print ('TITLE: '+ title.text)
            job.find('strong').decompose()
            desc = job.find_all('br')
            job.find('span', class_="jix_toolbar jix_appetizer_toolbar").decompose()
            print ('DESC: ' + job.text.replace('\r', '').replace('\n', '').strip())
    numberofjobs += len(job_containers)
    print (numberofjobs)
    print (numberofjobs)
    print (numberofjobs)
    print (numberofjobs)
t1 = time.time()
print ("Done")
print ("found nr of jobs: " + str(numberofjobs))
print (t1-t0)