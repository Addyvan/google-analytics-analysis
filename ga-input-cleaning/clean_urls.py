import pandas as pd

df = pd.read_csv("data/pedia_1.csv")

cleaned_urls = []

for url in df["urls"]:
    cleaned_urls.append(url[24:])

regex_string = ""

for i, url in enumerate(cleaned_urls):
    regex_string += url
    if i < (len(cleaned_urls) -1):
        regex_string += "|"

print(regex_string)