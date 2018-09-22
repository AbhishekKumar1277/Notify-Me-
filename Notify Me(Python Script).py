# Import requests (to download the page)
import requests
# import BeautifulSoup to parse the data
from bs4 import BeautifulSoup
import smtplib
url = "Website to scrap data"
response = requests.get(url)
# parse the downloaded homepage and grab all text, then,
soup = BeautifulSoup(response.text, "html.parser")
#.findAll is used to find all the div and class named under quotes ex:question-summary-wrapper
new_panel = soup.findAll('div', {'class': 'question-summary-wrapper'})
values=[]
# for loop to iterate over the new_panel
for news in new_panel:
    temp = news.find('h2')
    if temp and str(temp.text) not in values:
        values.append(temp.text)
        msg = 'Tour message goes here'
        # set the 'from' address,
        fromadds = 'XXX@gmail.com'
        # set the 'to' addresses,
        toaddrs  = ['YYY@gmail.com']     
        #default gmail port is 587    
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        #here enter your gmail id and password to login..login is used to login your id into gmail:
        	#steps to login without any issue:
        		#remove any 2 step verification from your gmail.
        		#allow less secoure app login from your gmail account settings.
        server.login("XXX.com", "Your Password")
        server.sendmail(fromadds, toaddrs, msg)
        server.quit()
        break
    else:
    	print('No new Data')    
