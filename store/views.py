from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Product, Order, Review
from django.db.models import Avg, Max
from django.http import HttpResponse

from reportlab.pdfgen import canvas

# WELCOME PAGE

def welcome(request):

    return render(request, 'welcome.html')


# HOME PAGE

def home(request):

    search = request.GET.get('search', '')

    category = request.GET.get('category')

    sort = request.GET.get('sort')

    products_list = Product.objects.all()

    # SEARCH

    if search:
        products_list = products_list.filter(name__icontains=search)

    # CATEGORY

    if category:
        products_list = products_list.filter(category=category)

    # SORT

    if sort == 'low':
        products_list = products_list.order_by('price')

    elif sort == 'high':
        products_list = products_list.order_by('-price')

    # PAGINATION

    paginator = Paginator(products_list, 12)

    page_number = request.GET.get('page')

    products = paginator.get_page(page_number)

    # CART COUNT

    cart = request.session.get('cart', {})

    return render(request, 'home.html', {
        'products': products,
        'cart_count': sum(cart.values()),
        'search': search
    })


# PRODUCT DETAIL

def product_detail(request, id):

    product = Product.objects.get(id=id)

    if request.method == 'POST':

        Review.objects.create(

            product=product,

            name=request.POST.get('name'),

            rating=request.POST.get('rating'),

            comment=request.POST.get('comment')
        )

        return redirect('product_detail', id=id)

    reviews = product.reviews.all().order_by(
        '-created_at'
    )

    average_rating = reviews.aggregate(
        Avg('rating')
    )['rating__avg']

    cart = request.session.get('cart', {})

    return render(
        request,
        'product_detail.html',
        {
            'product': product,

            'reviews': reviews,

            'average_rating': round(
                average_rating or 0,
                1
            ),

            'cart_count': sum(cart.values())
        }
    )


# ADD TO CART

def add_to_cart(request, id):

    cart = request.session.get('cart', {})

    id = str(id)

    if id in cart:
        cart[id] += 1

    else:
        cart[id] = 1

    request.session['cart'] = cart

    return redirect('cart')


# CART PAGE

def cart(request):

    cart = request.session.get('cart', {})

    ids = cart.keys()

    products = Product.objects.filter(id__in=ids)

    cart_items = []

    total = 0

    for product in products:

        quantity = cart[str(product.id)]

        subtotal = product.price * quantity

        total += subtotal

        cart_items.append({
            'product': product,
            'quantity': quantity,
            'subtotal': subtotal
        })

    return render(request, 'cart.html', {
        'cart_items': cart_items,
        'total': total,
        'cart_count': sum(cart.values())
    })


# REMOVE FROM CART

def remove_from_cart(request, id):

    cart = request.session.get('cart', {})

    id = str(id)

    if id in cart:

        if cart[id] > 1:
            cart[id] -= 1

        else:
            del cart[id]

    request.session['cart'] = cart

    return redirect('cart')


# CHECKOUT

def checkout(request):

    cart = request.session.get('cart', {})

    ids = cart.keys()

    products = Product.objects.filter(id__in=ids)

    total = 0

    checkout_items = []

    for product in products:

        quantity = cart[str(product.id)]

        subtotal = product.price * quantity

        total += subtotal

        checkout_items.append({
            'product': product,
            'quantity': quantity,
            'subtotal': subtotal
        })

    return render(request, 'checkout.html', {
        'checkout_items': checkout_items,
        'total': total,
        'cart_count': sum(cart.values())
    })


# SUCCESS PAGE

def success(request):

    cart = request.session.get('cart', {})

    ids = cart.keys()

    products = Product.objects.filter(id__in=ids)

    total = 0

    for product in products:
        quantity = cart[str(product.id)]
        total += product.price * quantity
        product.stock -= quantity
        product.save()

    if total > 0:

        Order.objects.create(

    customer_name=request.POST.get(
        'customer_name',
        'Unknown'
    ),

    customer_email=request.POST.get(
        'customer_email',
        'unknown@example.com'
    ),

    customer_phone=request.POST.get(
        'customer_phone',
        '0000000000'
    ),

    customer_address=request.POST.get(
        'customer_address',
        'Unknown'
    ),

    total_price=total
)

    request.session['cart'] = {}

    return render(
        request,
        'success.html'
    )
# =========================
# WISHLIST
# =========================

def add_to_wishlist(request, id):

    wishlist = request.session.get('wishlist', [])

    if id not in wishlist:

        wishlist.append(id)

    request.session['wishlist'] = wishlist

    return redirect('home')


