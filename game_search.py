from bs4 import BeautifulSoup
import requests, re, search_functions

# Prompt the user to enter a game to search
search_term = input("Enter a game: ")
print()

# Search the game on Steam
search_functions.steam(search_term)