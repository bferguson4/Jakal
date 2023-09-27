from django.contrib import admin
from .models import Player, Sponsor, Character, Franchise, Country

# Register your models here.
@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    pass

@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    pass

@admin.register(Sponsor)
class TeamAdmin(admin.ModelAdmin):
    pass

@admin.register(Franchise)
class FranchiseAdmin(admin.ModelAdmin):
    pass


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    pass


