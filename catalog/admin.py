from django.contrib import admin

# Register your models here.
from .models import Genre, Good, Saler, Customer, Transaction

admin.site.register(Genre)
admin.site.register(Good)
admin.site.register(Saler)
admin.site.register(Customer)
admin.site.register(Transaction)
