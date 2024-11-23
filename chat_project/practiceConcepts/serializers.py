from django.contrib.auth.models import Group, User
from rest_framework import serializers
from .models import Book
from datetime import datetime, date

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'published_date', 'price']

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price must be greater than zero.")
        return value
    def validate_published_date(self, value):
        
        if value>date.today():
            raise serializers.ValidationError("Published date cannot be in the future.")
        return value