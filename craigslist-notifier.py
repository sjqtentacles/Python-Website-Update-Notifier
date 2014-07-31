import urllib2
import sys,os
import time,threading

page = "http://losangeles.craigslist.org/sfv/cpg/"
timer = 60
notifier_title = "Craigslist"
notifier_message = "Updated"


def notify(title, subtitle, message):
    t = '-title {!r}'.format(title)
    s = '-subtitle {!r}'.format(subtitle)
    m = '-message {!r}'.format(message)
    os.system('terminal-notifier {}'.format(' '.join([m, t, s])))

webtry = urllib2.urlopen(page)
htmlprevious = webtry.read()
htmlcurrent = webtry.read()

def checkCraig():
	global htmlprevious
	global htmlcurrent
	global page
	global timer
	global notifier_title
	global notifier_message

	htmlcurrent = urllib2.urlopen(page).read()
	if(htmlcurrent != htmlprevious):
		notify(title = notifier_title,subtitle = '',message = notifier_message)
	htmlprevious = htmlcurrent
	threading.Timer(timer,checkCraig).start()
	
checkCraig()
	