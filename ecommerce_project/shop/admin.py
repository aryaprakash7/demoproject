from django.contrib import admin

# Register your models here.
##creating admin panel using class for a detailed view
from .models import Category,Product
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':['name',]}
admin.site.register(Category,CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','stock','available','created','updated','image']
    list_editable = ['price','stock','available']
    prepopulated_fields = {'slug':['name',]} ##automatically fills field
    list_per_page = 20
admin.site.register(Product,ProductAdmin)

