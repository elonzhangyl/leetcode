from requests_html import HTMLSession
session = HTMLSession()
url = 'https://www.quantquestions.com/firm-rankings/'
r = session.get(url)
print('123')
