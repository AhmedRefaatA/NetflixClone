from rest_framework import serializers
from netflix.models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'story', 'poster', 'video', 'rate', 'categories', 'classification']


class MovieSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'