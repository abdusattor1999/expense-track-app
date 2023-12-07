from django.urls import path, include
from .views import pr_list

app_name = 'profiles'

urlpatterns = [
    path('', pr_list, name='pr_list')
]
