from django.urls import path
from . import views  
from django.conf.urls.static import static
from django.conf import settings

app_name = 'expenses'

urlpatterns = [
    path('books/', views.books_list, name="book_list"),
    path('statistics/', views.EditorChartView.as_view(), name="EditorChartView"),
    path('excel-upload/', views.Import_Excel_pandas, name="Import_Excel_pandas"),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)