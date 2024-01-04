from django.contrib import admin

from cars.models import Car

# Register your models here

# django 1.x to 2.x syntax

# no customization syntax(simple syntax)
# admin.site.register(Car)

#customization syntax
# class CarAdmin(admin.ModelAdmin):
#     # fields = ["year", "brand"] #to order the fields
#     #to order the field sets
#     fieldsets = [
#         ("Date Information", {
#             "fields": ["year"]
#         }),
#         ("Car Information", {
#             "fields": ["brand"]
#         })
#     ]

# admin.site.register(Car, CarAdmin)

#django 2.x or later syntax(but any syntax is fine)
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    # write pass here if don't want want any customizations
    # fields = ["year", "brand"] #to order the fields
    #to order the field sets
    fieldsets = [
        ("Date Information", {
            "fields": ["year"]
        }),
        ("Car Information", {
            "fields": ["brand"]
        })
    ]