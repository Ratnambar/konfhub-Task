from django.urls import path
from konfhub_Task.views import all_list


urlpatterns = [
    path('', all_list, name='allList'),
]
