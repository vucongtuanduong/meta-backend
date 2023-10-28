from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.


# def home(request):
#     content = "<html><body><h1>Welcome to my website</h1></body></html>"
#     return HttpResponse(content)

# def homepage(request):
#     return HttpResponse("This is the homepage")
# def display_date(request):
#     date_joined = datetime.today().year
#     return HttpResponse(date_joined)
# def menu(request):
#     text = "<h1>Menu</h1><ul><li>Appetizers</li><li>Entrees</li><li>Desserts</li></ul>"
#     return HttpResponse(text)

# def new_home(request):
#     path = request.path
#     response = HttpResponse("This works !")
#     # return HttpResponse(path, content_type = 'text/html', charset = 'utf-8')
#     return response

def menuitems(request, dish):
    items = {
        'appetizers': ['salad', 'wings', 'fries'],
        'entrees': ['steak', 'salmon', 'tofu'],
        'desserts': ['ice cream', 'cake', 'pie']
    }
    description = items[dish][0]
    return HttpResponse(f"<h2> {dish} </h2>" + description)
