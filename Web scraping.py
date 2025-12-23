import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

def scrape_books(number_of_pages=3):
    """
    Extracts book data across multiple pages to create a custom dataset.
    Demonstrates: HTML navigation, Data cleaning, and Dataset creation.
    """
    base_url = "http://books.toscrape.com/catalogue/page-{}.html"
    headers = {"User-Agent": "Mozilla/5.0"}
    all_books = []

    print(f"📡 Starting extraction for {number_of_pages} pages...")

    for page in range(1, number_of_pages + 1):
        url = base_url.format(page)
        response = requests.get(url, headers=headers)
        
        if response.status_code != 200:
            print(f"❌ Failed to retrieve page {page}")
            continue
            
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Identify the relevant data containers
        book_containers = soup.find_all('article', class_='product_pod')
        
        for book in book_containers:
            # Handling HTML structure to gather accurate data
            title = book.h3.a['title']
            price = book.find('p', class_='price_color').text.replace('Â', '')
            availability = book.find('p', class_='instock availability').text.strip()
            
            # Extracting star rating from class names (e.g., "star-rating Three")
            rating = book.p['class'][1] 
            
            all_books.append({
                "Title": title,
                "Price": price,
                "Rating": rating,
                "Availability": availability
            })
        
        print(f"✅ Page {page} scraped successfully.")
        time.sleep(1) # Ethical scraping: pause to avoid overwhelming the server

    # Create custom dataset tailored to analysis needs
    df = pd.DataFrame(all_books)
    df.to_csv('titanic_era_style_books_dataset.csv', index=False)
    print("\n💾 Dataset 'titanic_era_style_books_dataset.csv' created successfully.")
    print(df.head())

if __name__ == "__main__":
    scrape_books(3) # Scrapes first 3 pages
