from django.contrib import admin
from myapp.models import Contact
from myapp.models import Donate

# Register your models here.

admin.site.register(Contact)
admin.site.register(Donate)
