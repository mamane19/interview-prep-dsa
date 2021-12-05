# Your task is to write a program that reads this web page:
# and gives back a list of the 10 most expensive books
# (among the most popular, books with many reviews).

# import requests
# from bs4 import BeautifulSoup


"""
THIS IS THE FUNCTION VERSION OF THE main.py file. This means that there is separation of concern here and every step
is working as a function now which is more organized. You can do either, as long as we get the same result
"""

import requests
import bs4
import time
import sys

base_url = "https://www.amazon.com/best-sellers-books-Amazon/zgbs/books/ref=zg_bs_pg_1?_encoding=UTF8&pg=1"

print("Fetching data from amazon web page...\n")
time.sleep(1)


# Make soup object
def make_soup(url):
    # In the event of a network problem (e.g. DNS failure, refused connection, etc), wrap entire program in a try and
    # expect
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/56.0.2924.76 "
            "Safari/537.36",
            "Upgrade-Insecure-Requests": "1",
            "DNT": "1",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,/;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate",
        }
        res = requests.get(url, headers=headers, params={"wait": 2})
        soup = bs4.BeautifulSoup(res.text, "lxml")
        return soup
    except requests.exceptions.RequestException as e:
        print("Something went wrong", e)


def books_component(s):
    if not len(s.select(".zg-item-immersion")):
        print(
            "Oops! The webpage has refused to serve data. It could be connections issue or the request is taking "
            "long. Please run the program again"
        )
        sys.exit()
    else:
        return s.select(".zg-item-immersion")


def get_popular_books(s):
    popular_books = []
    for item in books_component(s):
        if "a-star-5" in str(item):
            for book_names in item.select(".p13n-sc-truncated"):
                popular_books.append(book_names.getText().strip())
    return popular_books


# Get prices for most popular books
def popular_books_prices(s):
    prices_of_popular_books = []
    for item in books_component(s):
        if "a-star-5" in str(item):
            for prices in item.find(name="span", class_="p13n-sc-price"):
                prices_of_popular_books.append(float(prices.getText().replace("$", "")))
    return prices_of_popular_books


# Get top 10 prices from most popular books
def top_ten_prices(s):
    top_ten = []
    for price in popular_books_prices(s):
        top_ten.append(price)
    max_range = 10
    top_ten.sort()
    top_ten = top_ten[-max_range:]
    return top_ten


# Get top 10 most expensive books
def top_most_expensive(s):
    ten_most_expensive = []
    unsorted_prices = []
    for item in books_component(s):
        if "a-star-5" in str(item):
            for val in top_ten_prices(s):
                if f"${val}" in str(item):
                    ten_most_expensive.append(
                        item.find(name="div", class_="p13n-sc-truncate").text.strip()
                    )
                    # Not important to do
                    for prices in item.find(name="span", class_="p13n-sc-price"):
                        unsorted_prices.append(prices)

    # Not important to do
    return [
        {
            ten_most_expensive[i]: unsorted_prices[i]
            for i in range(len(ten_most_expensive))
        }
    ]


# This part is not that important, but it's great if you want your program to work in all of the pages in the website.
for x in range(1, 999):
    soup = make_soup(
        f"https://www.amazon.com/best-sellers-books-Amazon/zgbs/books/ref=zg_bs_pg_1?_encoding=UTF8&pg={x}"
    )
    top_most_expensive(soup)
    if not soup.find("li", {"class": "a-disabled a-last"}):
        pass
    else:
        break

# Call all your functions down here
soup_object = make_soup(base_url)
books_component(soup_object)
get_popular_books(soup_object)
popular_books_prices(soup_object)
top_ten_prices(soup_object)

print(top_most_expensive(soup_object))
