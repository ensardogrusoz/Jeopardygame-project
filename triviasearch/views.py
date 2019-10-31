from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from triviasearch.forms import CategoryForm
from django.template import RequestContext
import random as ran
import requests
import re
import datetime

# Create your views here.

TAG_RE = re.compile(r'<[^>]+>')

# def category(request):
#     offset=0
#     content_list = []
#     for offset in range(0,184,100):
                   
        
#         api_req = 'http://jservice.io/api/categories?count=100&offset=' + str(offset)       
#         r = requests.get(api_req)
#         category_set = r.json()
        
#         for category in category_set:          
#             dict = { 'title': category['title'], 'id': category['id'] }            
#             content_list.append(dict)

#     return render(request, 'trivia/home.html', {'categories': content_list})



def search(request):
    # Search Box
    form = CategoryForm(request.POST)
    if request.method == 'POST':
        
        if form.is_valid():
            data = form.cleaned_data

            cat = data['category'] if data['category']!= "" else None
            diff = data['difficulty'] if data['difficulty']!= "" else None
            from_date = data['from_date'] if data['from_date'] != None else datetime.date(1966, 1, 1)
            to_date = data['to_date'] if data['to_date'] != None else datetime.date(2011, 12, 12)

            return search_results(request, cat, diff, (from_date, to_date))
    # 
    # content = []
    # offset = ran.randint(0, 2000)
    # req = "http://jservice.io/api/categories?count=100" + "&offset=" + str(offset)
    # response = requests.get(req)
    # category_set = response.json()
    # for category in category_set:
    #     dict = {'title': category['title'], 'id': category['id']}
    #     content.append(dict)

    return render(request, 'trivia/home.html', { 'form': form, 'titleBar' : "Search"})

def search_results(request, cat, diff, date):
    content_set = []
    clues_set = []
    success = False

    offset = 0
    categories = []
    while True:
        api_req = "http://jservice.io/api/categories?count=100&offset=" + str(offset)
        response = requests.get(api_req)
        category_set = response.json()
        # amount of categories
        if offset >= 10000:
            break
        # find right Categories
        for category in category_set:
            categories.append(category['title'])
            if category['title'] == None:
                break
            
            # Add all the questions/clues from that category and append to larger list
            elif (cat == None) or (cat != "" and cat in category['title']):
                clue_req = "http://jservice.io/api/clues?category=" + str(category['id'])
                clue_question = requests.get(clue_req)
                clue_question_set = clue_question.json()

                # Loop through all the questions in one category
                for clue in clue_question_set:
                    value = clue['value'] # sees difficulty of the question
                    airdate = datetime.date(int(clue['airdate'][:4]), int(clue['airdate'][5:7]), int(clue['airdate'][8:10]))

                    if value == None:
                        continue

                    # Max difficulty value == 1000
                    dict = {'easy': 0 < value <= 400,
                            'medium': 400 < value <= 700,
                            'hard': 700 < value <= 1000,
                            None : True}
                    difficulty = dict[diff]

                    # filter date here
                    timeframe = date[0] <= airdate <= date[1]

                    if difficulty and timeframe:
                        clues_set.append(clue)

        offset += 100

    if len(clues_set) != 0:
        success = True

    # f = open("all_categories.txt", "w")
    # f.write(str(categories))

    for clue in clues_set:
        dict = {'id': clue['id'], 'question':clue['question'], 'answer':clue['answer'], 'category':clue['category']['title'], 'airdate':clue['airdate'][:10], 'value':clue['value'], 'category_id':clue['category_id']}
        content_set.append(dict)

    return render(request,'trivia/listcategory_results.html', {'trivia':content_set, 'title':cat, 'success':success, 'titleBar':cat})



def random(request):
    api_req = 'http://jservice.io/api/random'
    r = requests.get(api_req)
    trivia_set = r.json()
    content_list = []
    for trivia in trivia_set:
        dict = { 'id': trivia['id'], 'question' : trivia['question'], 'answer' : TAG_RE.sub('', trivia['answer']), 'category' : trivia['category']['title'] }
        content_list.append(dict)
    return render(request, 'trivia/random.html', {'trivia' : content_list})



def category_results(request, id='1'):
    req = 'http://jservice.io/api/category?id='+id
    response = requests.get(req)
    category_set = response.json()
    clues_set = category_set['clues']
    content = []
    for clues in clues_set:
        dict = {'answer':clues['answer'], 'question':clues['question']}
        content.append(dict)
    return render(request, 'trivia/listcategory_results.html', {'clues':content})

