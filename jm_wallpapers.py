from bs4 import BeautifulSoup
from string import ascii_lowercase
import urllib.request
import requests
import shutil
import os
counter = 0

baseUrl = 'http://justinmaller.com'
url ='http://justinmaller.com/wallpapers/'
baseSaveLocation = 'F:/git/justinMaller_wallpapers/jm_wallpapers/'

html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

for comicImageTag in soup.findAll('div', attrs={'class': 'project-image'}):
	comicImageHtml = comicImageTag.findAll('a')
	# comicImageLinkName= comicImageLink['src'][55:]
	# print (comicImageHtml)

	for a in comicImageHtml:
		link = a['href']
		# print ("Links :" +link)

		singleWallpaper = urllib.request.urlopen(baseUrl+link).read()
		singlewallpapersoup = BeautifulSoup(singleWallpaper,'html.parser')

		for wallpapers in singlewallpapersoup.findAll('div', attrs={'id':'wallwindow'}):
			wallpaperLink = wallpapers.find('img',src=True)
			wallpaperName = wallpaperLink['src'][51:]
			# print ("Wallpaper links: "+wallpaperLink['src'])
			# print ("Wallpaper name: "+wallpaperName)

			if not os.path.exists(baseSaveLocation+wallpaperName):
				try:
					with open(baseSaveLocation+wallpaperName, 'wb') as f:
						f.write(urllib.request.urlopen(wallpaperLink['src']).read())
						print(u"Downloaded: "+wallpaperName+"\n")
				except:
					print("exception, so skipping this")
					pass
			else:
				print("File already exists")				

