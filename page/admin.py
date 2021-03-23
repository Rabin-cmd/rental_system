from django.contrib import admin
from .models import Rental
# Register your models here.



class RentalAdmin(admin.ModelAdmin):
    list_display=('name','price','dt')
    search_fields=('name',)
    list_filter=('price','type')

admin.site.register(Rental,RentalAdmin)

admin.site.site_header = 'Rental System Admin'