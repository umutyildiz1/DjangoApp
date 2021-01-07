from django.contrib import admin

# Register your models here.

from .models import ariza,tamirci,map,message,extendedUsers

admin.site.register(ariza)
admin.site.register(tamirci)
admin.site.register(map)
admin.site.register(message)
admin.site.register(extendedUsers)