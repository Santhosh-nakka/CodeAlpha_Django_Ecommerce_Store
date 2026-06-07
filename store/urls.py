from django.urls import path
from . import views

urlpatterns = [

    # ADD PRODUCT

    path(
        'add-product/',
        views.add_product,
        name='add_product'
    ),

    # WELCOME PAGE

    path(
        '',
        views.welcome,
        name='welcome'
    ),

    # SHOP PAGE

    path(
        'shop/',
        views.home,
        name='home'
    ),

    # PRODUCT DETAIL

    path(
        'product/<int:id>/',
        views.product_detail,
        name='product_detail'
    ),

    # ADD TO CART

    path(
        'add-to-cart/<int:id>/',
        views.add_to_cart,
        name='add_to_cart'
    ),

    # CART

    path(
        'cart/',
        views.cart,
        name='cart'
    ),

    # REMOVE FROM CART

    path(
        'remove-from-cart/<int:id>/',
        views.remove_from_cart,
        name='remove_from_cart'
    ),

    # CHECKOUT

    path(
        'checkout/',
        views.checkout,
        name='checkout'
    ),

    # SUCCESS

    path(
        'success/',
        views.success,
        name='success'
    ),

    # WISHLIST

    path(
        'add-to-wishlist/<int:id>/',
        views.add_to_wishlist,
        name='add_to_wishlist'
    ),

    path(
        'wishlist/',
        views.wishlist,
        name='wishlist'
    ),

    path(
        'remove-from-wishlist/<int:id>/',
        views.remove_from_wishlist,
        name='remove_from_wishlist'
    ),

    # DASHBOARD

    path(
        'dashboard/',
        views.dashboard,
        name='dashboard'
    ),

    # PRODUCT MANAGEMENT

    path(
        'manage-products/',
        views.manage_products,
        name='manage_products'
    ),

    path(
        'view-products/',
        views.view_products,
        name='view_products'
    ),

    path(
        'view-orders/',
        views.view_orders,
        name='view_orders'
    ),

    path(
        'edit-product/<int:product_id>/',
        views.edit_product,
        name='edit_product'
    ),

    path(
        'delete-product/<int:product_id>/',
        views.delete_product,
        name='delete_product'
    ),
path(
    'invoice/',
    views.download_invoice,
    name='invoice'
),
    path(
        'test123/',
        views.welcome,
        name='test123'
    ),
]