from .company import Company

# Define default instances
kontakt_home = Company(
    name='Kontakt Home', 
    grid_name='products-grid', 
    item_name='prodItem', 
    title='.prodItem__title', 
    price='.prodItem__prices b', 
    url="https://kontakt.az/az/catalogsearch/result/", 
    query="q", 
    page="p"
)

baku_electronics = Company(
    name='Baku Electronics', 
    grid_name='catalog__wrap', 
    item_name='product__card', 
    title='.product__title', 
    price='.product__price--cur', 
    url="https://www.bakuelectronics.az/search.html", 
    query="query", 
    page="page"
)

world_telecom = Company(
    name='World Telecom', 
    grid_name='filterProducts', 
    item_name='productCard', 
    title='.productName', 
    price='.productPrice span', 
    url="https://w-t.az/axtaris", 
    query="s", 
    page="page"
)

irshad = Company(
    name='Irshad', 
    grid_name='filterProducts', 
    item_name='item', 
    title='.productName', 
    price='realPrice', 
    url="https://irshad.az/mehsullar", 
    query="q", 
    page="p"
)

music_gallery = Company(
    name='MG Store', 
    grid_name='custom-products', 
    item_name='box-view', 
    title='.name a', 
    price='.price-new', 
    url="https://www.mgstore.az/search/", 
    query="search", 
    page=""
)

bytelecom = Company(
    name='ByTelecom', 
    grid_name='filter-products', 
    item_name='product', 
    title='.product-name', 
    price='.prices h5', 
    url="https://bytelecom.az/search", 
    query="search", 
    page=""
)

from fuzzywuzzy import fuzz
def search(query, target):
    
    if fuzz.partial_ratio(target.lower(), "kontakt home") > 75:
        return kontakt_home.search(query)
    elif fuzz.partial_ratio(target.lower(), "baku electronics") > 75:
        return baku_electronics.search(query)
    elif fuzz.partial_ratio(target.lower(), "world telecom") > 75:
        return world_telecom.search(query)
    elif fuzz.partial_ratio(target.lower(), "irshad") > 75:
        return irshad.search(query)
    elif fuzz.partial_ratio(target.lower(), "music gallery") > 75:
        return music_gallery.search(query)
    elif fuzz.partial_ratio(target.lower(),  "bytelecom") > 75:
        return bytelecom.search(query)
    else:
        return "Target company not found"
