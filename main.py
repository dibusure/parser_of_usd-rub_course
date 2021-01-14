import requests
from bs4 import BeautifulSoup as bs
import time

class Currency:
	usdRub = 'https://www.google.com/search?q=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&oq=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&aqs=chrome..69i57j0i20i263j0l6.10436j1j9&sourceid=chrome&ie=UTF-8'
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}

	current_converted_price = 0
	difference = 5

	def __init__(self):
		self.current_converted_price = float(self.get_currency_price().replace(",", "."))

	def get_currency_price(self):
		full_page = requests.get(self.usdRub, headers=self.headers)

		soup = bs(full_page.content, 'html.parser')

		convert = soup.findAll("span", {"class": 'DFlfde', "class": "SwHCTb", "data-precision": 2})
		return convert[0].text

	def check_currency(self):
		currency = float(self.get_currency_price().replace(",", "."))
		if currency >= self.current_converted_price + self.difference:
			print("Курс сильно вырос, может пора что-то делать?")
		elif currency <= self.current_converted_price - self.difference:
			print("Курс сильно упал, может пора что-то делать?")

		print("Сейчас курс: 1 доллар (usd) = " + str(currency))
		time.sleep(3)
		self.check_currency()

currency = Currency()
currency.check_currency()



# https://www.youtube.com/watch?v=4L57oY3J378 5:05 - таймкод;