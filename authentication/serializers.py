
from authentication.models import Coders
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coders
        fields = "__all__"

