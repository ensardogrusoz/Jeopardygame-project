from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from triviasearch.forms import CategoryForm
import requests
import re
# Create your views here.

RE_TAGS = re.compile(r'<[^>]+>')

def category(request):
    content_list = []
 
    for offset in range(0,10000): 
            
        api_req = 'http://jservice.io/api/categories?count=100&offset=' + str(offset)
        
        r = requests.get(api_req)
        category_set = r.json()
        for category in category_set:          
            dict = { 'title': category['title'], 'id': category['id'] }            
            content_list.append(dict)
  
        return render(request, 'trivia/home.html', {'categories': content_list})
        


def random(request):
    api_req = 'http://jservice.io/api/random'
    r = requests.get(api_req)
    trivia_set = r.json()
    content_list = []
    for trivia in trivia_set:
        dict = { 'id': trivia['id'], 'question' : trivia['question'], 'answer' : RE_TAGS.sub('', trivia['answer']), 'category' : trivia['category']['title'] }
        content_list.append(dict)
    return render(request, 'trivia/random.html', {'trivia' : content_list})
