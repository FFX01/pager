from django.contrib.auth.models import User
from .models import Page
from .serializers import PageSerializer
from rest_framework import viewsets, permissions


class PageViewSet(viewsets.ModelViewSet):

    queryset = Page.objects.all()
    serializer_class = PageSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


