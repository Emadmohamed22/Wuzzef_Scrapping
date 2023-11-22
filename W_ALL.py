# importing libraries & methods
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import csv

# Numbers of pages
pages = range(20)

f = open("wuzzuf.illustor.csv","a",encoding="utf-8")
header = "job_title, company_name, job_type\n"
f.write(header)

# Scrapping Data from 0 to 19
for page in pages:
    # Inputing the url
    url=f"https://wuzzuf.net/search/jobs/?a=hpb&q=illustartor&start={page}"
    # Create a Client-based Request to Get the URL
    client=urlopen(url)
    # Getting the HTML Code of the Full Page
    html=client.read()
    # Closing the Request
    client.close
    # Creating an HTML parser Using Beaitfulsoup
    soup=bs(html,"html.parser")
    # Creating a Container forthe Needed Data
    containers=soup.find_all("div",{"class":"css-1gatmva e1v1l3u10"})
    for container in containers:
        Jtitle =container.findAll("h2",{"class":"css-m604qf"})
        job_title= Jtitle[0].text.strip()

        Cname=container.findAll("a",{"class":"css-17s97q8"})
        company_name = Cname[0].text.strip()

        Jtype=container.findAll("span",{"class":"css-1ve4b75 eoyjyou0"})
        job_type=Jtype[0].text.strip()

        f.write(job_title +", "+ company_name +", "+ job_type +"\n")
f.close