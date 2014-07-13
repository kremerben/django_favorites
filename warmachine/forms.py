from django.forms import ModelForm
from models import *



class WarForm(ModelForm):
    class Meta:
        model = War

class BattleForm(ModelForm):
    class Meta:
        model = Battle

class CountryForm(ModelForm):
    class Meta:
        model = Country

class MilitaryForm(ModelForm):
    class Meta:
        model = Military

class CommanderForm(ModelForm):
    class Meta:
        model = Commander
