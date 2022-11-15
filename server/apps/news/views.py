from rest_framework.generics import (
    CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView)
from rest_framework.permissions import IsAuthenticated

from apps.news.models import News
from apps.news.serializers import NewsCreateUpdateSerializer, NewsListSerializer, NewsRetrieveSerializer


class NewsCreateAPIView(CreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsCreateUpdateSerializer
    permission_classes = (IsAuthenticated, )


class NewsListAPIView(ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsListSerializer

    def get_queryset(self):
        search_query = self.kwargs["q"]
        return News.objects.filter(title__contains=search_query) 


class NewsRetrieveAPIView(RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsRetrieveSerializer


class NewsUpdateAPIView(UpdateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsCreateUpdateSerializer
    permission_classes = (IsAuthenticated, )


class NewsDestroyAPIView(DestroyAPIView):
    queryset = News.objects.all()
    permission_classes = (IsAuthenticated, )
