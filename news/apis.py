from django.db.models import Q
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import News
from .pagination import StandardResultsSetPagination
from .permissions import WasSynced
from .serializers import NewsCreateSerializer


class NewsList(ListCreateAPIView):
    """

        GET /
        POST /

        This endpoint by default returns all news Item from the DB

        search <url>?search=<query>
        query text

        filter <url>?filter=<query>
        query type
    """
    queryset = News.objects.all()
    serializer_class = NewsCreateSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.query_params.get('search')
        filter = self.request.query_params.get('filter')

        if filter:
            queryset = queryset.filter(type=filter)
        if search:
            queryset = queryset.filter(Q(text__icontains=search))

        return queryset


class NewsRetrieveUpdateDelete(RetrieveUpdateDestroyAPIView):
    """
        Retrieve, Update & Delete News
        GET, PUT, PATCH & DELETE /detail/<int:pk>/
        param pk -- news id
    """
    serializer_class = NewsCreateSerializer
    lookup_url_kwarg = 'id'
    queryset = News.objects.all()
    permission_classes = [WasSynced]


