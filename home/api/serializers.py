from rest_framework import serializers

class JsonRPCSerializer(serializers.Serializer):
    jsonrpc = serializers.CharField()
    method = serializers.CharField()
    params = serializers.DictField()
    id = serializers.IntegerField()



def create_dynamic_serializer(model):
    """
    Returns a read-only serializer for any model.
    """
    class DynamicSerializer(serializers.ModelSerializer):
        class Meta:
            model = model
            fields = '__all__'
            read_only_fields = '__all__'
    return DynamicSerializer