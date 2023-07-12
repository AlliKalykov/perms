from rest_framework import serializers
from .models import Movie, Saloon, Ticket
from django.contrib.auth.models import User


class MovieSerializer(serializers.ModelSerializer):  # create class to serializer model
    creator = serializers.ReadOnlyField(source='creator.username')

    class Meta:
        model = Movie
        fields = ('id', 'title', 'genre', 'year', 'creator')


class UserSerializer(serializers.ModelSerializer):  # create class to serializer user model
    movies = serializers.PrimaryKeyRelatedField(many=True, queryset=Movie.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'movies')


class SaloonSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Saloon
        fields = '__all__'


class TicketSerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source='creator.username')

    class Meta:
        model = Ticket
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at', 'creator', 'id')
