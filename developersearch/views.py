from django.shortcuts import render
from django.http import HttpResponse
from .models import Developer, Language, ProgrammingLanguage


# Create your views here.


def index(request):
    try:
        language_search = request.GET['srchlang'];
        if (language_search == ''):
            raise Exception('no filter added')

        language_search = formatRequst(language_search);
        languages = Language.objects.filter(code__in=language_search)
    except:
        languages = Language.objects.all()
    try:
        programming_language_search = request.GET['srchproglang'];
        if (programming_language_search == ''):
            raise Exception('no filter added')

        programming_language_search = formatRequst(programming_language_search);
        programming_languages = ProgrammingLanguage.objects.filter(name__in=programming_language_search)

    except:
        programming_languages = ProgrammingLanguage.objects.all()

    developer_list = Developer.objects.filter(languages__in=languages,
                                               programming_languages__in=programming_languages).distinct()

    context = {'developer_list': developer_list}
    # return  HttpResponse(developer_list)
    return render(request, 'developersearch/index.html', context)


# def filterDev(request):
#     developer_list = Developers.objects.filter(languages=['3','2'])
#     context = {'developer_list': developer_list}
#     return  HttpResponse(developer_list,)
# return render(request, 'developersearch/index.html', context)

def formatRequst(value):
    value = value.replace(',', ' ')
    return value.split(' ')

def filterLnaguage(request):
    language_list = Language.objects.filter(developer=None)
    print(language_list)
    context = {'language_list': language_list}
    return render(request, 'developersearch/language.html', context)

