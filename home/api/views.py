import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import JsonRPCSerializer

class OdooProxyView(APIView):
    """
    Django API that accepts the exact JSON format and calls Odoo JSON-RPC.
    """
    def post(self, request):
        serializer = JsonRPCSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        payload = serializer.validated_data
        
        # Extract params
        params = payload["params"]
        args = params["args"]

        # db = args[0]
        db = "zainab"
        # uid = args[1]
        uid = 2
        password = "Defcon@123#"
        # password = args[2]
        model = args[3]
        method = args[4]
        domain = args[5]
        extra = args[6]

        odoo_url = "https://kashdeals.com/jsonrpc"

        # Prepare JSON-RPC data for Odoo call
        odoo_payload = {
            "jsonrpc": "2.0",
            "method": "call",
            "params": {
                "service": "object",
                "method": "execute_kw",
                "args": [
                    db,
                    uid,
                    password,
                    model,
                    method,
                    domain,
                    extra
                ]
            },
            "id": payload["id"]
        }

        try:
            response = requests.post(odoo_url, json=odoo_payload)
            odoo_result = response.json()
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        return Response(odoo_result)
