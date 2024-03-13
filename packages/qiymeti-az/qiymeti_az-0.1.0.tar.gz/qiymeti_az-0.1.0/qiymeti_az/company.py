import requests
from bs4 import BeautifulSoup

class Company:
    def __init__(self, name, grid_name, item_name, title, price, url, query, page=None):
        self.name = name
        self.grid_name = grid_name
        self.item_name = item_name
        self.title = title
        self.price = price
        self.url = url
        self.query = query
        self.page = page

    def scrape(self, query, page=None):
        try:
            url = f"{self.url}?{self.query}={query}{('&'+self.page+'='+page) if page else ''}".replace(' ', '+')
            response = requests.get(url)

            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                products_grid_div = soup.find('div', class_=self.grid_name)
                result = {}
                for prod_item_div in products_grid_div.find_all('div', class_=self.item_name):
                    title_tag_content = prod_item_div.select_one(f'{self.title}')
                    price_tag_content = prod_item_div.select_one(f'{self.price}')

                    if price_tag_content:
                        result[title_tag_content.get_text(strip=True)] = price_tag_content.get_text(strip=True)
                return result
            else:
                return [f"Failed to retrieve the webpage. Status code: {response.status_code}"]
        except:
            return [f"Failed to connect"]

    def search(self, query, category=None):
        return self.scrape(f'{query}{" "+category if category else ""}')
