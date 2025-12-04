from rest_framework import serializers

class JsonRPCSerializer(serializers.Serializer):
    jsonrpc = serializers.CharField()
    method = serializers.CharField()
    params = serializers.DictField()
    id = serializers.IntegerField()



def create_dynamic_serializer(model_class):
    class DynamicSerializer(serializers.ModelSerializer):
        class Meta:
            model = model_class
            fields = '__all__'
            read_only_fields = [field.name for field in model_class._meta.fields]  # <-- fix
    return DynamicSerializer

class registerSerializer(serializers.Serializer):
    name = serializers.CharField()
    email = serializers.CharField()
    password = serializers.CharField()