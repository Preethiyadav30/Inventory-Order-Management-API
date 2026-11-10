# Inventory & Order Management REST API

## Project Overview

The **Inventory & Order Management REST API** is a backend application developed using Python, Django, and Django REST Framework (DRF).

The project provides APIs to manage product categories, products, customers, and orders. It also includes token-based authentication and automatic stock management during order creation and cancellation.

The APIs can be tested using Postman.

## Features

### 1. User Authentication
- User registration
- User login
- Token-based authentication
- User logout
- Protected API endpoints

### 2. Category Management
- Create categories
- Retrieve category details
- Update categories
- Delete categories

### 3. Product Management
- Add new products
- View product details
- Update product information
- Delete products
- Manage product prices and stock quantities
- Associate products with categories

### 4. Customer Management
- Register customers
- View customer details
- Update customer information
- Delete customers

### 5. Order Management
- Create orders for customers
- Add multiple products to an order
- Calculate total order amount automatically
- Reduce product stock when an order is placed
- Cancel orders
- Restore product stock when an order is cancelled
- View order details and order status

## Technologies Used

- Python
- Django
- Django REST Framework
- SQLite
- Postman
- Git and GitHub

## API Endpoints

# Module #                       # Endpoint(URLS)#                  # Method #

| Register|               `/api/accounts/register/`             | POST |
| Login |                  `/api/accounts/login/`               | POST |
| Logout |                 `/api/accounts/logout/`              | POST |
| Categories |               `/api/categories/`              | GET, POST |
| Category Details |        `/api/categories/{id}/`        | GET, PUT, PATCH, DELETE |
| Products |                  `/api/products/`              | GET, POST |
| Product Details |          `/api/products/{id}/`      | GET, PUT, PATCH, DELETE |
| Customers |                  `/api/customers/`              | GET, POST |
| Customer Details |         `/api/customers/{id}/`       | GET, PUT, PATCH, DELETE |
| Orders |                      `/api/orders/`                 | GET, POST |
| Order Details             | `/api/orders/{id}/`        | GET, PUT, PATCH, DELETE |
| Cancel Order |          `/api/orders/{id}/cancel/`            | POST |

## Authentication

The project uses Django REST Framework Token Authentication.

Users must register and log in to obtain an authentication token.

For protected API requests, include the following header:

`Authorization: Token your_authentication_token`

## Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the project directory

```bash
cd InventoryManagement
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Apply database migrations

```bash
python manage.py migrate
```

### 7. Create a superuser (optional)

```bash
python manage.py createsuperuser
```

### 8. Start the development server

```bash
python manage.py runserver
```

The application will be available at:

`http://127.0.0.1:8000/`

## API Testing

All API endpoints can be tested using **Postman**.

Testing includes:
- Sending GET, POST, PUT, PATCH, and DELETE requests
- Registering and logging in users
- Passing authentication tokens
- Creating and cancelling orders
- Verifying automatic stock updates
- Testing API responses and error handling

## Learning Objectives

- Gain practical experience in backend development using Python, Django, and Django REST Framework.
- Understand REST API development and CRUD operations.
- Learn database design, model relationships, and data management.
- Implement user authentication and authorization.
- Understand order processing and automated inventory stock management.
- Develop skills in API testing and debugging using Postman.
- Gain hands-on experience in building and managing a real-world backend application.


Developed using Python, Django & Django REST Framework.
