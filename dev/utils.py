from bs4 import BeautifulSoup
import requests 

### Time definitions
seconds = 1
minutes = 60
days = 1440
### Soup Handler Function
def getHtmlSoup(ingredientUrl):
	try:
		return BeautifulSoup(requests.get(ingredientUrl).content, 'html.parser')
	except Exception as error:
		print(error)
		print("Failed to get soup request.")

