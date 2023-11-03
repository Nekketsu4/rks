from rest_framework import generics
from django.db.models.functions import Concat
from django.db.models import F, Value, ExpressionWrapper, CharField

from .models import Album
from .serializers import MultimediaSerializer


class MultimediaListView(generics.ListAPIView):
    serializer_class = MultimediaSerializer

    def get_queryset(self):

        sorting = self.request.query_params.get('sorting', None)

        queryset = Album.objects.all().annotate(
            alb=ExpressionWrapper(Concat(F('name'), Value('['), F('year'), Value(']')), CharField()),
            artist_name=Concat(F('artist__name'), Value('@'), F('name')))
        if sorting is not None:
            queryset = queryset.order_by(sorting)

        return queryset