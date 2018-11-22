from rest_framework import serializers
from Test1.models import testModel

class Test1Serializer(serializers.ModelSerializer):
    class Meta:
        model = testModel
        fields = ('__all__')