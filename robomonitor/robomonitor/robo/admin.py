from django.contrib import admin
from .models import AppUser, Profile, Websites, Logs


# Register your models here.

@admin.register(AppUser)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(Websites)
class WebsitesAdmin(admin.ModelAdmin):
    pass


@admin.register(Logs)
class WebsitesAdmin(admin.ModelAdmin):
    pass
