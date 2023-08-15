import requests

#r = requests.get("https://newsapi.org/v2/everything?qInTitle=stock%20market&from=2023-8-5&to=2023-8-28&sortBy=popularity&language=en&apiKey=890603a55bfa47048e4490069ebee18c")
#content = r.json()

#articles = content["articles"]


#for article in articles:
#  print('AUTHOR\n:',article["author"], '\nTITLE\n:',article["title"])

def news(topic, from_date, to_date, language='en',api_Key='6a2297b099574b1b9ed2bc269aa1d0d1'):

  url = f'https://newsapi.org/v2/everything?qInTitle={topic}&from={from_date}&to={to_date}&sortBy=popularity&language={language}&apiKey={api_Key}'
  r = requests.get(url)
  content = r.json()
  articles = content["articles"]
  results = []
  for article in articles:
    results.append(f"TITLE\n'{article['title']}, '\nTITLE\n',{article['description']}")
  return results  
  
print(news(topic="news",from_date="2023-8-2",to_date="2023-8-18",language="en",api_Key="6a2297b099574b1b9ed2bc269aa1d0d1"))
  
  




  