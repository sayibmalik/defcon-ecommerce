# ProductViewSet API Examples

## Complete API Response Examples

### 1. List Products Response

**Endpoint:** `GET /api/products/`

**Response:**
```json
{
  "count": 25,
  "next": "http://localhost:8000/api/products/?page=2",
  "previous": null,
  "results": [
    {
      "id": 1,
      "vendor": 1,
      "name": {
        "id": 10,
        "name": "Wireless Headphones",
        "price": "79.99",
        "list_price": "99.99",
        "volume": "0.50",
        "weight": "0.25",
        "compare_list_price": "89.99"
      },
      "image_128": {
        "id": 101,
        "name": "headphones_128",
        "image_128": "/media/product_images/headphones_128.jpg"
      },
      "quantity": 45.0
    },
    {
      "id": 2,
      "vendor": 1,
      "name": {
        "id": 11,
        "name": "USB-C Cable",
        "price": "9.99",
        "list_price": "12.99",
        "volume": "0.01",
        "weight": "0.05",
        "compare_list_price": "10.99"
      },
      "image_128": {
        "id": 102,
        "name": "cable_128",
        "image_128": "/media/product_images/cable_128.jpg"
      },
      "quantity": 250.0
    },
    {
      "id": 3,
      "vendor": 2,
      "name": {
        "id": 12,
        "name": "Laptop Stand",
        "price": "39.99",
        "list_price": "49.99",
        "volume": "2.00",
        "weight": "1.50",
        "compare_list_price": "44.99"
      },
      "image_128": null,
      "quantity": 0.0
    }
  ]
}
```

### 2. Single Product Response

**Endpoint:** `GET /api/products/1/`

**Response:**
```json
{
  "id": 1,
  "vendor": 1,
  "name": {
    "id": 10,
    "name": "Wireless Headphones",
    "account_type": "revenue",
    "price": "79.99",
    "list_price": "99.99",
    "volume": "0.50",
    "weight": "0.25",
    "compare_list_price": "89.99",
    "categ_id": 5,
    "type": "product",
    "create_date": "2024-01-15T10:30:00Z",
    "write_date": "2024-12-08T15:45:00Z"
  },
  "image_128": {
    "id": 101,
    "name": "Headphones 128px variant",
    "image_128": "iVBORw0KGgoAAAANSUhEUgAAAIAAAACACAYAAABccqPeAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAA..."
  },
  "quantity": 45.0
}
```

### 3. Filter by Vendor

**Endpoint:** `GET /api/products/?vendor=1`

**Response:**
```json
{
  "count": 12,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "vendor": 1,
      "name": {
        "id": 10,
        "name": "Wireless Headphones",
        "price": "79.99",
        "list_price": "99.99"
      },
      "image_128": {
        "id": 101,
        "name": "headphones_128",
        "image_128": "/media/product_images/headphones_128.jpg"
      },
      "quantity": 45.0
    }
  ]
}
```

### 4. No Image Available

**Scenario:** Product with no 128px image

**Response:**
```json
{
  "id": 3,
  "vendor": 2,
  "name": {
    "id": 12,
    "name": "Laptop Stand",
    "price": "39.99",
    "list_price": "49.99"
  },
  "image_128": null,
  "quantity": 25.0
}
```

### 5. No Quantity Available

**Scenario:** Product with zero stock

**Response:**
```json
{
  "id": 5,
  "vendor": 3,
  "name": {
    "id": 15,
    "name": "Out of Stock Item",
    "price": "199.99",
    "list_price": "249.99"
  },
  "image_128": {
    "id": 105,
    "name": "item_128",
    "image_128": "/media/product_images/item_128.jpg"
  },
  "quantity": 0.0
}
```

## cURL Examples

### 1. Get all products
```bash
curl -X GET "http://localhost:8000/api/products/" \
  -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGc..."
```

### 2. Get product by ID
```bash
curl -X GET "http://localhost:8000/api/products/1/" \
  -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGc..."
```

### 3. Filter by vendor
```bash
curl -X GET "http://localhost:8000/api/products/?vendor=1" \
  -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGc..."
```

### 4. Pagination
```bash
curl -X GET "http://localhost:8000/api/products/?page=2&page_size=10" \
  -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGc..."
```

## Python Requests Examples

### 1. Basic GET request
```python
import requests

headers = {
    'Authorization': 'Bearer your_jwt_token_here'
}

response = requests.get('http://localhost:8000/api/products/', headers=headers)
products = response.json()

for product in products['results']:
    print(f"Product: {product['name']['name']}")
    print(f"Quantity: {product['quantity']}")
    if product['image_128']:
        print(f"Image: {product['image_128']['image_128']}")
```

### 2. Get specific product
```python
import requests

headers = {
    'Authorization': 'Bearer your_jwt_token_here'
}

response = requests.get('http://localhost:8000/api/products/1/', headers=headers)
product = response.json()

print(f"Name: {product['name']['name']}")
print(f"Price: ${product['name']['price']}")
print(f"Stock: {product['quantity']} units")
print(f"Image: {product['image_128']}")
```

### 3. Filter and process
```python
import requests

headers = {
    'Authorization': 'Bearer your_jwt_token_here'
}

# Get products from vendor 1 that are in stock
response = requests.get('http://localhost:8000/api/products/?vendor=1', headers=headers)
products = response.json()

in_stock_products = [p for p in products['results'] if p['quantity'] > 0]

for product in in_stock_products:
    print(f"{product['name']['name']}: {product['quantity']} units")
```

## Response Field Descriptions

| Field | Type | Description |
|-------|------|-------------|
| `id` | Integer | Product ID |
| `vendor` | Integer | Vendor ID |
| `name` | Object | Full ProductTemplate object |
| `name.name` | String | Product display name |
| `name.price` | String | Current selling price |
| `image_128` | Object/Null | 128px image data (null if not available) |
| `image_128.id` | Integer | Image record ID |
| `image_128.image_128` | String | Base64 encoded or URL to 128px image |
| `quantity` | Float | Total available quantity in stock |

## Error Responses

### 401 Unauthorized
```json
{
  "detail": "Authentication credentials were not provided."
}
```

### 404 Not Found
```json
{
  "detail": "Not found."
}
```

### 400 Bad Request
```json
{
  "vendor": [
    "This field may be null."
  ]
}
```

## Notes

- All requests require JWT authentication
- Image data is retrieved from the ProductImage model with image_1128 field
- Quantity is aggregated from all StockQuant records for the product
- Timestamps are in ISO 8601 format
- All prices are returned as strings with 2 decimal places
