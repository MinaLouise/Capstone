from django.contrib import admin
from . import models

# Register your models here.

class NatalieAdminArea(admin.AdminSite):
    site_header = 'Natalie Admin Area'

Natalie_site = NatalieAdminArea(name = 'AdminArea')

# Natalie_site.register(models.(model))