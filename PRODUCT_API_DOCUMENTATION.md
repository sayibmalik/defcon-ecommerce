# ProductViewSet API Documentation

## Overview
Updated the `ProductViewSet` API to retrieve product image (128px) and quantity information along with product details.

## Changes Made

### 1. Updated ProductSerializer (`multivendor/serializers.py`)

#### New Imports
```python
from django.db.models import Sum
from home.models import ProductTemplate, ProductImage, StockQuant
```

#### New Serializer Class
**ProductImageSerializer** - Handles serialization of product images
```python
class ProductImageSerializer(serializers.ModelSerializer):
    """Serializer for 128px product images"""
    class Meta:
        model = ProductImage
        fields = ('id', 'name', 'image_1128')
```

#### Enhanced ProductSerializer
The `ProductSerializer` now includes two new custom fields:

- **image_128** (SerializerMethodField): Returns the 128px product image
- **quantity** (SerializerMethodField): Returns total available quantity from stock

```python
class ProductSerializer(serializers.ModelSerializer):
    name = ProductTemplateSerializer(read_only=True)
    image_128 = serializers.SerializerMethodField(read_only=True)
    quantity = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Product
        fields = ('id', 'vendor', 'name', 'image_128', 'quantity')
```

### 2. Method Implementations

#### get_image_128(self, obj)
Retrieves the 128px image for the product from the ProductImage model.

**Logic:**
- Filters ProductImage by product template ID
- Returns image data with id, name, and image_1128 field
- Returns None if no image is found

**Response Example:**
```json
{
  "id": 1,
  "name": "Product Image Name",
  "image_128": "base64_encoded_image_data_or_url"
}
```

#### get_quantity(self, obj)
Retrieves total quantity available for the product from StockQuant.

**Logic:**
- Filters StockQuant by product ID
- Aggregates quantity across all warehouse locations
- Returns 0 if no quantity is found or on error

**Response Example:**
```json
{
  "quantity": 150.0
}
```

## API Response Example

```json
{
  "id": 1,
  "vendor": 1,
  "name": {
    "id": 10,
    "name": "Product Name",
    "price": "100.00",
    "list_price": "120.00"
  },
  "image_128": {
    "id": 1,
    "name": "Product Image",
    "image_128": "image_data"
  },
  "quantity": 150.0
}
```

## Database Models Used

### ProductImage
- Field: `image_1128` - The 128px product image
- Field: `product_tmpl_id` - Foreign key to ProductTemplate
- Located in: `home.models.ProductImage`

### StockQuant
- Field: `product_id` - Foreign key to Product
- Field: `quantity` - Available quantity
- Located in: `home.models.StockQuant`

## Error Handling

Both methods include try-except blocks to gracefully handle errors:
- Returns `None` for image_128 if no image found or error occurs
- Returns `0` for quantity if no stock found or error occurs

## Usage

The ProductViewSet can be accessed via:

```
GET /api/products/ - List all products with image and quantity
GET /api/products/{id}/ - Retrieve specific product with image and quantity
```

### Query Parameters
Use existing ProductViewSet filters:
- `vendor={vendor_id}` - Filter by vendor
- Any standard DRF pagination parameters

## Performance Considerations

1. **Database Queries:**
   - Each product retrieval triggers 2 additional queries (image lookup + quantity aggregation)
   - Consider using `select_related()` or `prefetch_related()` if performance becomes an issue

2. **Optimization Recommendations:**
   - For large result sets, consider caching image URLs
   - Use database indexes on `product_tmpl_id` and `product_id` fields
   - Consider implementing a dedicated quantity view/field at the database level

## Testing

To test the API:

```bash
# List products with images and quantities
curl -X GET "http://localhost:8000/api/products/" \
  -H "Authorization: Bearer YOUR_TOKEN"

# List products by vendor
curl -X GET "http://localhost:8000/api/products/?vendor=1" \
  -H "Authorization: Bearer YOUR_TOKEN"
```

## Notes

- The serializer requires authentication (JWT)
- Image data is returned as-is from the ProductImage model
- Quantity is aggregated across all warehouse locations
- All fields are read-only (no write operations on image/quantity through API)
