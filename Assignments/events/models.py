from django.db import models

class Venue(models.Model):
    name = models.CharField('Value Name', max_length=120)
    address = models.CharField(max_length=300)
    zip_code = models.CharField('Zip Code', max_length=13)
    phone = models.CharField('Contact Phone', max_length=15)
    web = models.URLField('Website Address')
    email_address = models.EmailField('Email Address')

    def __str__(self):
        return self.name


class MyUsers(models.Model):
    first_name = models.CharField('First Name', max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField('User Email')

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Event(models.Model):
    name = models.CharField('Event Name', max_length=120)
    event_date = models.DateTimeField('Event Date', max_length=120)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE, blank=True, null=True)                   # adding Venue class to as foreign key so that we get all the info of that class
    manager = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    attendees = models.ManyToManyField(MyUsers, blank=True)

    def __str__(self):
        return self.name