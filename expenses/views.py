from django.views.generic import TemplateView
from django.shortcuts import render 
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
import pandas as pd
from .models import Book, BookCategory, Publisher, Expanse
from .resourse import BookResource
from tablib import Dataset



def home(request):
    return render(request, 'home_page.html')

def books_list(request):
    books = Book.objects.all()[:10]
    return render(request, 'book_list.html', {'books':books})

def Import_Excel_pandas(request):
    if request.method == 'POST' and request.FILES.get('spreadsheet', None):      
        spreadsheet = request. FILES['spreadsheet']
        fs = FileSystemStorage()
        filename = fs.save(spreadsheet.name, spreadsheet)
        uploaded_file_url = fs.url(filename)              
        empexceldata = pd.read_excel(f"media/{filename}")        
        dbframe = empexceldata
        for dbframe in dbframe.itertuples():
            obj = Book.objects.create(
                book_id=dbframe.id,
                title=dbframe.title, 
                subtitle=dbframe.subtitle,
                authors=dbframe.authors, 
                publisher=Publisher.objects.get_or_create(name=dbframe.publisher)[0], 
                publish_date=dbframe.published_date, 
                category=BookCategory.objects.get_or_create(name=dbframe.category)[0],
                distribution_expense=dbframe.distribution_expense)   

        return render(request, 'Import_excel_db.html', {
            'uploaded_file_url': uploaded_file_url
        })   
    return render(request, 'Import_excel_db.html',{})


def import_excel(request):
    if request.method == 'POST':
        book =BookResource()
        dataset = Dataset()
        new_book = request.FILES['myfile']
        data_import = dataset.load(new_book.read())
        result = BookResource.import_data(dataset,dry_run=True)
        if not result.has_errors():
            BookResource.import_data(dataset,dry_run=False)        
    return render(request, 'Import_excel_db.html',{})


# Creating views
class EditorChartView(TemplateView):
    template_name = 'chart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categs = BookCategory.objects.all()
        context['expanse_by_categ'] = []
        
        for categ in categs:
            data = {'label':categ.name}
            data['expanse'] = self.get_filtered_qs(category=categ)
            context['expanse_by_categ'].append(data)

        return context
    
    def get_filtered_qs(self, category=None, publisher=None) -> int: 
        qs = None
        summa = 0
        if publisher:
            qs = Book.objects.filter(publisher=publisher)
        elif category:
            qs = Book.objects.filter(category=category)
        
        for obj in qs:
            if isinstance(obj, Book):
                summa += obj.distribution_expense
            else:
                for i in obj:
                    summa += i.distribution_expense
        return summa
        