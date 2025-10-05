from django.shortcuts import render,redirect, get_list_or_404, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Books
from .forms import BookForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test 
@user_passes_test(lambda u: u.is_staff)
def delete_book(request, books_id):
    book = get_object_or_404(Books, id=books_id)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'inventory/confirm_delete.html', {'book': book})


def book_list(request):
    query = request.GET.get('q', '')
    if query:
        books = Books.objects.filter(title__icontains=query)
    else:
        books = Books.objects.all()
    return render(request, 'inventory/book_list.html', {'books': books, 'query': query})

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'inventory/add_books.html', {'form': form})


def update_book(request, books_id):
    books = get_object_or_404(Books, id=books_id)
    if request.method == 'POST':
                form = BookForm(request.POST, instance=books)
                if form.is_valid():
                    form.save()
                    return redirect('book_list')
    else:
        form = BookForm(instance=books)
    return render(request, 'inventory/update.html', {'form': form,'form.instance.pk': True})



def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})


@login_required
def home_view(request):
    books = Books.objects.all()
    return render(request, 'inventory/book_list.html', {'books': books})