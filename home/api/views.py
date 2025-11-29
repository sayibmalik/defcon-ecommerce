import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import JsonRPCSerializer, create_dynamic_serializer
from django.apps import apps


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





class DynamicModelView(APIView):
    """
    API to list all models and fetch data from a given model.
    """
    
    def get(self, request):
        model_name = request.query_params.get('model')
        if not model_name:
            # return all model names
            all_models = [m._meta.model_name for m in apps.get_models()]
            return Response({'models': all_models})
        
        # get model class dynamically
        try:
            model = apps.get_model('home', model_name)
        except LookupError:
            return Response({'error': 'Model not found'}, status=404)
        
        serializer_class = create_dynamic_serializer(model)
        queryset = model.objects.all()[:100]  # limit 100 records
        serializer = serializer_class(queryset, many=True)
        return Response(serializer.data)
