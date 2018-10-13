import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'simple_search.settings')

django.setup()

from django_seed import Seed

from developersearch.models import Developer, ProgrammingLanguage, Language
import random

seeder = Seed.seeder()
seeder.add_entity(Developer, 100)
seeder.execute()

developers = Developer.objects.all()
programming_languages = ProgrammingLanguage.objects.all()
languages = Language.objects.all()
for dev in developers:
    for language in languages:
        if (language.id % 2 == random.randint(0,1) and dev.id % 2 == random.randint(0,1)) or (language.id % 2 != random.randint(0,1) and dev.id % 2 != random.randint(0,1)):
            continue
        dev.languages.add(language)
    for programming_language in programming_languages:
        if (programming_language.id % 2 == random.randint(0,1) and dev.id % 2 == random.randint(0,1)) or (programming_language.id % 2 != random.randint(0,1) and dev.id % 2 != random.randint(0,1)):
            continue
        dev.programming_languages.add(programming_language)
