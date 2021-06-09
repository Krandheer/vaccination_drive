import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def get_population(url):
	driver = webdriver.Chrome(executable_path = '/Users/randheerkumar/Downloads/chromedriver')
	driver.get(url)
	time.sleep(5)
	html = driver.page_source
	soup = BeautifulSoup(html,"html.parser")
	d = soup.find("div", {'class':'maincounter-number'}).find("span")
	
	d1 = d.find("span", class_ = 'rts-nr-int rts-nr-10e9').text
	d2 = d.find("span", class_ =  'rts-nr-int rts-nr-10e6').text
	d3 = d.find("span", class_ =  'rts-nr-int rts-nr-10e3').text
	d4 = d.find("span", class_ =  'rts-nr-int rts-nr-10e0').text
	data=int(d1+d2+d3+d4)
	return data
	
#population_ind = get_population('https://www.worldometers.info/world-population/india-population/')
# url2 = 'https://www.mygov.in/covid-19'

def vaccinated(url):

	population_ind = get_population('https://www.worldometers.info/world-population/india-population/')
	
	r = requests.get(url).content
	soup = BeautifulSoup(r, 'lxml')
	vac = soup.find("div", class_ = 'vaccinated-view')

	vac_tot = vac.find("div", class_ = 'total-vcount')
	vac_tot = vac_tot.find('strong').text
	print(f'total number of people vaccinated: {vac_tot}')

	vac_y = vac.find('div', class_ = 'yday-vcount')
	vac_y = vac_y.find('strong').text
	print(f'vaccinated day before: {vac_y}')
	vac_y=int(vac_y.replace(',',''))

	pop = f'{population_ind:,}'
	print(f'Population of India: {pop}')

	take_day = population_ind//vac_y

	print(f'number of days it will take to vaccinate india: {take_day}')

vaccinated('https://www.mygov.in/covid-19')

