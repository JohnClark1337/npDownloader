"""
NPDownloader.py
Created by Jonathon Scofield

Designed to download all comics from the 8-bit theater on nuklearpower.com
Possibly will expand to further download capability later

"""


import os
from bs4 import BeautifulSoup
import wget
import urllib
import re


dirname = "8-bit Theater"
initialLink = 'http://www.nuklearpower.com/2001/03/02/episode-001-were-going-where/'

pathname = os.path.expanduser('~') + "\\Documents\\" + dirname
if os.path.exists(pathname) == False:
    os.makedirs(pathname)

looper = True
epnum = 1
while looper:
    
    content = urllib.request.urlopen(initialLink).read()
    looper = False #assume false until proven true
    soup = BeautifulSoup(content, features="html5lib")
    for image in soup.find_all('img'):
        check = image.get('alt')
        if "Episode" in check:
            ep = image.get('src')
            percentage = epnum / 1230 * 100
            print("  Comic Strip #" + str(epnum) + "  " + str(round(percentage, 2)) + "%")
            dloc = pathname + "\\" + str(epnum) + '.jpg'
            epnum += 1
            wget.download(ep, dloc)

    for links in soup.find_all('a'):
        checknext = str(links.get('rel'))
        if "next" in checknext:
            looper = True
            initialLink = links.get('href')

print("  Series Complete  100%")




