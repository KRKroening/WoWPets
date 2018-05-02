from .models import PetsToCollect
import requests
from bs4 import BeautifulSoup as bs
import urllib3 as urllib
import pdb

def UpdateNeededPets():
    # Get character specific pets
    urlCollected = "https://us.api.battle.net/wow/character/doomhammer/Ziast?fields=pets&locale=en_US&apikey=zpbbcws848zkzqb3gqv5rjy2npwf2qb9"
    responseCollected = requests.get(urlCollected).json()
    responseCollected = responseCollected["pets"]["collected"]

    urlAll = "https://us.api.battle.net/wow/pet/?locale=en_US&apikey=zpbbcws848zkzqb3gqv5rjy2npwf2qb9"
    responseAll = requests.get(urlAll).json()
    responseAll = responseAll["pets"]

    notCollected = []

    for i in responseAll:  # refactor
        found = False
        for t in responseCollected:
            if i["creatureId"] == t["creatureId"]:
                found = True
                break
        if not found:
            notCollected.append(i)

    for pet in notCollected:
        # pdb.set_trace()
        p, r = PetsToCollect.objects.get_or_create(creatureId=pet["creatureId"],
                                                creatureName=pet["name"],
                                                source="unknown",
                                                zone="unknown",
                                                investmentType="unknown",
                                                investmentValue="0",
                                                )
        p.save()
        # TODO:
        #     Create func to scrape wowhead or warcraft pets to get the data I need.
        #     I don't think there is an API available for this.

def scrapeWPForData(creatureId):
    url = "https://www.warcraftpets.com/?npc=" + str(creatureId)
    page = urllib.PoolManager().request('GET', url).data
    soup = bs(page, 'html.parser')
    target = soup.find("div", {"class": "wowtooltip"})
    pdb.set_trace()

    spans = target.findAll("span")
    investmentType = spans[0].text.strip()
    pdb.set_trace()

    links = target.findAll("a")
    source, zone, investmentValue = links[0].text.strip() , links[1].text.strip() , links[2].text.strip()
    pdb.set_trace()

    pet = PetsToCollect.objects.get(creatureId=creatureId)
    pet.source, pet.zone, pet.investmentType, pet.investmentValue = source, zone, investmentType, investmentValue
    pdb.set_trace()

    pet.save()


def GetPets():
    return PetsToCollect.objects.all().order_by('creatureName')

def GetPet(id):
    pet = PetsToCollect.objects.get(creatureId=id)
    return pet

def ClearNeededPets():
    pets = PetsToCollect.objects.all()
    for pet in pets:
        pet.delete()

def RemoveFromDB(id):
    pet = PetsToCollect.objects.get(creatureId=id)
    pet.delete()
