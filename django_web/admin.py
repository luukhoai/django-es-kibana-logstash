from django.contrib import admin
from .models import BlogPost
from elasticsearch_dsl.connections import connections

connections.create_connection()

admin.site.register(BlogPost)