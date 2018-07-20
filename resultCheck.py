import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
print("Welcome to the Result Checker for 2nd Semester")

#taking the semester in consideration
#sem = input('Enter your Semester-')
#to set proper length of the semester string to be compared
#if len(sem)==1:
#    sem = '0'+sem

#taking branch in consideration
def getBranch(b):
    if b=='CSE' or b=='cse':
        return '001 : B.Tech - Computer Science and Engineering'
    elif b=='ECE' or b=='ece':
        return '003 : B.Tech -  Electronics & Communication Engineering'
    elif b=='CE' or b=='ce':
        return '009 : B.Tech -  Civil Engineering'
    elif b=='CHE' or b=='che':
        return '005 : B.Tech -  Chemical Engineering'
    elif b=='EE' or b=='ee':
        return '002 : B.Tech -  Electrical Engineering'
    elif b=='ME' or b=='me':
        return '004 : B.Tech -  Mechanical Engineering'
    elif b=='BT' or b=='bt':
        return '008 : B.Tech -  Bio Technology'
    elif b=='BME'or b=='bme':
        return '007 : B.Tech -  Bio Medical Engineering'
    elif b=='BCA' or b=='bca':
        return '041 : Bachelor of  Computer Application (BCA)'


branch = input('Enter your branch(Short form only like CSE, ECE etc): ');
#Now, converting branch to standard format as specified on the webpage
branch = getBranch(branch)
#print(branch)
#sending the get request to the server
url = 'https://www.dcrustedp.in/show_chart.php';
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
#getting all <td> tags present on the page
tags = soup('td')
flag = 0
out = '\n\n\tBranch not found\n\n'

for tag in tags:
    #working along the vertical side of table
    if tag.contents[0] == branch and flag!=1:
        #print('Branch found')
        flag = 1
        continue;
    if flag==1:
        flag = 0
        #now, working on the horizontal side of table
        if tag.contents[0]!='X':
            out = "\n\n\tResult DECLARED!!\n\n"
            break
        else:
            out = "\n\n\tResult NOT Declared Yet\n\n"
            break

print(out)
