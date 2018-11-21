from rest_framework import serializers
from Profile.models import profileModel

class JSONSerializerField(serializers.Field):
    """ Serializer para JSONField -- requiere hacer el campo escribible """
    def to_internal_value(self, data):
        return data
    def to_representation(self, value):
        return value

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = profileModel
        fields = ('id', 'name')