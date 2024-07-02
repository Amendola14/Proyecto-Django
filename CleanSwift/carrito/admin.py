from django.contrib import admin
from django.utils.module_loading import autodiscover_modules
from django.contrib.admin import site


def autodiscover_admin():
    autodiscover_modules('admin', register_to=site)


