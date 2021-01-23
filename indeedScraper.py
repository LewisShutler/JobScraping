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
        job_soup = soup.find(id="resultsCol")
        
        #Extract job information
        job_elems = job_soup.find_all('div', class_='jobsearch-SerpJobCard')
        
        cols = ['titles', 'companies', 'links', 'date_listed']

        cols.append('titles')
        for job_elem in job_elems:
            title_elem = job_elem.find('h2', class_='title')
            title = title_elem.text.strip()
            title = title.strip('new')
            titles.append(title)
        extracted_info.append(titles)                    

        for job_elem in job_elems:
            company_elem = job_elem.find('span', class_='company')
            company = company_elem.text.strip()
            companies.append(company)
        extracted_info.append(companies)

        for job_elem in job_elems:
            link = job_elem.find('a')['href']
            link = 'www.Indeed.co.uk' + link
            links.append(link)
        extracted_info.append(links)

        for job_elem in job_elems:
            date_elem = job_elem.find('span', class_='date')
            date = date_elem.text.strip()
            dates.append(date)
        extracted_info.append(dates)
        
        for j in range(len(cols)-1):
            jobs_list[cols[j]] = extracted_info[j]
        
        num_listings = len(extracted_info[0])
        page_num += 1
        
    jobs = pd.DataFrame(jobs_list)
    jobs.to_excel(f"{job_title} jobs in {location}.xlsx")
  

if __name__ == '__main__':
    jobs_list = {}
    extracted_info = []
    titles = []
    companies = []
    links = []
    dates = []
    find_jobs()



