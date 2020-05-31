from django.contrib import admin
# from .models import Team 
# from .models import Player
# from .models import Matches
from django.apps import apps
models = apps.get_models()

for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass

