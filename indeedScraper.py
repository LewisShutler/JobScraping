import requests
from bs4 import BeautifulSoup
import pandas as pd
import urllib

def find_jobs():  
    """This function asks the user to input a job title and location to search indeed.co.uk for jobs and saves to a csv document."""
    job_title = input("Please enter a job title that you want to search indeed for:")
    location = input("Please enter a location:")
    
    
    Vars = {'q' : job_title, 'l' : location, 'sort' : 'date'}
    url = ('https://www.indeed.co.uk/jobs?' + urllib.parse.urlencode(Vars))
            


    while True:
        #Gets soup
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
                               
        #Extract job information
        job_elems = soup.find_all('div', class_='jobsearch-SerpJobCard')

        #Loops html to find desired data
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

        next = soup.find('a', attrs={'aria-label':'Next'})
        try:
            next = (next["href"])
        except TypeError:
            print("No more pages to search.")
            break
        url = ('https://www.indeed.co.uk' + next)

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



