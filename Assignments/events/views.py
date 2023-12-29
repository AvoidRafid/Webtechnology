from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .models import Event


def all_events(request):
    event_list = Event.objects.all()
    return render(request, 'events/event_list.html',
    {
        'event_list' : event_list

    })


def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    name = "Nabil"
    month = month.capitalize()
    
    # converting month to num
    month_num = list(calendar.month_name).index(month)
    month_num = int(month_num)

    # creating calendar
    cal = HTMLCalendar().formatmonth(year, month_num)

    # get current year
    now = datetime.now()
    current_year = now.year
    time = now.strftime('%I:%M %p')

    return render(request, 
                  'events\home.html', 
                  {
                    "name" : name,
                    "year": year,
                    "month": month,
                    "cal": cal,
                    "current_year": current_year,
                    "time":time,
                   }
                   )
