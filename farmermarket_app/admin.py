from django.contrib import admin

from .models import (Category, Vendor,
                     Blog, Product, Advertisement, About, Order, OrderItem, Customer, Contact, userDetail,CoverImage)


admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(Vendor)
admin.site.register(Product)
admin.site.register(Blog)
admin.site.register(Advertisement)
admin.site.register(About)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Contact)
admin.site.register(userDetail)
admin.site.register(CoverImage)
# admin.site.register(OrderItem)
# admin.site.register(Order)
