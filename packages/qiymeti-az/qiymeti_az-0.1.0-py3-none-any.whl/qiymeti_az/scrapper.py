import requests
from bs4 import BeautifulSoup

def scrape_website(url, grid_name, item_name, title, price, query, page=None):
    try:
        url = f"{url}?{query}={query}{('&'+page+'='+page) if page else ''}".replace(' ', '+')
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            products_grid_div = soup.find('div', class_=grid_name)
            result = {}
            for prod_item_div in products_grid_div.find_all('div', class_=item_name):
                title_tag_content = prod_item_div.select_one(f'{title}')
                price_tag_content = prod_item_div.select_one(f'{price}')

                if price_tag_content:
                    result[title_tag_content.get_text(strip=True)] = price_tag_content.get_text(strip=True)
            return result
        else:
            return [f"Failed to retrieve the webpage. Status code: {response.status_code}"]
    except:
        return [f"Failed to connect"]
