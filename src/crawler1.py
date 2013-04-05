"""
"   Here I implemented the basic url extraction, and also I could extract all urls out from page.
"""

page = 'this is a page of link. <a href="http://www.google.com">Google</a>, and this is the second <a href="http://www.dumingzhe.com">page</a>'
url_list = []


def extractURL(page):
    start_quote = page.find('<a href=')
    if start_quote == -1:
        return 'None', -1
    else:
        start_index = page.find('"', start_quote)
        end_index = page.find('"', start_index + 1)
        url = page[start_index + 1 : end_index]
        return url, end_index

def extractAllURL(page):
    end = 0
    while end != -1:
        url, end = extractURL(page)
        if url != 'None':
            url_list.append(url)
        page = page[end:]
        

extractAllURL(page)
print url_list

