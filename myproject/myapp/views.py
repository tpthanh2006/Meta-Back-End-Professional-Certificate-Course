from django.shortcuts import render
from django.http import HttpResponse
from .models import Menu
#from myapp.forms import BookingForm

# Create your views here.
def home(request):
  return render(request, 'home.html')

def menu(request):
  menu_items = Menu.objects.all()
  items_dict = {"menu": menu_items}
  return render(request, 'menu.html', items_dict)

def about(request):
  about_content = {'about': [
          {'name': "Little William"},
          {'name': "Little Melo"},
  ]}
  return render(request, "about.html", about_content)


'''def form_view(request): 
  form = BookingForm() 
  context = {'form': form} 
  return render(request, 'booking.html', context)

def about(request):
  return HttpResponse("About us")

def menu(request):
  return HttpResponse("Menu")

def book(request):
  return HttpResponse("Make a booking")

def drinks(request, drink_name):
  drink = {
    'mocha': 'type of coffe',
    'tea': 'type of beverage',
    'lemonade': 'type of refreshment',
  }
  choice_of_drink = drink[drink_name]
  return HttpResponse(f"<h2> {drink_name} </h2>" + choice_of_drink)
'''