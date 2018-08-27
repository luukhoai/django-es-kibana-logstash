import logging
from django.http import HttpResponse
from .models import BlogPost
from rest_framework import generics
from .serializers import BlogpostSerializer

logger = logging.getLogger('django_web')


def index(request):
    logger.info('Hello world')
    return HttpResponse('Hello World')


class BlogPostList(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogpostSerializer


class BlogPostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogpostSerializer