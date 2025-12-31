# Knotique - Handmade Crochet E-commerce Site

A Django-based e-commerce website for selling handmade crochet items including handwarmers, skirts, and bouquets.

## Features

- 🛍️ **Product Catalog**: Browse products by category (Handwarmers, Skirts, Bouquets)
- 🛒 **Shopping Cart**: Add items to cart with quantity tracking
- 💳 **Cash on Delivery (COD)**: Simple checkout process with COD payment option
- 👤 **User Authentication**: Sign up, login, and logout functionality
- ⭐ **Customer Reviews**: View customer testimonials
- 🎨 **Beautiful UI**: Pink-themed, responsive design

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/nuskfr/Knotique.git
cd Knotique
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run database migrations:
```bash
python manage.py migrate
```

4. Create a superuser (admin):
```bash
python manage.py createsuperuser
```

5. Run the development server:
```bash
python manage.py runserver
```

6. Access the site at `http://localhost:8000/`

## Project Structure

```
Knotique/
├── myshop/                 # Project settings
│   ├── settings.py         # Django settings
│   ├── urls.py            # Main URL configuration
│   └── wsgi.py            # WSGI configuration
├── shop/                   # Main app
│   ├── models.py          # Database models (CrochetItem)
│   ├── views.py           # View functions
│   ├── admin.py           # Admin configuration
│   ├── templates/shop/    # HTML templates
│   └── migrations/        # Database migrations
├── media/                  # Uploaded images
├── db.sqlite3             # SQLite database (development)
├── requirements.txt       # Python dependencies
└── manage.py              # Django management script
```

## Usage

### Admin Panel

Access the admin panel at `http://localhost:8000/admin/` to:
- Add/edit/delete products
- Manage users
- View all crochet items

### Adding Products

1. Log in to the admin panel
2. Go to "Crochet items"
3. Click "Add Crochet Item"
4. Fill in:
   - Name
   - Description
   - Price
   - Category (handwarmers, skirts, or bouquets)
   - Image (optional)

### Customer Features

- **Browse Products**: Visit homepage and click category buttons or "Explore All Items"
- **Add to Cart**: Click "Add to Cart" on any product
- **View Cart**: Click "Cart" in navigation
- **Checkout**: Click "Proceed to Checkout (COD)" in cart
- **Sign Up**: Create an account via "Signup" link
- **Login**: Access your account via "Login" link

## Database Configuration

### Development (Default - SQLite)

The project is configured to use SQLite by default for easy development and testing.

### Production (PostgreSQL)

For production, uncomment the PostgreSQL configuration in `myshop/settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'Knotique',
        'USER': 'postgres',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

## Future Enhancements

- ✨ eSewa payment gateway integration (structure prepared)
- 📧 Email notifications for orders
- 📦 Order tracking system
- 🔍 Product search functionality
- 💬 Customer review submission

## Technologies Used

- **Backend**: Django 6.0
- **Database**: SQLite (development) / PostgreSQL (production)
- **Frontend**: HTML, CSS, Bootstrap 5
- **Image Handling**: Pillow

## License

This project is created for educational purposes.

## Author

Created by nuskfr - Knotique Handmade Crochet Shop
