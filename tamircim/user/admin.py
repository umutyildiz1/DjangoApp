from django.contrib import admin

# Register your models here.

from .models import ariza,tamirci,map,message,extendedUsers,usermap,ariza1

admin.site.register(ariza)
admin.site.register(tamirci)
admin.site.register(map)
admin.site.register(message)
admin.site.register(extendedUsers)
admin.site.register(usermap)
admin.site.register(ariza1)