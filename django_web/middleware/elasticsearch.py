from django.utils.deprecation import MiddlewareMixin
from elasticsearch_dsl.connections import connections
from django_web.settings import ELASTICSEARCH_URL


class ElasticSearchMiddleWare(MiddlewareMixin):

    def process_request(self, request):
        request.es = connections.create_connection(hosts=[ELASTICSEARCH_URL])