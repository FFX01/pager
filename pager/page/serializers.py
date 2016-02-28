from rest_framework import serializers
from .models import Page
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    # TODO: Include more safe user model fields

    class Meta:
        model = User
        fields = (
            'username',
        )


class PageSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Page
        fields = (
            'id',
            'title',
            'slug',
            'meta_description',
            'author',
            'status',
            'parent',
            'children',
            'content'
        )
