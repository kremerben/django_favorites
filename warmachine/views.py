from django.shortcuts import render, render_to_response, redirect
from django.forms import ModelForm

from models import *
from forms import *
# Create your views here.

def home(request):
    return render_to_response("home.html")

def wars(request):
    wars = War.objects.all()
    return render_to_response("wars/wars.html", {'wars': wars})

def battles(request):
    battles = Battle.objects.all()
    return render_to_response("battles/battles.html", {'battles': battles})

def countries(request):
    countries = Country.objects.all()
    return render_to_response("countries/countries.html", {'countries': countries})

def militaries(request):
    militaries = Military.objects.all()
    return render_to_response("militaries/militaries.html", {'militaries': militaries})

def commanders(request):
    commanders = Commander.objects.all()
    return render_to_response("commanders/commanders.html", {'commanders': commanders})


def new_commander(request):
    if request.method == "POST":
        form = CommanderForm(request.POST)
        if form.is_valid():
            if form.save():
                return redirect("/commanders")
    else:
        form = MilitaryForm()
    data = {'form': form}
    return render(request, "commanders/add_commander.html", data)


def view_commander(request, commander_id):
    commander = Country.objects.get(id=commander_id)
    data = {"commander": commander}
    return render(request, "commanders/view_commander.html", data)


def new_military(request):
    if request.method == "POST":
        form = MilitaryForm(request.POST)
        if form.is_valid():
            if form.save():
                return redirect("/militaries")
    else:
        form = MilitaryForm()
    data = {'form': form}
    return render(request, "militaries/add_military.html", data)


def view_military(request, military_id):
    military = Country.objects.get(id=military_id)
    data = {"military": military}
    return render(request, "militaries/view_military.html", data)


def new_country(request):
    if request.method == "POST":
        form = CountryForm(request.POST)
        if form.is_valid():
            if form.save():
                return redirect("/countries")
    else:
        form = CountryForm()
    data = {'form': form}
    return render(request, "countries/add_country.html", data)


def view_country(request, country_id):
    country = Country.objects.get(id=country_id)
    data = {"country": country}
    return render(request, "countries/view_country.html", data)


def new_battle(request):
    if request.method == "POST":
        form = BattleForm(request.POST)
        if form.is_valid():
            if form.save():
                return redirect("/battles")
    else:
        form = BattleForm()
    data = {'form': form}
    return render(request, "battles/add_battle.html", data)


def view_battle(request, battle_id):
    battle = Battle.objects.get(id=battle_id)
    data = {"battle": battle}
    return render(request, "battles/view_battle.html", data)


def new_war(request):
    if request.method == "POST":
        form = WarForm(request.POST)
        if form.is_valid():
            if form.save():
                return redirect("/wars")
    else:
        form = WarForm()
    data = {'form': form}
    return render(request, "wars/add_war.html", data)


def view_war(request, war_id):
    war = War.objects.get(id=war_id)
    data = {"war": war}
    return render(request, "wars/view_war.html", data)

