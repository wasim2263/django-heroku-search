from django.urls import path

from . import views

app_name = 'developersearch'

urlpatterns = [
    # ex: /
    path('', views.index, name='index'),
    path('unused-languages', views.filterLnaguage, name='unused.languages'),

]