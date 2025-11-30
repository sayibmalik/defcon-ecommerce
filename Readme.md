{
    "jsonrpc": "2.0",
    "method": "call",
    "params": {
        "service": "object",
        "method": "execute_kw",
        "args": [
            "my_db",
            2,
            "admin",
            "product.product",
            "search_read",
            [
                [
                    ["is_published", "=", "true"]
                ]
            ],
            {
                "fields": [
                    "name",
                    "default_code",
                    "list_price",
                    "barcode",
                    "qty_available",
                    "type",
                    "categ_id",
                    "image_128"
                ],
                "limit": 3
            }
        ]
    },
    "id": 1
}



docker compose up --build
http://localhost:8000/api/models/
http://localhost:8000/api/models/?model=account_account




how i moved the backup

docker build -t odoo18 -f odooDockerfile .
check base image for ref

docker tag odoo18 nexus.defconinnovations.in/backup/kashdeals:odoo-18.1

docker push nexus.defconinnovations.in/backup/kashdeals:odoo-18.1      