# pip install requests
# pip install beatifulsoup4
# pip install lxml

# importing libraries & methods
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import csv

# Inputing the url
url="https://wuzzuf.net/search/jobs/?q=illustartor&a=hpb"
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
# Accessing Page Elements
Jtitle=containers[0].findAll("h2",{"class":"css-m604qf"})
print(Jtitle[0].text)
Cname=containers[0].findAll("a",{"class":"css-17s97q8"})
print(Cname[0].text)
Jtype=containers[0].findAll("span",{"class":"css-1ve4b75 eoyjyou0"})
print(Jtype[0].text)
# Bringing it All Together
f = open("wuzzuf.illustor.csv","w")
header = "job_title, company_name, job_type\n"
f.write(header)

for container in containers:
    Jtitle =container.findAll("h2",{"class":"css-m604qf"})
    job_title= Jtitle[0].text.strip()

    Cname=container.findAll("a",{"class":"css-17s97q8"})
    company_name = Cname[0].text.strip()

    Jtype=container.findAll("span",{"class":"css-1ve4b75 eoyjyou0"})
    job_type=Jtype[0].text.strip()

    f.write(job_title +", "+ company_name +", "+ job_type +"\n")
f.close

# Inputting the File into Pandas



