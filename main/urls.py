from django.urls import path
from main.views import (
    show_main,
    show_product,
    register_user,
    login_user,
    logout_user,
    get_products_json,
    add_product_ajax,
    edit_product,
    get_product_by_id_json,
    delete_product_ajax,
    login_ajax,
    register_ajax,
)

app_name = "main"

urlpatterns = [
    # Page Rendering URLs
    path("", show_main, name="show_main"),
    path("product/<int:id>/", show_product, name="show_product"),
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),

    # AJAX Endpoints
    path("get-products/", get_products_json, name="get_products_json"),
    path("create-product-ajax/", add_product_ajax, name="add_product_ajax"),
    # Corrected URL pattern for editing
    path('edit-product/<int:id>/', edit_product, name='edit_product'), 
    path('get-product/<int:id>/', get_product_by_id_json, name='get_product_by_id_json'),
    path('delete-product-ajax/<int:id>/', delete_product_ajax, name='delete_product_ajax'),
    path('login-ajax/', login_ajax, name='login_ajax'),
    path('register-ajax/', register_ajax, name='register_ajax'),
]

