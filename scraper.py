import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_data(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        items = []
        for title in soup.find_all('h2', class_='product-title'):
            items.append(title.text.strip())
        
        df = pd.DataFrame(items, columns=['Product Name'])
        df.to_csv('output.csv', index=False)
        print("Data scraped and saved successfully!")
    else:
        print("Failed to retrieve webpage.")

if __name__ == "__main__":
    # Test URL (Replace with your target website)
    target_url = "https://example.com"
    scrape_data(target_url)
