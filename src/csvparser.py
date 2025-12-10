import requests
from bs4 import BeautifulSoup
import json
import pandas as pd
from datetime import datetime
import csv
import numpy as np
import matplotlib.pyplot as plt

def parse_csv(date):
    results = []

    with open("weather.csv", "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            if row["date"] == date:
                results.append(row)

    return results


target_date = '1997-5-22'
print(parse_csv(target_date))
