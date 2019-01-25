from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class PostsView(ListAPIView):
    authentication_class = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)
