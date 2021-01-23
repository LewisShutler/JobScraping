import requests
from bs4 import BeautifulSoup
import pandas as pd
import urllib

def find_jobs():  
    """This function asks the user to input a job title, location and number of pages to search indeed.co.uk for jobs and saves to an excel document."""
    job_title = input("Please enter a job title that you want to search indeed for:")
    location = input("Please enter a location:")
    pages_wanted = int(input("Number of pages would you like to search Indeed.co.uk for:"))
    
    page_num = 1  
    while page_num <= pages_wanted:

        Vars = {'q' : job_title, 'l' : location, 'sort' : 'date', 'start' : 10*(page_num-1)}
        url = ('https://www.indeed.co.uk/jobs?' + urllib.parse.urlencode(Vars))
                
        # load indeed jobs
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        
        
        #Extract job information
        job_elems = soup.find_all('div', class_='jobsearch-SerpJobCard')

        
        for job_elem in job_elems:
            title_elem = job_elem.find('h2', class_='title')
            title = title_elem.text.strip().strip('\nnew')
            titles.append(title) 

            company_elem = job_elem.find('span', class_='company')
            company = company_elem.text.strip()
            companies.append(company)
  
            link = job_elem.find('a')['href']
            link = 'www.Indeed.co.uk' + link
            links.append(link)

            date_elem = job_elem.find('span', class_='date')
            date = date_elem.text.strip()
            dates.append(date)
 
        page_num += 1
        
    jobs = pd.DataFrame({'Titles' : titles , 'companies' : companies , 'links' : links , 'date_listed' : dates})
    jobs.to_csv(f"{job_title} jobs in {location}.csv")
  

if __name__ == '__main__':
    jobs_list = {}
    extracted_info = []
    titles = []
    companies = []
    links = []
    dates = []
    find_jobs()



