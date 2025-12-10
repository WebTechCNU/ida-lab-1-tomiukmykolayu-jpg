import requests
from bs4 import BeautifulSoup
import json
import pandas as pd
from datetime import datetime
import csv
import numpy as np
import matplotlib.pyplot as plt

def parse_web_page(url):
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')

    text = soup.get_text(separator=" ", strip=True)

    return text


print(parse_web_page('https://fmi.chnu.edu.ua/')[:255])
