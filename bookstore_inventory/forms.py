from django import forms
from .models import Books

class BookForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ['title', 'author', 'published_date', 'isbn_number', 'price', 'stock_quantity']
        widgets = {
            'published_date': forms.DateInput(attrs={'type': 'date'}),
            'price': forms.NumberInput(attrs={'step': '0.01'}),
            'stock_quantity': forms.NumberInput(attrs={'min': '0'}),
        }

       