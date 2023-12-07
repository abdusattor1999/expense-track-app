from django.db import models

class Publisher(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

class BookCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

class Book(models.Model):
    book_id = models.CharField(max_length=50)
    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=250)
    authors = models.CharField(max_length=300)
    publisher = models.ForeignKey(Publisher, models.SET_NULL, null=True, blank=True)
    publish_date = models.DateField()
    category = models.ForeignKey(BookCategory, on_delete=models.CASCADE, blank=True, null=True)
    distribution_expense = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self) -> str:
        return self.title
    
    
SELECT_CATEGORY_CHOICES = [
    ("Food","Food"),
    ("Travel","Travel"),
    ("Shopping","Shopping"),
    ("Necessities","Necessities"),
    ("Entertainment","Entertainment"),
    ("Other","Other")
 ]
ADD_EXPENSE_CHOICES = [
     ("Expense","Expense"),
     ("Income","Income")
]

class Expanse(models.Model):
    user = models.ForeignKey('profiles.Profile', models.CASCADE, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=15, choices=ADD_EXPENSE_CHOICES)
    date = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=20, choices=SELECT_CATEGORY_CHOICES, blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.type}-{self.amount}"
