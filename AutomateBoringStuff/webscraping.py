#! python3
import bs4, requests

def getAmazonPrice(productUrl):
	#set user-agent to get around bot/scraping filters
	#http://docs.python-requests.org/en/master/user/quickstart/
	res = requests.get(productUrl,
		headers={ "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36" })

	res.raise_for_status()

	soup= bs4.BeautifulSoup(res.text, 'html.parser')

	elems = soup.select('.offer-price')
	return elems[0].text.strip()

theURL = input("Enter web address of Amazon product page:")
print(getAmazonPrice(theURL))
