from rest_framework import serializers
import user.models as models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User