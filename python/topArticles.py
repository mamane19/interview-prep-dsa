# Query a REST API to get a list of articles. Given an integer, limit, return the top limit  article names 
# ordered decreasing by comment count, then decreasing alphabetically for those that have the same comment counts.
# To access the collection of comments, make an HTTP GET request to: https://jsonmock.hackerrank.com/api/articles?page=<pageNumber>
# where <pageNumber> is an integer where 1 <= pageNumber <= total_pages. total_pages  is one of the fields in the JSON data.

# The response is a JSON object with the following 5 fields:
# page: the current page number
# per_page: the number of articles per page
# total: the total number of articles
# total_pages: the total number of pages
# data: an array of article objects with the following fields:
# title: the article title, may be null
# url: the article URL, may be null
# author: the article author, may be null
# num_comments: the number of comments for the article
# story_id: the story id of the article
# story_title: the story title of the article
# story_url: the story URL of the article
# parent_id: the parent story id of the article
# created_at: the date and time when the article was created


# first get the article name.
# if the title in the field is not null, use that.
# otherwise, if the story_title is not null use that.
# if both are null, ignore the article.

# Sort the titles decreasing by comment count, then decreasing alphabetically by article name if there is a tie in comments count. 
# Return a list of the top limit article names.


import requests


def get_top_articles(limit):
         # your code here
     url = 'https://jsonmock.hackerrank.com/api/articles'
     page = 1
     top_articles = []
     while page <= limit:
          response = requests.get(url + '?page=' + str(page))
          if response.status_code == 200:
               data = response.json()
               for article in data['data']:
                    title = article['title']
                    story_title = article['story_title']
                    if title is not None:
                         top_articles.append(title)
                    elif story_title is not None:
                         top_articles.append(story_title)
          else:
               break
          page += 1
     # let's sort the list based on the number of comments and not exceed the limit.
     top_articles.sort(key=lambda x: (len(x), x), reverse=True)
     return top_articles[:limit]



















# if limit < 1:
#         raise ValueError("limit must be greater than 0")

#     url = "https://jsonmock.hackerrank.com/api/articles?page=1"
#     response = requests.get(url)
#     data = response.json()
#     total_pages = data["total_pages"]
#     page_num = 1
#     articles = []
#     while page_num <= total_pages:
#         for article in data["data"]:
#             if article["title"] is not None:
#                 articles.append(article["title"])
#             elif article["story_title"] is not None:
#                 articles.append(article["story_title"])
#         url = "https://jsonmock.hackerrank.com/api/articles?page=" + str(page_num)
#         response = requests.get(url)
#         data = response.json()
#         page_num += 1
#     return sorted(articles, key=lambda x: (-len(x), x))[:limit]