def wishlist(request):

    wishlist = request.session.get('wishlist', [])

    products = Product.objects.filter(id__in=wishlist)

    return render(request, 'wishlist.html', {

        'products': products,

        'wishlist_count': len(wishlist),

        'cart_count': sum(
            request.session.get('cart', {}).values()
        )
    })


def remove_from_wishlist(request, id):

    wishlist = request.session.get('wishlist', [])

    if id in wishlist:

        wishlist.remove(id)

    request.session['wishlist'] = wishlist

    return redirect('wishlist')
# =========================
# DASHBOARD
# =========================

def dashboard(request):

    total_products = Product.objects.count()

    total_stock = sum(
        product.stock
        for product in Product.objects.all()
    )

    categories = Product.objects.values_list(
        'category',
        flat=True
    ).distinct()

    total_categories = len(categories)

    cart = request.session.get('cart', {})

    wishlist = request.session.get('wishlist', [])

    total_cart_items = sum(cart.values())

    total_wishlist_items = len(wishlist)
    total_orders = Order.objects.count()
    low_stock_products = Product.objects.filter(
        stock__lt=5
    ).count()
    average_price = Product.objects.aggregate(
        Avg('price')
    )['price__avg']
    most_expensive_product = Product.objects.order_by(
        '-price'
    ).first()
    return render(request, 'dashboard.html', {

        'total_products': total_products,

        'total_stock': total_stock,

        'total_categories': total_categories,

        'total_cart_items': total_cart_items,

        'total_wishlist_items': total_wishlist_items,
        'total_orders': total_orders,
        'low_stock_products': low_stock_products,

'average_price': round(average_price or 0),

'most_expensive_product': most_expensive_product,

    })

def add_product(request):

    if request.method == 'POST':

        Product.objects.create(

            name=request.POST.get('name'),

            price=request.POST.get('price'),

            category=request.POST.get('category'),

            image_url=request.POST.get('image_url'),

            description=request.POST.get('description'),

            stock=1

        )

        return redirect('home')

    return render(
        request,
        'add_product.html'
    )
def manage_products(request):

    return render(
        request,
        'manage_products.html'
    )
def view_products(request):

    products = Product.objects.all()

    search = request.GET.get('search')

    if search:

        products = products.filter(
            name__icontains=search
        )

    return render(
        request,
        'view_products.html',
        {
            'products': products
        }
    )
def delete_product(request, product_id):

    product = Product.objects.get(id=product_id)

    product.delete()

    return redirect('view_products')
def edit_product(request, product_id):

    product = Product.objects.get(id=product_id)

    if request.method == 'POST':

        product.name = request.POST.get('name')

        product.price = request.POST.get('price')

        product.category = request.POST.get('category')

        product.image_url = request.POST.get('image_url')

        product.description = request.POST.get('description')

        product.save()

        return redirect('view_products')

    return render(
        request,
        'edit_product.html',
        {
            'product': product
        }
    )
def view_orders(request):

    orders = Order.objects.all().order_by('-created_at')

    total_revenue = 0

    for order in orders:

        total_revenue += order.total_price

    return render(
        request,
        'view_orders.html',
        {
            'orders': orders,
            'total_revenue': total_revenue
        }
    )
def download_invoice(request):

    response = HttpResponse(
        content_type='application/pdf'
    )

    response['Content-Disposition'] = (
        'attachment; filename="invoice.pdf"'
    )

    p = canvas.Canvas(response)

    p.setFont("Helvetica-Bold", 20)

    p.drawString(
        200,
        800,
        "MyStore Invoice"
    )

    latest_order = Order.objects.order_by(
        '-created_at'
    ).first()

    p.setFont("Helvetica", 12)

    if latest_order:
        p.drawString(
        50,
        740,
        f"Order ID: {latest_order.id}"
    )
        p.drawString(
        50,
        710,
        f"Customer: {latest_order.customer_name}"
    )
        p.drawString(
        50,
        680,
        f"Email: {latest_order.customer_email}"
    )
        p.drawString(
        50,
        650,
        f"Phone: {latest_order.customer_phone}"
    )
        p.drawString(
        50,
        620,
        f"Address: {latest_order.customer_address}"
    )
        p.drawString(
        50,
        590,
        f"Total Amount: Rs.{latest_order.total_price}"
    )
    else:

        p.drawString(
            50,
            740,
            "No Orders Found"
        )

    p.save()

    return response