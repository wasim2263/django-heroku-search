from django.contrib import admin

# Register your models here.
from .models import Developer, Interview, Language, ProgrammingLanguage


class DeveloperAdmin(admin.ModelAdmin):
    list_display = (['email'])
    search_fields = (['email'])



class DeveloperInterviewAdmin(admin.ModelAdmin):
    list_display = (['developer', 'score', 'comment'])
    search_fields = (['developer__email'])

admin.site.register(Developer, DeveloperAdmin)
admin.site.register(Interview, DeveloperInterviewAdmin)
admin.site.register(Language)
admin.site.register(ProgrammingLanguage)
