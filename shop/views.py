from django.shortcuts import render
from shop.models import CrochetItem
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def products(request):
    items = CrochetItem.objects.all()
    return render(request, 'shop/products.html', {'items': items})

def homepage(request):
    return render(request, 'shop/homepage.html')

def skirts(request):
    items = CrochetItem.objects.filter(category='skirts')
    return render(request, 'shop/skirts.html', {'items': items})

def bouquets(request):
    items = CrochetItem.objects.filter(category='bouquets')
    return render(request, 'shop/bouquets.html', {'items': items})

def handwarmers(request):
    items = CrochetItem.objects.filter(category='handwarmers') 
    return render(request, 'shop/handwarmers.html', {'items': items})

#i have manually added the reviews as i don't have active customers for now
def reviews(request):
    example_reviews = [
        {
            "user": "Shashswot",
            "review": "Amazing crochet products! Highly recommend!",
            "rating": 5,
        },
        {
            "user": "Sushab",
            "review": "Loved the red rose bouquet. Will buy more.",
            "rating": 4,
        },
        {
            "user": "Sita",
            "review": "The pink skirt is so pretty, great craftsmanship!",
            "rating": 5,
        },
    ]
    return render(request, 'shop/reviews.html', {'reviews': example_reviews})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'shop/signup.html', {'form': form})

def add_to_cart(request, item_id):
    item = CrochetItem.objects.get(id=item_id)
    cart = request.session.get('cart', {})
    item_id_str = str(item_id)
    cart[item_id_str] = {
        'name': item.name,
        'price': float(item.price),
        'quantity': cart.get(item_id_str, {}).get('quantity', 0) + 1
    }
    request.session['cart'] = cart
    return redirect('view_cart')

def view_cart(request):
    cart = request.session.get('cart', {})
    total = sum(item['price'] * item['quantity'] for item in cart.values())
    return render(request, 'shop/cart.html', {'cart': cart, 'total': total})

def remove_from_cart(request, item_id):
    cart = request.session.get('cart', {})
    item_id_str = str(item_id)
    if item_id_str in cart:
        del cart[item_id_str]
        request.session['cart'] = cart
    return redirect('view_cart')

def checkout_cod(request):
    cart = request.session.get('cart', {})
    if not cart:
        return render(request, 'shop/checkout_empty.html')
    # this will help clear the cart after placing an order
    request.session['cart'] = {}
    return render(request, 'shop/checkout_cod.html', {'cart': cart})