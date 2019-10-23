from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

import requests
import re
# Create your views here.

RE_TAGS = re.compile(r'<[^>]+>')

def random(request):
    api_req = 'http://jservice.io/api/random?'
    r = requests.get(api_req)
    trivia_set = r.json()
    content_list = []
    for trivia in trivia_set:
        dict = { 'id': trivia['id'], 'question' : trivia['question'], 'answer' : RE_TAGS.sub('', trivia['answer']), 'category' : trivia['category']['title'] }
        content_list.append(dict)
    return render(request, 'trivia/random.html', {'trivia' : content_list})
