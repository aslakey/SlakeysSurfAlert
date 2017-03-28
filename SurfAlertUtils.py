#SurfAlertUtils
import csv   
from bs4 import BeautifulSoup
import urllib.request
import re
import smtplib #to send emails
from email.mime.text import MIMEText #email text


def adduser(user):
    if len(user)<4:
        print("Please provide four argument: User, Email, Surf Spot, URL")
        return()
    try:
        with open(r'data/SurfAlerts.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow(user)
            print("User successfully added!")
    except:
        with open('data/SurfAlerts.csv', 'wb') as f:
            wr = csv.writer(f)
            wr.writerow(mylist)
        print("Created data file and added user")
    return()

def run():
    with open('data/SurfAlerts.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            user = row[0]
            email = row[1]
            spot = row[2]
            website = row[3]
            with urllib.request.urlopen(website) as content:
                search(content,user,email,spot)
    return()

def search(content,user,email,spot):
    soup = BeautifulSoup(content, "lxml")
    div = soup.find('div', id="msw-js-fcc")
    data_string = div.get('data-chartdata')
    pattern="maxBreakingHeight...."
    result = re.findall(pattern, data_string)[-6:]
    for height in result:
        int_height = int(re.search(r'\d+', height).group())
        if int_height > 5:
            Email(user,email,spot)
            print("Sent Surf Alert to "+email+" for "+spot)
            return()

def Email(user,email,spot):
    print("EMAIL Function")
    # Open a plain text file for reading.  For this example, assume that
    # the text file contains only ASCII characters.
    fp = open('data/email.txt', 'r')
    # Create a text/plain message
    msg = MIMEText(fp.read())
    fp.close()

    me = 'acslakey@gmail.com'
    you = email
    msg['Subject'] = 'SURF ALERT for %s' % spot
    msg['From'] = me
    msg['To'] = email

    # Send the message via our own SMTP server, but don't include the
    # envelope header.
    s = smtplib.SMTP('smtp.gmail.com',587) #port 465 or 587
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login('acslakey@gmail.com','1927octavia')
    #to use lcal:
    #python -m smtpd -n -c DebuggingServer localhost:1025
    #s = smtplib.SMTP('localhost',1025)
    s.sendmail(me, [you], msg.as_string())
    s.quit()
    return()
