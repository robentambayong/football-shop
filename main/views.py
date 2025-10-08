import datetime
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags
from django.forms.models import model_to_dict

from main.models import Product
from main.forms import ProductForm

# --- Page Rendering Views ---

@login_required(login_url='/login/')
def show_main(request):
    context = { 'last_login': request.COOKIES.get('last_login', 'Never') }
    return render(request, "main.html", context)

@login_required(login_url='/login/')
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)
    return render(request, "product_detail.html", {"product": product})

def login_user(request):
   form = AuthenticationForm()
   return render(request, 'login.html', {'form': form})

def register_user(request):
    form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

# --- AJAX Endpoints ---

@csrf_exempt
@require_POST
@login_required
def add_product_ajax(request):
    form = ProductForm(request.POST)
    if form.is_valid():
        # Create the product from cleaned data, ensuring security and correctness
        product = form.save(commit=False)
        product.user = request.user
        # Apply strip_tags to the specific fields
        product.name = strip_tags(form.cleaned_data.get("name"))
        product.description = strip_tags(form.cleaned_data.get("description"))
        product.save()
        return HttpResponse(b"CREATED", status=201)
    else:
        # Return form errors if validation fails
        return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)

@csrf_exempt
@require_POST
@login_required
def edit_product(request, id):
    product = get_object_or_404(Product, pk=id, user=request.user)
    form = ProductForm(request.POST, instance=product)
    if form.is_valid():
        # Save the form with the updated data
        product = form.save(commit=False)
        # Apply strip_tags to the specific fields
        product.name = strip_tags(form.cleaned_data.get("name"))
        product.description = strip_tags(form.cleaned_data.get("description"))
        product.save()
        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error", "errors": form.errors}, status=400)

@csrf_exempt
@require_POST
@login_required
def delete_product_ajax(request, id):
    try:
        product = Product.objects.get(pk=id, user=request.user)
        product.delete()
        return JsonResponse({"status": "success"}, status=200)
    except Product.DoesNotExist:
        return JsonResponse({"status": "error", "message": "Product not found or permission denied."}, status=404)

@csrf_exempt
@require_POST
def login_ajax(request):
    form = AuthenticationForm(data=request.POST)
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = JsonResponse({"status": "success", "message": "Login successful!"})
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response
    else:
        return JsonResponse({"status": "error", "message": "Invalid username or password."}, status=401)

@csrf_exempt
@require_POST
def register_ajax(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        return JsonResponse({"status": "success", "message": "Registration successful! You can now log in."}, status=201)
    else:
        return JsonResponse({"status": "error", "errors": form.errors}, status=400)

# --- JSON Data Endpoints ---

@login_required
def get_products_json(request):
    filter_type = request.GET.get("filter")
    if filter_type == "my":
        products = Product.objects.filter(user=request.user)
    else:
        products = Product.objects.all()
    return HttpResponse(serializers.serialize("json", products), content_type="application/json")

@login_required
def get_product_by_id_json(request, id):
    product = get_object_or_404(Product, pk=id)
    return JsonResponse(model_to_dict(product))

# --- Legacy Data Views (Assignment 3) ---
def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

