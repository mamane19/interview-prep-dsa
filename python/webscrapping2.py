# Your task is to write a program that reads this web page:
# and gives back a list of the 10 most expensive books
# (among the most popular, books with many reviews).


import requests
import bs4
import time

base_url = "https://www.amazon.com/best-sellers-books-Amazon/zgbs/books/ref=zg_bs_pg_1?_encoding=UTF8&pg={}"
start_time = time.time()


def soup_it(url):
    """
    Returns a soup object from the url
    """
    # we are going to make the program run as long as the status is not 200
    response = requests.get(url)
    while True:
        if response.status_code == 200:
            break
        else:
            # print("The request did not go through. Please try again later.\n")
            print("\nOops, we have a {} error".format(response.status_code))
            print("Retrying...\n")
            time.sleep(2)
            response = requests.get(url)
    return bs4.BeautifulSoup(response.text, "html.parser")


def books_data(soup):
    """
    Returns a list of tuples with the title, price and reviews of the books
    """
    if time.time() - start_time > 2:
        print("Be Patient. It is taking a while to load the data...")
        time.sleep(2)

    books = soup.select(".zg-item-immersion")
    stars = soup.select(".a-icon-row")
    # let's get the data from the books and match it with the stars
    books_list = []
    for book, star in zip(books, stars):
        title = book.select_one(".p13n-sc-truncate").text
        price = book.select_one(".p13n-sc-price").text
        stars = star.select(".a-link-normal")[1].text
        books_list.append({"title": title, "price": price, "stars": stars})
    return books_list


def get_most_popular_books(books_list):
    """
    Returns a list of the most popular books based on the reviews.
    Meaning, the books with the most stars.
    """
    most_popular_books = sorted(
        books_list, key=lambda k: float(k["stars"].replace(",", "")), reverse=True
    )
    return most_popular_books[:10]


# get the most expensive books among the most popular
def get_10_most_expensive_books(most_popular_books):
    """
    Returns a list ordered by price of the most popular books in descending order
    """
    return sorted(
        most_popular_books,
        key=lambda k: float(k["price"].replace("$", "")),
        reverse=True,
    )[:10]


def main():
    print("Scrapping...")
    print("It may take a while to load the data...")
    # get both pages
    page_1 = soup_it(base_url.format(1))
    page_2 = soup_it(base_url.format(2))
    # get the data from both pages
    books_list_1 = books_data(page_1)
    books_list_2 = books_data(page_2)

    most_popular_books1 = get_most_popular_books(books_list_1)
    most_popular_books2 = get_most_popular_books(books_list_2)

    # get the 10 most expensive books among the most popular books from both pages
    most_expensive_books = get_10_most_expensive_books(
        most_popular_books1 + most_popular_books2
    )
    print(
        "\nScrapping completed in {} seconds".format(
            (time.time() - start_time).__round__(2)
        )
    )
    print("The 10 most expensive books among the most popular are:")
    books = []
    for book in most_expensive_books:
        books.append(
            "{}   -Price: {} -Reviews: {}".format(
                book["title"], book["price"], book["stars"]
            )
        )
    print("\n".join(books))
    print("\n")


if __name__ == "__main__":
    main()
