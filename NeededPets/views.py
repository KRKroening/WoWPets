import pdb

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from .logic import *

# Create your views here.

def index(request):
    template_name = loader.get_template('petFinder/index.html')

    context = { 'needed_pets' : GetPets() }
    # pdb.set_trace()
    return HttpResponse(template_name.render(context, request))

def individualPage(request, creatureId):
    template_name = loader.get_template('petFinder/indvPage.html')
    scrapeWPForData(creatureId)
    # TODO:
    #     Redir to new page. Get Info from Wowhead to display Picture, loc, drop, ect.
    # TODO:
    #  Filters to screen types
    context = { 'pet' : GetPet(creatureId) }

    return HttpResponse(template_name.render(context, request))


def UpdateNeededCollection(request):
    ClearNeededPets()
    UpdateNeededPets()

    # pdb.set_trace()
    return HttpResponseRedirect(reverse('index'))

def RemoveFromCollection(request, creatureId):
    RemoveFromDB(creatureId)
    return HttpResponseRedirect(reverse('index'))
