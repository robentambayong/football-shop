import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.contrib import messages

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core import serializers

from main.models import Product
from main.forms import ProductForm


# --- Logout ---
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

# --- Login Form ---
def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

# --- Registration Form ---
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

# --- Main page: list all products ---
@login_required(login_url='/login')
def show_main(request):

    filter_type = request.GET.get("filter", "all") # default 'all'

    if filter_type == "all":
        products = Product.objects.all()
    else:
        products = Product.objects.filter(user=request.user)

    context = {
        "npm": "2406453594",       # change to your real NPM
        "name": request.user.username,      # change to your real name
        "class": "PBP KKI",         # change if needed
        "products": products,
        'last_login': request.COOKIES.get('last_login', 'Never')
    }
    return render(request, "main.html", context)


# --- Add new product via form ---
@login_required(login_url='/login')
def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == 'POST':
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return redirect('main:show_main')

    return render(request, "create_product.html", {'form': form})


# --- Detail page for a product ---
@login_required(login_url='/login')
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)
    return render(request, "product_detail.html", {"product": product})


# --- Data delivery views (Assignment 3 requirement) ---

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(
        serializers.serialize("xml", data),
        content_type="application/xml"
    )

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(
        serializers.serialize("json", data),
        content_type="application/json"
    )

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(
        serializers.serialize("xml", data),
        content_type="application/xml"
    )

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(
        serializers.serialize("json", data),
        content_type="application/json"
    )
