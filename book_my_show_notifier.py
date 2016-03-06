import urllib2
from bs4 import BeautifulSoup
import time
import yagmail


#book_my_show_url = raw_input("Enter the url :")

book_my_show_url = "https://in.bookmyshow.com/buytickets/deadpool-chennai/movie-chen-ET00038638-MT/20160306"

sender_email = raw_input("Enter your email address to send mail :")

email_password = raw_input("Enter your email password :")

receiver_email = raw_input("Enter the email address you want to receive  mail :")

while True:
	requester = urllib2.Request(book_my_show_url, headers={'User-Agent': "Magic Browser"})

	connector = urllib2.urlopen(requester)

	connector_reader = connector.read()

	soup = BeautifulSoup(connector_reader, "lxml")

	text = soup.get_text()

	if "Luxe Cinemas: Chennai" in text:
		sender = yagmail.SMTP(sender_email, email_password)
		sender.send(receiver_email, "Ticket reminder" , contents='Hola! Doors are opened !')
		time.sleep(300)

	else:
		print "Nope not yet"	