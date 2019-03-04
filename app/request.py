import urllib.request,json
from .models import Quote
from app import app
# Getting api key
# api_key = None
# Getting the movie base url
base_url = None
base_url = app.config['BLOG_API_BASE_URL']

def configure_request(app):
    global base_url
    

def get_quotes():

    get_movies_url = base_url
  
    print(base_url)

    with urllib.request.urlopen(base_url) as url:
        get_quotes_data = url.read()
        get_quotes_response = json.loads(get_quotes_data)

        quote_object = None

        if get_quotes_response:
            id=get_quotes_response.get('id')
            author=get_quotes_response.get('author')
            quote=get_quotes_response.get('quote')
            quote_object = Quote(id,author,quote)

    return quote_object