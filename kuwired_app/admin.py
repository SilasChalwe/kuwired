# dashboard/admin.py
from django.contrib import admin
from .models import ProductItem,testimonial,TeamMember,FAQ,ContactMessage
from .models import Client_Item,CallToAction,HeroSection,Service,Category,AboutUs

#class Client_Item_admin(admin.ModelAdmin):
   # list_display = ['id','name','image']

        

admin.site.register(ProductItem)
admin.site.register(testimonial)
admin.site.register(FAQ)
admin.site.register(TeamMember)
admin.site.register(Client_Item)
admin.site.register(ContactMessage)
admin.site.register(CallToAction)
admin.site.register(HeroSection)
admin.site.register(Service)
admin.site.register(Category)
admin.site.register(AboutUs)
