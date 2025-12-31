from django.shortcuts import render
from shop.models import CrochetItem
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

# Sample reviews data shared across views
SAMPLE_REVIEWS = [
    {
        "user": "Shashswot",
        "review": "Amazing crochet products! Highly recommend!",
        "rating": 5,
        "image": "/media/site_images/reviewer1.png",
    },
    {
        "user": "Sushab",
        "review": "Loved the red rose bouquet. Will buy more.",
        "rating": 4,
        "image": "/media/site_images/reviewer2.png",
    },
    {
        "user": "Sita",
        "review": "The pink skirt is so pretty, great craftsmanship!",
        "rating": 5,
        "image": "/media/site_images/reviewer3.jpg",
    },
]

def products(request):
    items = CrochetItem.objects.all()
    return render(request, 'shop/products.html', {'items': items})

def homepage(request):
    return render(request, 'shop/homepage.html', {'reviews': SAMPLE_REVIEWS})

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
    return render(request, 'shop/reviews.html', {'reviews': SAMPLE_REVIEWS})

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
    # Calculate subtotal for each item and overall total
    cart_items = []
    total = 0
    for item_id, item in cart.items():
        subtotal = item['price'] * item['quantity']
        cart_items.append({
            'id': item_id,
            'name': item['name'],
            'price': item['price'],
            'quantity': item['quantity'],
            'subtotal': subtotal
        })
        total += subtotal
    return render(request, 'shop/cart.html', {'cart_items': cart_items, 'total': total, 'cart': cart})

def remove_from_cart(request, item_id):
    cart = request.session.get('cart', {})
    item_id_str = str(item_id)
    if item_id_str in cart:
        del cart[item_id_str]
        request.session['cart'] = cart
    return redirect('view_cart')

def checkout_cod(request):
    """
    Cash on Delivery checkout
    Clears the cart after placing an order
    """
    cart = request.session.get('cart', {})
    if not cart:
        return render(request, 'shop/checkout_empty.html')
    # Clear the cart after placing an order
    request.session['cart'] = {}
    return render(request, 'shop/checkout_cod.html', {'cart': cart})

# TODO: Future eSewa payment gateway integration
# When ready to integrate eSewa:
# - Create checkout_esewa view
# - Generate unique transaction IDs
# - Implement eSewa API calls
# - Handle success/failure callbacks
# - Update URLs to include eSewa routes