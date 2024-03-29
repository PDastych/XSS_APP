from django.urls import path
from .views import *


urlpatterns = [
    path('dom_based_xss', dom_based_xss_view, name='dom_based_xss'),
    path('dom_based_xss/introduction', dom_based_xss_introduction, name='dom_based_xss_introduction'),
    path('dom_based_xss/level1', dom_based_xss_level1, name='dom_based_xss_level1'),
    path('dom_based_xss/level1/create', level1_create_text, name='dom_based_xss_level1_create'),
    path('dom_based_xss/level1/delete/<int:id>', level1_delete_text, name='dom_based_xss_level1_delete')
]