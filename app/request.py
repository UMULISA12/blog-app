import urllib.request,json
from .models import Quote
# Getting api key
# api_key = None
# Getting the movie base url
base_url = None

def configure_request(app):
    global base_url
    # api_key = app.config['MOVIE_API_KEY']
    base_url = app.config['MOVIE_API_BASE_URL']

def get_quotes(category):
    '''
    Function that gets the json response to our url request
    '''
    print(base_url)

    with urllib.request.urlopen(get_movies_url) as url:
        get_movies_data = url.read()
        get_movies_response = json.loads(get_movies_data)

        quote_object = None

        if get_movies_response:
            id=get_quote_response.get('id')
            id=get_quote_response.get('author')
            id=get_quote_response.get('quote')
            quote_object = Quote(id,author,quote)
    return quote_object