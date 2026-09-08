import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = "https://books.toscrape.com/catalogue/page-{}.html"

data = []

for page in range(1, 51):

    url = base_url.format(page)

    response = requests.get(url)

    print("Scraping page:", page)

    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find_all("article", class_="product_pod")

    for book in books:

        rating = book.find("p", class_="star-rating")["class"][1]

        book_url = "https://books.toscrape.com/catalogue/" + book.h3.a["href"]

        title = book.h3.a["title"]

        price = book.find(
            "p",
            class_="price_color"
        ).text.replace("Â£", "GBP ")

        availability = book.find(
            "p",
            class_="instock availability"
        ).text.strip()

        data.append({
            "Title": title,
            "Price": price,
            "Availability": availability,
            "Rating": rating,
            "Book URL": book_url
        })


# Convert data into DataFrame
df = pd.DataFrame(data)

# Menu
while True:

    print("\n========== BOOK SCRAPER ==========")
    print("1. Search book")
    print("2. Filter by price")
    print("3. Filter by rating")
    print("4. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":

        search = input("Enter a book name to search: ")

        results = df[
            df["Title"].str.contains(search, case=False, na=False)
        ]

        if len(results) > 0:
            print("\nBooks found:")
            print(
                results[
                    ["Title", "Price", "Availability", "Rating", "Book URL"]
                ].to_string(index=False)
            )
        else:
            print("\nNo books found.")

    elif choice == "2":

        try:
           max_price = float(input("Enter maximum price: "))
        except ValueError:
           print("\nPlease enter a valid number.")
           continue

        df["Price_Number"] = (
            df["Price"]
            .str.replace("GBP ", "", regex=False)
            .astype(float)
        )

        price_results = df[df["Price_Number"] <= max_price]

        if len(price_results) > 0:
            print("\nBooks below your price:")
            print(
                price_results[
                    ["Title", "Price", "Availability", "Rating", "Book URL"]
                ].to_string(index=False)
            )
        else:
            print("\nNo books found below this price.")

    elif choice == "3":

        rating_choice = input("Enter rating (1-5): ")

        rating_map = {
            "1": "One",
            "2": "Two",
            "3": "Three",
            "4": "Four",
            "5": "Five"
        }

        rating_choice = rating_map.get(rating_choice, rating_choice)

        rating_results = df[
            df["Rating"].str.lower() == rating_choice.lower()
        ]

        if len(rating_results) > 0:
            print("\nBooks with selected rating:")
            print(
                rating_results[
                    ["Title", "Price", "Availability", "Rating", "Book URL"]
                ].to_string(index=False)
            )
        else:
            print("\nNo books found with this rating.")

    elif choice == "4":

        print("\nThank you for using Book Scraper!")
        break

    else:

        print("\nInvalid choice. Please enter 1, 2, 3, or 4.")

# Save data
df.to_csv(
    "scraped_data.csv",
    index=False,
    encoding="utf-8-sig"
)

print("\nScraping completed!")
print("Total books scraped:", len(data))