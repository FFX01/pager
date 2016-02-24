from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Page


class PageSerializer(serializers.HyperlinkedModelSerializer):

    author = serializers.ReadOnlyField(
        source='author.username'
    )

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
