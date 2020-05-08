"""
youtube video: https://www.youtube.com/watch?v=tb8gHvYlCFs&list=RDtb8gHvYlCFs&start_radio=1&t=0

Python Requests Tutorial: Request Web Pages, Download Images, POST Data, Read JSON, and More


Corey Schafer:

In this Python Programming Tutorial, we will be learning how to use the Requests library. The Requests library allows us
 to send HTTP requests and interact with web pages. We will be learning how to grab the source code of a site, download
 images, POST form data to routes, read JSON responses, perform authentication, and more. Let's get started...
"""
from pprint import pprint as pp
import requests


# primeira_parte
# conhecendo a biblioteca

# r = requests.get('https://xkcd.com/353/')
# print(r)
# print(dir(r))
# help(r)
# print('')
# r2 = requests.get('https://imgs.xkcd.com/comics/python.png')
# pp(r2.status_code)
# print(r2.ok)
# print(r2.content)
# pp(r2.headers)
# print('')
# with open('comic.png', 'wb') as f:
#     f.write(r.content)


payload = {'page': 2, 'count': 25}
r = requests.get('https://httpbin.org/json')
help(requests.post)
print(r.json())

