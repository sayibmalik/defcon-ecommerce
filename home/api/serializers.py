from rest_framework import serializers

class JsonRPCSerializer(serializers.Serializer):
    jsonrpc = serializers.CharField()
    method = serializers.CharField()
    params = serializers.DictField()
    id = serializers.IntegerField()
