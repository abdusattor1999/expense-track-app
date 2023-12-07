from django.contrib import admin
from django.urls import path, include
from expenses.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('expenses/', include('expenses.urls')),
    path('profiles/', include('profiles.urls')),
    path('', home, name='index'),
]
