from django.contrib import admin

from .models import *

# Register your models here.


admin.site.register(animal)
admin.site.register(breed_cat)
admin.site.register(breed_dog)
admin.site.register(service)
admin.site.register(application)
class applicationAdmin(admin.ModelAdmin):
    class Media:
        from django.conf import settings
        static = getattr(settings, 'STATIC_URL', '/static')
        js = [
            static+'/admin/js/formset_handlers.js', 
            'https://code.jquery.com/jquery-3.5.1.min.js',
            'vetsapp/js/main.js',
            'static/js/main.js',
            '/static/js/main.js'
            ]

    change_form_template = 'admin.html'
