import os
import django
import random

os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE',
    'ecommerce.settings'
)

django.setup()

from store.models import Product

# DELETE OLD PRODUCTS

Product.objects.all().delete()

# CATEGORY-WISE PRODUCTS

products = [

    # ================= MOBILES =================

    {
        "name": "iPhone 15",
        "description": "Latest Apple smartphone",
        "category": "Mobile",
        "image": "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9"
    },

    {
        "name": "Samsung Galaxy S24",
        "description": "Premium Android smartphone",
        "category": "Mobile",
        "image": "https://images.unsplash.com/photo-1598327105666-5b89351aff97"
    },

    # ================= LAPTOPS =================

    {
        "name": "MacBook Air",
        "description": "Apple lightweight laptop",
        "category": "Laptop",
        "image": "https://images.unsplash.com/photo-1517336714739-489689fd1ca8"
    },

    {
        "name": "Dell Inspiron",
        "description": "Professional office laptop",
        "category": "Laptop",
        "image": "https://images.unsplash.com/photo-1496181133206-80ce9b88a853"
    },

    # ================= ACCESSORIES =================

    {
        "name": "Wireless Earbuds",
        "description": "Bluetooth audio earbuds",
        "category": "Accessory",
        "image": "https://images.unsplash.com/photo-1583394838336-acd977736f90"
    },

    {
        "name": "Phone Case",
        "description": "Protective mobile cover",
        "category": "Accessory",
        "image": "https://images.unsplash.com/photo-1601593346740-925612772716"
    },

    # ================= SHIRTS =================

    {
        "name": "Black T-Shirt",
        "description": "Comfortable cotton shirt",
        "category": "Shirt",
        "image": "https://images.unsplash.com/photo-1521572163474-6864f9cf17ab"
    },

    {
        "name": "Formal White Shirt",
        "description": "Office wear formal shirt",
        "category": "Shirt",
        "image": "https://images.unsplash.com/photo-1603252109303-2751441dd157"
    },

    # ================= SHOES =================

    {
        "name": "Nike Air Max",
        "description": "Comfortable running shoes",
        "category": "Shoes",
        "image": "https://images.unsplash.com/photo-1542291026-7eec264c27ff"
    },

    {
        "name": "Adidas UltraBoost",
        "description": "Premium sports shoes",
        "category": "Shoes",
        "image": "https://images.unsplash.com/photo-1600185365483-26d7a4cc7519"
    },

    # ================= WATCHES =================

    {
        "name": "Apple Watch",
        "description": "Smart fitness watch",
        "category": "Watch",
        "image": "https://images.unsplash.com/photo-1523275335684-37898b6baf30"
    },

    {
        "name": "Samsung Watch",
        "description": "Android smartwatch",
        "category": "Watch",
        "image": "https://images.unsplash.com/photo-1546868871-7041f2a55e12"
    },

    # ================= TOYS =================

    {
        "name": "Remote Control Car",
        "description": "Kids racing toy car",
        "category": "Toy",
        "image": "https://images.unsplash.com/photo-1566576912321-d58ddd7a6088"
    },

    {
        "name": "Teddy Bear",
        "description": "Soft plush teddy toy",
        "category": "Toy",
        "image": "https://images.unsplash.com/photo-1615485290382-441e4d049cb5"
    },

    # ================= SPORTS =================

    {
        "name": "Football",
        "description": "Professional football",
        "category": "Sports",
        "image": "https://images.unsplash.com/photo-1575361204480-aadea25e6e68"
    },

    {
        "name": "Basketball",
        "description": "Indoor outdoor basketball",
        "category": "Sports",
        "image": "https://images.unsplash.com/photo-1546519638-68e109498ffc"
    },

    # ================= BOOKS =================

    {
        "name": "Python Programming",
        "description": "Learn Python easily",
        "category": "Book",
        "image": "https://images.unsplash.com/photo-1512820790803-83ca734da794"
    },

    {
        "name": "DSA Mastery",
        "description": "Data Structures and Algorithms",
        "category": "Book",
        "image": "https://images.unsplash.com/photo-1524995997946-a1c2e315a42f"
    },

    # ================= GAMING =================

    {
        "name": "Gaming Keyboard",
        "description": "RGB mechanical keyboard",
        "category": "Gaming",
        "image": "https://images.unsplash.com/photo-1511512578047-dfb367046420"
    },

    {
        "name": "Gaming Headset",
        "description": "Immersive gaming sound",
        "category": "Gaming",
        "image": "https://images.unsplash.com/photo-1612444530582-fc66183b16f7"
    },

    # ================= FITNESS =================

    {
        "name": "Yoga Mat",
        "description": "Exercise fitness yoga mat",
        "category": "Fitness",
        "image": "https://images.unsplash.com/photo-1518611012118-696072aa579a"
    },

    {
        "name": "Dumbbells",
        "description": "Gym workout equipment",
        "category": "Fitness",
        "image": "https://images.unsplash.com/photo-1517836357463-d25dfeac3438"
    },

    # ================= FURNITURE =================

    {
        "name": "Study Table",
        "description": "Modern wooden study table",
        "category": "Furniture",
        "image": "https://images.unsplash.com/photo-1505693416388-ac5ce068fe85"
    },

    {
        "name": "Office Chair",
        "description": "Comfortable office chair",
        "category": "Furniture",
        "image": "https://images.unsplash.com/photo-1505843513577-22bb7d21e455"
    },

]

# CREATE 100 PRODUCTS

for i in range(5):

    for item in products:

        Product.objects.create(

            name=f"{item['name']} {i+1}",

            description=item["description"],

            price=random.randint(999, 99999),

            category=item["category"],

            stock=random.randint(1, 50),

            image_url=item["image"]

        )

print("100% Accurate Products Added Successfully!")