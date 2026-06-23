from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from books.models import Book
from books.forms import BookForm
from django.shortcuts import redirect
from django.shortcuts import render

# Create your views here.
def index(request):
    books = Book.objects.all()
    return render(request,"index.html",{"books":books})

@permission_required('books.can_add_book')
@login_required
def create(request):
    form = BookForm()
    return render(request,"create.html",{"form":form})

@permission_required('books.can_add_book')
@login_required
def store(request):
    form = BookForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect("books:index")
    return render(request,"create.html",{"form":form})

def show(request,id):
    book = Book.objects.get(id=id)
    return render(request,"show.html",{"book":book})

@permission_required('books.can_edit_book')
@login_required
def edit(request,id):
    book = Book.objects.get(id=id)
    form = BookForm(instance=book)
    return render(request,"edit.html",{"book":book,"form":form})

@permission_required('books.can_edit_book')
@login_required
def update(request,id):
    book = Book.objects.get(id=id)
    form = BookForm(request.POST,instance=book)
    if form.is_valid():
        form.save()
        return redirect("books:index")
    return render(request,"edit.html",{"book":book,"form":form})

@permission_required('books.can_delete_book')
@login_required
def delete(request,id):
    Book.objects.get(id=id).delete()
    return redirect("books:index")



    
    