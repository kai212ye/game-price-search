from bs4 import BeautifulSoup
import requests, re, search_functions

search_term = input("Enter a game: ")
print()

# Search the game on Steam
search_functions.steam(search_term)