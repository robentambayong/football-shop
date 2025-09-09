from django.shortcuts import render

def home(request):
    context = {
        "app_name": "Football Shop",     # Application name
        "your_name": "Roben Joseph B Tambayong",  # Your name
        "your_class": "Ilmu Komputer KKI 2024"        # Your class
    }
    return render(request, "home.html", context)