from django.contrib import admin

# Register your models here.
from .models import Wordlist, WordlistType, Family, Format


class WordlistAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ['name', 'type', 'family', 'effectiveness_rating',
                    'size_rating', 'wordcount', 'date_origin']


admin.site.register(Family)
admin.site.register(Format)
admin.site.register(Wordlist, WordlistAdmin)
admin.site.register(WordlistType)
