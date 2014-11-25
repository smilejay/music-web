from rest_framework import serializers
import music.models as models


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Song


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ('id', 'name')
