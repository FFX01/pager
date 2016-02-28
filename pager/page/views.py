from django.contrib.auth.models import User
from .models import Page
from .serializers import PageSerializer, UserSerializer
from rest_framework import viewsets, permissions


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class PageViewSet(viewsets.ModelViewSet):
    # TODO: Check how this actually works.
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


