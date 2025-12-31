# Knotique - Handmade Crochet Shop

Welcome to Knotique, an e-commerce platform for handmade crochet items built with Django.

## Features

- Product catalog with categories (handwarmers, skirts, bouquets)
- Shopping cart functionality
- User authentication (login/signup)
- Cash on Delivery checkout
- Customer reviews
- Responsive design with Bootstrap

## Setup Instructions

### Prerequisites

- Python 3.8+
- PostgreSQL 12+
- pgAdmin (optional, for database management)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Knotique
   ```

2. **Install dependencies**
   ```bash
   pip install Django psycopg2-binary Pillow
   ```

3. **Configure PostgreSQL**
   - Ensure PostgreSQL server is running
   - Create a database named `Knotique`
   - Update credentials in `myshop/settings.py` if needed:
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

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser**
   ```bash
   python manage.py createsuperuser
   ```

6. **Add product images**
   - Place product images in `media/crochet_images/`
   - Sample images are already included

7. **Add products via admin panel**
   ```bash
   python manage.py runserver
   ```
   - Navigate to `http://localhost:8000/admin`
   - Login with superuser credentials
   - Add CrochetItem products with:
     - Name
     - Description
     - Price
     - Image
     - Category (handwarmers, skirts, bouquets, or general)

## Running the Application

```bash
python manage.py runserver
```

Visit `http://localhost:8000` to view the application.

## Project Structure

```
Knotique/
├── myshop/              # Main project settings
│   ├── settings.py      # Django settings (PostgreSQL configured)
│   └── urls.py          # URL routing
├── shop/                # Shop application
│   ├── models.py        # CrochetItem model
│   ├── views.py         # View functions
│   ├── templates/       # HTML templates
│   └── migrations/      # Database migrations
├── media/               # User-uploaded files
│   └── crochet_images/  # Product images
└── manage.py            # Django management script
```

## Key Changes from SQLite to PostgreSQL

- Database engine changed from `sqlite3` to `postgresql`
- Added `psycopg2-binary` dependency for PostgreSQL adapter
- Created migrations for PostgreSQL database
- All models now work with PostgreSQL

## Template Enhancements

- Consistent pink theme (#ff66cc) across all pages
- Styled buttons for all actions
- Image display in product listings
- Responsive layout with Bootstrap 5
- Enhanced user authentication pages

## Testing

To test the application:

1. **Authentication**: Try signup and login
2. **Browse Products**: Visit different category pages
3. **Shopping Cart**: Add items to cart, remove items
4. **Checkout**: Complete a cash on delivery order
5. **Admin Panel**: Manage products through Django admin

## Notes

- Images should be added to `media/crochet_images/` directory
- Ensure PostgreSQL server is active before running the application
- Use pgAdmin for database management and monitoring
