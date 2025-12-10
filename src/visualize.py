import requests
from bs4 import BeautifulSoup
import json
import pandas as pd
from datetime import datetime
import csv
import numpy as np
import matplotlib.pyplot as plt

def visualize_data():
    df = pd.read_csv("weather.csv")

    df["date"] = pd.to_datetime(df["date"])

    plt.figure(figsize=(10, 5))
    plt.plot(df["date"], df["temp"])
    plt.title("Temperature over time")
    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")
    plt.grid(True)
    plt.savefig("plot_temp.png")
    plt.close()

    plt.figure(figsize=(10, 5))
    plt.plot(df["date"], df["humidity"])
    plt.title("Humidity over time")
    plt.xlabel("Date")
    plt.ylabel("Humidity (%)")
    plt.grid(True)
    plt.savefig("plot_humidity.png")
    plt.close()

    print("Visualizations saved: plot_temp.png, plot_humidity.png")


visualize_data()