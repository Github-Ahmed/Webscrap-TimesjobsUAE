# To remove mapping error in code (Happens in python 3.10)
import collections.abc
collections.Mapping = collections.abc.Mapping
collections.MutableMapping = collections.abc.MutableMapping

import time
from bs4 import BeautifulSoup
import requests

def find_jobs():
    # Requesting some information:
    html_text = requests.get(
        'https://ae.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text

    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

    unfamiliar_skills = input("Enter skills you don't know: ")
    print(f'Filtering out {unfamiliar_skills} skill')


    for index, job in enumerate(jobs):
        published_date = job.find('span', class_='sim-posted').span.text

        if 'few' in published_date:
            company_name = job.find('h3', class_='joblist-comp-name').text.strip()
            skills = job.find('span', class_='srp-skills').text.replace('\r\n',
                                                                        '\n').replace('  ', '').replace(',', ', ').strip()
            job_name = job.find('h2').text.replace('\r\n', '').strip()
            more_info = job.header.h2.a['href']
            
            if unfamiliar_skills not in skills:
                
                with open(f'/Users/Ahmed/PythonProjects/Learning Projects/Bs4/posts/{index}.txt', 'w') as f:

                    f.write(f'Job title: {job_name} \n')
                    f.write(f'Company name: {company_name.strip()} \n')
                    f.write(f'Required skills: {skills} \n')
                    f.write(f'More information: {more_info} \n')
                    f.write('')

                print(f'file saved {index}' )

 
if '__name__' != '__main__':
    while True:
        find_jobs()

        time_wait = 10
        print(f"Watching {time_wait} minutes")
        time.sleep(time_wait * 60)
    

