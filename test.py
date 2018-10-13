import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'simple_search.settings')
django.setup()

from developersearch.models import Developers, ProgrammingLanguages, Languages

developers = Developers.objects.all()
programming_languages = ProgrammingLanguages.objects.all()
languages = Languages.objects.all()

developer_list = Developers.objects.filter(languages=1)
print(developer_list)
