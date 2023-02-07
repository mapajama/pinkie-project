from django.contrib import admin
from .models import Client
from .models import Underwriter
from .models import Cobroker

admin.site.register(Client)
admin.site.register(Underwriter)
admin.site.register(Cobroker)
# Register your models here.
