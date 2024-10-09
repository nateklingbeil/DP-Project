from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Product, User
from .forms import UserForm


# Create your views here.
def index(request):
    # fetching all th e products and passing them to the template
    Product_list = Product.objects.all()
    return render(request, 'index.html', {'products': Product_list})

def new_user(request):
    # if the request is a post, handle form submission
    if request.method == 'POST':
        form = UserForm(request.POST) # <- sending info to UserForm
        if form.is_valid(): 
            form.save() # <-- save the form to the sql database
            return redirect('index') # <- once submitted, redirects back to index.html
    else:
        form = UserForm()
    # rendering the new user form
    return render(request, 'newuser.html', {'form': form}) 

    # get all users from user template in models.py and passes them to the table template
def user_table(request):
    users = User.objects.all()
    return render(request, 'usertable.html', {'users': users})