from django.contrib import admin
from .models import Category,Product,Order
# Register your models here.
class AdminCategory(admin.ModelAdmin):
    list_display = ('name','date_added')

class AdminProduct(admin.ModelAdmin):
    list_display = ('title','price','pourcatange','pricenet','category','date_added')

class AdminOrder(admin.ModelAdmin):
    list_display = ('product','name','lastname','email','phone','city','description','date_added')    
admin.site.register(Product,AdminProduct)
admin.site.register(Category,AdminCategory)
admin.site.register(Order,AdminOrder)