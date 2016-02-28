from django.contrib.auth.models import User
from .models import Page
from .serializers import PageSerializer, UserSerializer
from rest_framework import viewsets, permissions


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class PageViewSet(viewsets.ModelViewSet):
    # TODO: Allow only the author of a page or a superuser to modify a page.
    # TODO: Allow users to see their own unpublished pages.

    queryset = Page.objects.filter(status='published')
    serializer_class = PageSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


