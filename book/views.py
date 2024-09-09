from django.shortcuts import render
import bs4
import requests

# Create your views here.
def index(request):
    return render(request, 'index.html')

def word(request):
    word = request.GET['word']

    wordpage = requests.get('https://www.dictionary.com/browse/'+word)
    

    if wordpage:
        soup = bs4.BeautifulSoup(wordpage.text, 'lxml')

        meaning = soup.find_all('div', {'class':'NZKOFkdkcvYgD3lqOIJw'})
        meaning1 = meaning[0].getText()
        
    else:
        word = 'Sorry, '+ word + ' Is Not Found In Our Database'
        meaning = ''
        meaning1 = ''


    results = {
        'word' : word,
        'meaning' : meaning1,
    }

    return render(request, 'word.html', results)