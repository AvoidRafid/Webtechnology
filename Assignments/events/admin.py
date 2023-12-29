from django.contrib import admin
from .models import Venue
from .models import MyUsers
from .models import Event


admin.site.register(Venue)
admin.site.register(MyUsers)
admin.site.register(Event)