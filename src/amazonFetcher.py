import requests

from bs4 import BeautifulSoup


class AmazonProduct:
    def __init__(self, asin:str, name:str, price:float, currency:str, url:str):
        # The asin is a unique id given by amazon
        self.asin = asin
        self.name = name
        self.price = price
        self.currency = currency
        self.url = url


class AmazonFetcher:
    def __init__(self):
        # You can use this User Agen(UA) or use another one (may break the application)
        # Find your UA : https://whatmyuseragent.com/
        # List of UAs: https://gist.github.com/pzb/b4b6f57144aea7827ae4
        self.HEADERS = ({
            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15;) Gecko/20100101 Firefox/146.0',
            'Accept-Language': 'en-US, en;q=0.5'
        })
    
    def _request_url(self, url:str) -> requests.Response:
        """Request a URL"""
        return requests.get(url, headers=self.HEADERS, timeout=10)

    def _extract_asin(self, soup:BeautifulSoup) -> str:
        """Obtain the asin of a product"""
        try:
            asin = soup.find("input", attrs={"id":"asin"})
            asin_value = asin["value"]
            return asin_value
        except AttributeError as exc:
            raise ValueError(f"ASIN not found")
        
    def _extract_name(self, soup:BeautifulSoup) -> str:
        """Obtain the name of a product"""

        try:
            name = soup.find("span", attrs={"id":"productTitle"})
            name_value = name.text.strip()
            return name_value
        except Exception as exc:
            raise Exception from exc
    
    def _extract_price(self, soup:BeautifulSoup) -> float:
        """Obtain the price of a procuct"""

        try:
            price_whole = soup.find("span", attrs={"class":"a-price-whole"})
            price_fraction = soup.find("span", attrs={"class":"a-price-fraction"})
            
            price_whole_value = price_whole.text.replace(",","")
            price_fraction_value = price_fraction.text

            return float(price_whole_value + price_fraction_value)
        except Exception as exc:
            raise Exception from exc
        
    def _extract_currency(self, soup:BeautifulSoup) -> str:
        """Obtain the currecy for a product price"""

        try:
            currency = soup.find("span", attrs={"class":"a-price-symbol"})
            currency_value = currency.text
            return currency_value
        except Exception as exc:
            raise Exception from exc
        
    def fetch_product(self, url:str) -> AmazonProduct:
        """Obtain the asin, name, price and currency for a product
        
        This method returns a AmazonProduct object instance that can be
        used by other modules.
        """

        webpabe = self._request_url(url)
        soup = BeautifulSoup(webpabe.content, "lxml")

        asin = self._extract_asin(soup)
        name = self._extract_name(soup)
        price = self._extract_price(soup)
        currency = self._extract_currency(sopu)

        return AmazonProduct(asin, name, price, currency, url)