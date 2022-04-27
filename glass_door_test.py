
import pip
from pip._internal import main
#installing packages locally
def install(package):
    """install packages"""
    if hasattr(pip, 'main'):
        pip.main(['install', package])
    else:
        main(['install', package])
#uncomment them to install
# install('selenium')
# install('selenium')
# install('bs4')
# install('webdriver_manager')

#importing the libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import datetime
#Stores the time so that when a csv file is created then its time stamp is also created
x=datetime.datetime.now()

chrome_options = webdriver.ChromeOptions()
#Enabling Icognito
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=chrome_options)
#For adding glassdoor sites add the urls and update URLS list
# url1="https://www.glassdoor.com/Job/saint-petersburg-jobs-SRCH_IL.0,16_IC1154421.htm"
# url2="https://www.glassdoor.com/Job/jobs.htm?sc.keyword=&clickSource=searchBox&locId=1154162&locT=C&locName=Hialeah%2C%20FL%20(US)"
# url3="https://www.glassdoor.com/Job/brandon-jobs-SRCH_IL.0,7_IC1154386.htm"
# url4="https://www.glassdoor.com/Job/jobs.htm?sc.keyword=&clickSource=searchBox&locId=1138213&locT=C&locName=Washington%2C%20DC%20(US)"
# url5="https://www.glassdoor.com/Job/jobs.htm?sc.keyword=&clickSource=searchBox&locId=1132348&locT=C&locName=New%20York%2C%20NY%20(US)"
# url6="https://www.glassdoor.com/Job/jobs.htm?sc.keyword=&clickSource=searchBox&locId=1146821&locT=C&locName=Los%20Angeles%2C%20CA%20(US)"
# url7="https://www.glassdoor.com/Job/jobs.htm?sc.keyword=&clickSource=searchBox&locId=1128808&locT=C&locName=Chicago%2C%20IL%20(US)"
# url8="https://www.glassdoor.com/Job/jobs.htm?sc.keyword=&clickSource=searchBox&locId=1140171&locT=C&locName=Houston%2C%20TX%20(US)"
# url9="https://www.glassdoor.com/Job/jobs.htm?sc.keyword=&clickSource=searchBox&locId=1152672&locT=C&locName=Philadelphia%2C%20PA%20(US)"
# url10="https://www.glassdoor.com/Job/jobs.htm?sc.keyword=&clickSource=searchBox&locId=1133904&locT=C&locName=Phoenix%2C%20AZ%20(US)"
# url11="https://www.glassdoor.com/Job/jobs.htm?sc.keyword=&clickSource=searchBox&locId=1140494&locT=C&locName=San%20Antonio%2C%20TX%20(US)"
# url12="https://www.glassdoor.com/Job/jobs.htm?sc.keyword=&clickSource=searchBox&locId=1147311&locT=C&locName=San%20Diego%2C%20CA%20(US)"
# url13="https://www.glassdoor.com/Job/jobs.htm?sc.keyword=&clickSource=searchBox&locId=1139977&locT=C&locName=Dallas%2C%20TX%20(US)"
# url14="https://www.glassdoor.com/Job/jobs.htm?sc.keyword=&clickSource=searchBox&locId=1147436&locT=C&locName=San%20Jose%2C%20CA%20(US)"
# url15="https://www.glassdoor.com/Job/jobs.htm?sc.keyword=&clickSource=searchBox&locId=1139761&locT=C&locName=Austin%2C%20TX%20(US)"
# URLS=[url1,url2,url3,url4,url5,url6,url7,url8,url9,url10,url11,url12,url13,url14,url15]
#counter variable 
url_df=pd.read_csv("City_names.csv")
URLS=url_df['Links '].to_list()
i=0
#Iterating through URLS list essentially going through all the links 
for url in URLS:
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
    df.to_csv(f'Glass_Door_jobs_in_{name_of_file[0+i]}_{x.day}day{x.month}month_at{x.hour}_{x.minute}.csv',index=False)
    #incrementing the counter
    i=i+1
    