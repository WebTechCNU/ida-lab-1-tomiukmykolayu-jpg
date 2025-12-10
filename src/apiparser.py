import requests
from bs4 import BeautifulSoup
import json
import pandas as pd
from datetime import datetime
import csv
import numpy as np
import matplotlib.pyplot as plt

def parse_api(api_url):
    response = requests.get(api_url)
    response.raise_for_status()

    data = response.json()

    # Зберігаємо у файл
    with open("result.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    print(f"Data saved to result.json from {api_url}")


parse_api('https://api.github.com/')