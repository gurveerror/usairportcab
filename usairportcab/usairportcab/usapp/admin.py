from django.contrib import admin
from .models import Car, Car_fare, Common_detail, Site, Sites_common_detail

# Register your models here.
class CarAdmin(admin.ModelAdmin):
    list_display = ['car_name', 'pax', 'large_luggage' ,'status']
admin.site.register(Car, CarAdmin)

class CarfareAdmin(admin.ModelAdmin):
    list_display = ['car_name', 'min_fare', 'site_name']
    list_filter = ['car_name', 'site_name', 'min_fare']
    list_editable = ['car_name', 'site_name']
    #prepopulated_fields = {'car_name': ('min_fare',)}
admin.site.register(Car_fare, CarfareAdmin)

class CommondetailAdmin(admin.ModelAdmin):
    list_display = ['update_data']
admin.site.register(Common_detail, CommondetailAdmin)

class SiteAdmin(admin.ModelAdmin):
    list_display = ['companyname', 'telno', 'email', 'website']
    list_filter = ['companyname', 'telno', 'email', 'website']
    list_editable = ['companyname', 'website']
    prepopulated_fields = {'companyname': ('website',)}
admin.site.register(Site, SiteAdmin)

class SitescommondetailAdmin(admin.ModelAdmin):
    list_display = ['company_name','update_data']
admin.site.register(Sites_common_detail, SitescommondetailAdmin)