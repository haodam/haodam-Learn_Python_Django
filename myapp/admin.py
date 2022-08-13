from operator import imod
from django.contrib import admin
from.models import BaiBao, Publication, Python2104 , Place, Restaurant, Reporter, Article
class ReporterAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email']

# Register your models here.
admin.site.register(Python2104)
admin.site.register(Place)
admin.site.register(Restaurant)
admin.site.register(Reporter, ReporterAdmin)
admin.site.register(Article)
admin.site.register(Publication)
admin.site.register(BaiBao)