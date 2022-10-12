import time
import json
import numpy as np
from time_data import *
from plot import *
from bs4 import BeautifulSoup
from urllib.request import urlopen

cases_url = 'https://steamcommunity.com/market/search/render/?query=Case&start=0&count=50&search_descriptions=0&sort_column=price&sort_dir=asc&appid=730&category_730_ItemSet%5B%5D=any&category_730_ProPlayer%5B%5D=any&category_730_StickerCapsule%5B%5D=any&category_730_TournamentTeam%5B%5D=any&category_730_Weapon%5B%5D=any&category_730_Type%5B%5D=tag_CSGO_Type_WeaponCase'
#knife_url = 'https://steamcommunity.com/market/search/render/?query=&start=0&count=1000&search_descriptions=0&sort_column=price&sort_dir=asc&appid=730&category_730_ItemSet%5B%5D=any&category_730_ProPlayer%5B%5D=any&category_730_StickerCapsule%5B%5D=any&category_730_TournamentTeam%5B%5D=any&category_730_Weapon%5B%5D=any&category_730_Type%5B%5D=tag_CSGO_Type_Knife'

page = urlopen(cases_url)

data = json.loads(page.read().decode())
html = data['results_html']

soup = BeautifulSoup(html, 'html.parser')

objects = soup.findAll(class_="market_listing_row_link")

data = []
history = {}

for g in objects:
    link = g["href"]
    case_name = g.find(class_="market_listing_item_name").text
    price = g.find('span', {'data-price': True}).text
    if (link[-4::] == 'Case' or link[-1].isdigit()):
    	data.append((price, case_name))

size = len(data)

cases = np.empty(size, dtype=object)
prices = np.empty(size, dtype=float)

for i in range(size):
	prices[i] = data[i][0].strip('$')
	cases[i] = data[i][1]

print(mdy)
displayPlot(cases, prices)