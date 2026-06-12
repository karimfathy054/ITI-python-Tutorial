from django.shortcuts import redirect
from django.http import HttpResponse
from django.shortcuts import render

books={
    1:{"id":1,"title":"book1","price":100},
    2:{"id":2,"title":"book2","price":200},
    3:{"id":3,"title":"book3","price":300}
    }
books_id = 4
# Create your views here.
def index(request):
    return render(request,"index.html",{"books":books.values()})

def create(request):
    return render(request,"create.html")

def store(request):
    # using post request because I can not pass multiple data items as path parameters
    # and I didn't feel like passing it in query parameters too as I didn't want to search about that
    # sending parameters in post body is the right way to send data to the server
    global books_id
    title,price = request.POST.get("title"), request.POST.get("price")
    books[books_id] = {"id":books_id,"title":title,"price":price}
    books_id+=1
    return redirect("books:index")

def show(request,id):
    book = books[id]
    return render(request,"show.html",{"book":book})

def edit(request,id):
    book = books[id]
    return render(request,"edit.html",{"book":book})

def update(request,id):
    book = books[id]
    
    title,price = request.POST.get("title"), request.POST.get("price")
    book["title"] = title   
    book["price"] = price
    return redirect("books:index")

def delete(request,id):
    del books[id]
    return redirect("books:index")

    
    