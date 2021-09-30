from bs4 import BeautifulSoup
import requests, re

# Searches the game on Steam

def steam(search_term):
    
    # Obtains the HTML of a search page using a get request
    url = f"https://store.steampowered.com/search/?term={search_term}"
    page = requests.get(url).text
    html = BeautifulSoup(page, "html.parser")
    
    # Narrow down the search by obatining the most relevant search, for Steam, it's usually the first on the list
    search_results = html.find(id="search_resultsRows")
    
    # If no results are found, exit
    try:
        game = list(search_results.descendants)[3]
    except AttributeError:
        print("No results found.")
        return()
    
    # Find the official title of the game
    name = game.find(class_="title").string
    
    # Check whether the game is on sale, and find the price
    sale = False
    original_price = None
    if game.find(class_="col search_price discounted responsive_secondrow") == None:
        price = game.find(class_="col search_price responsive_secondrow").string
    else:
        price = str(game.find(class_="col search_price discounted responsive_secondrow")).split(">")[-2][:-5]
        original_price = str(game.find(class_="col search_price discounted responsive_secondrow")).split(">")[3].split("<")[0].replace(" ", "")
        sale = True
    
    # Clean up the price format
    price = price.replace(" ", "").replace("\n", "")
    
    # Provide a link to the store page
    link = game['href']
    
    # Print the results
    print("Steam:")
    print(name)
    if sale:
        print("On sale!")
        print("Original price: " + original_price)
    print("Price: " + price)
    print(link)
        
    