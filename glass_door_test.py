
# import pip
# from pip._internal import main
# #installing packages locally
# def install(package):
#     """install packages"""
#     if hasattr(pip, 'main'):
#         pip.main(['install', package])
#     else:
#         main(['install', package])
#uncomment them to install
# install('selenium')
# install('selenium')
# install('bs4')
# install('webdriver_manager')

#importing the libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import datetime
#Stores the time so that when a csv file is created then its time stamp is also created


chrome_options=Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
chrome_options.add_argument("--incognito")
#Enabling Icognito

driver = webdriver.Chrome(options=chrome_options)

#counter variable 
url_df=pd.read_csv("City_names.csv")
URLS=url_df['Links '].to_list()
i=0
#Iterating through URLS list essentially going through all the links 
for url in URLS:
    #date
    x=datetime.datetime.now()
    #name of the places
    name_of_file=url_df['City'].to_list()
    driver.get(url)
    company_name=[]
    # iterating through elements of particular div classes
    for elements in driver.find_elements(by=By.XPATH,value='//div[@class="d-flex justify-content-between align-items-start"]'):
                       
        company_name.append(elements.text)
    job_title=[]
    for element in driver.find_elements(by=By.XPATH, value='.//a[@class="jobLink job-search-key-1rd3saf eigr9kq1"]'):
        job_title.append(element.text)
    location=[]
    for element in driver.find_elements(by=By.XPATH,value='//div[@class="d-flex flex-wrap job-search-key-1m2z0go e1rrn5ka2"]'):
        location.append(element.text)

    salary=[]
    #used try catch here as many classes dont have salary 
    for element in driver.find_elements(by=By.XPATH,value='//div[@class="d-flex flex-column pl-sm css-1buaf54 job-search-key-1mn3dn8 e1rrn5ka0"]'):
        
        try:
            salary.append(element.find_element(by=By.XPATH,value='.//span[@class="job-search-key-1hbqxax e1wijj240"]').text)
        except:
            salary.append('')
    #making a pandas df and transposing the values as list is horizontal 
    df=pd.DataFrame([company_name,job_title,location,salary]).T
    #adding column names
    df.columns=['Company_name','Job_title','Location','Salary']
    #converting it to csv
    print(f'{name_of_file[0+i]} city jobs')      
    df.to_csv(f'Glass_Door_jobs_in_{name_of_file[0+i]}_{x.day}day{x.month}month_at{x.hour}_{x.minute}.csv',index=False)
    #incrementing the counter
    i=i+1
    