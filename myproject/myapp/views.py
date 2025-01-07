from django.shortcuts import render
from django.http import HttpResponse

#from myapp.forms import BookingForm

# Create your views here.
'''def form_view(request): 
  form = BookingForm() 
  context = {'form': form} 
  return render(request, 'booking.html', context)


def home(request):
  response = HttpResponse("Welcome to Little Lemon!")
  return response

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