# Web-Scrapping_timesjob.com
Scrapped timesjob.com to get the data of companies offering jobs to the candidates having python as one of the skill.

I have made 3 functions in python for scrapping job opportunities from jobs.com the 1st one being Find_jobs(), **Find_jobs()** first asks you an unfamiliar skill in a terminal, then scrappes the job opportunity which was published few days ago and requires python as skill to work then out of these job opportunity it filters out the jobs with a skill you are unfamiliar with and prints the list of companies with details such as company name , skills , publish date and a link to apply and get more information for a particular job. These function runs continuesly after a break of 1 minute so that you don't have to run it again and again. I have used the following libraries and module for these project:
- [Beautifull Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Requests](https://www.w3schools.com/python/module_requests.asp)
- [Time](https://www.geeksforgeeks.org/python-time-module/) 

The other 2 functions being **Find_jobs_storing_in_single_file()**, **Find_jobs_storing_in_individual_file()** are developed to store the data of job opportunities in files instead of showing it right away in terminal. Find_jobs_storing_in_single_file() stores the data (includes company name , skills , publish date and a link to apply and get more information) of all the companies in a single file named scrapped_data.txt whereas Find_jobs_storing_in_individual_file() stores the data of each company in a individual text file named <serial no.>_Scrapped_Data.txt. Since these function need not need to call again and again, function call for these functions are commented off.
