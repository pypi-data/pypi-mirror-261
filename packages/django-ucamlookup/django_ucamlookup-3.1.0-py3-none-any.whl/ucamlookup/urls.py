from django.urls import re_path
from ucamlookup.views import find_people, find_groups


urlpatterns = [
    re_path(r'findPeople$', find_people, name='ucamlookup_find_people'),
    re_path(r'findGroups$', find_groups, name='ucamlookup_find_groups'),
]
