# from asyncore import write
# from os import fdopen
from bs4 import BeautifulSoup
import requests
import time
import pandas as pd

company_name_csv = []
skill_csv = []
link_csv = []


'''This function will give you the scrapped data from the website, you can wwrite a skill that you are unfamiliar
with and it will not show you the jobs that require that skill'''

def Find_jobs():

    unfamiliar_skill = input("Please write (in lower case) the skill you are unfamiliar with\n>")
    print(f"filtering out {unfamiliar_skill}...") #Getting the unfamiliar skill

    link = 'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation='
    html_doc = requests.get(link) #getting the link of the job posting website from which jobs data will be scrapped

    print(html_doc.status_code) #if status code == 200 data website request was successfull

    html_text = html_doc.text #converting the content of website in text format
    soup = BeautifulSoup(html_text , 'lxml') #parsing the data 

    jobs = soup.find_all('li' , class_ = 'clearfix job-bx wht-shd-bx') #writing the logic to get access to the data
    for job in jobs:  
        date = job.find('span' , class_ = 'sim-posted').text.replace("Work from Home" , "").strip()
        if 'few' in date :
            company_name = job.find('h3',class_ ='joblist-comp-name')
            skills = job.find('span' , class_ = 'srp-skills')
            link = job.header.h2.a["href"]      #calling href attribute by ["href"]

            company_name = company_name.get_text().replace(" (More Jobs)","").strip()
            skills = skills.get_text().strip()

            company_name_csv.append(company_name)
            skill_csv.append(skills)
            link_csv.append(link)

            if unfamiliar_skill not in skills: #printing only that data through which skill user is familiar with
                print(f"Company name : {company_name}")
                print(f"Skills : {skills}")
                print(f"Publish Date : {date}")
                print(f"More info : {link}\n")

    df = pd.DataFrame({'Company Name':company_name_csv , 'Skills Required':skill_csv , 'Apply and More information':link_csv})
    df.to_csv('All_Scrapped_Data_csv.csv')


if __name__ == '__main__': #By doing these we make sure that these runs here only, i.e if we import these file to
                           #another python program these will not work (it is just like main function of c++)
    while True:         #by doing these our program will run on repeat after each 1 minute
        Find_jobs()
        time_wait = 1
        print(f"Please wait {time_wait} minutes more...")
        time.sleep(time_wait*60)                            #input variable in time.sleep() is in second






        

'''             The Below code is just for refrence on storing data in text format                  '''

def Find_jobs_storing_in_single_file():

    link = 'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation='
    html_doc = requests.get(link)
    print(html_doc.status_code)
    print("Copying the scrapped data in the file")

    html_text = html_doc.text
    soup = BeautifulSoup(html_text , 'lxml')
    jobs = soup.find_all('li' , class_ = 'clearfix job-bx wht-shd-bx')
    for index, job in enumerate(jobs):  
        date = job.find('span' , class_ = 'sim-posted').text.replace("Work from Home" , "").strip()
        if 'few' in date :
            company_name = job.find('h3',class_ ='joblist-comp-name')
            skills = job.find('span' , class_ = 'srp-skills')
            link = job.header.h2.a["href"]      #calling href attribute by ["href"]

            company_name = company_name.get_text().replace(" (More Jobs)","").strip()
            skills = skills.get_text().strip()

            with open("scrapped_data.txt" , "a") as f:
                f.write(f"{index+1})\n")
                f.write(f"Company name : {company_name}\n")
                f.write(f"Skills : {skills}\n")
                f.write(f"Publish Date : {date}\n")
                f.write(f"More info : {link}\n\n")
            print(f'File Saved : {index + 1}')

# Find_jobs_storing_in_single_file()

def Find_jobs_storing_in_individual_file():
    link = 'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation='
    html_doc = requests.get(link)
    print(html_doc.status_code,"\n")

    html_text = html_doc.text
    soup = BeautifulSoup(html_text , 'lxml')
    jobs = soup.find_all('li' , class_ = 'clearfix job-bx wht-shd-bx')

    for index,job in enumerate(jobs):  
        date = job.find('span' , class_ = 'sim-posted').text.replace("Work from Home" , "").strip()
        if 'few' in date :
            company_name = job.find('h3',class_ ='joblist-comp-name')
            skills = job.find('span' , class_ = 'srp-skills')
            link = job.header.h2.a["href"]      #calling href attribute by ["href"]

            company_name = company_name.get_text().replace(" (More Jobs)","").strip()
            skills = skills.get_text().strip()

            fil = open(f'{index+1}_Scrapped_Data.txt' , 'w')
            fil.write(f"{index+1}\nCompany name : {company_name}\nSkills : {skills}\nMore info : {link}\n\n")
            print(f"Data of company number {index+1} : Saved")


# Find_jobs_storing_in_individual_file()
