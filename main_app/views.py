from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Hello FinchCollector</h1>')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    return render(request, 'finches/index.html', {'finches': finches})

class Finch:
    def __init__(self, name, species, description, age):
        self.name = name
        self.species = species
        self.description = description
        self.age = age

finches = [
    Finch('Script', 'Java', 'First pet bird to conquer Asia', 2),
    Finch('Rainbow', 'Gouldian', 'Endangered in its native habitat of Northern Australia', 3),
    Finch('Owl', 'Double-barred', 'A popular species that goes by several other names, the Owl finch, Clown Finch and Bicheno’s finch', 4)
]