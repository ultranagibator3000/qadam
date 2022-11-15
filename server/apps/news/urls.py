from django.urls import path, re_path

from apps.news.views import (NewsCreateAPIView, NewsListAPIView,
                             NewsRetrieveAPIView, NewsUpdateAPIView, NewsDestroyAPIView)

urlpatterns = [
    path('news/', NewsCreateAPIView.as_view(), name="news-create"),
    re_path(r'^news/(?P<q>[a-zA-Z]+)/$',
            NewsListAPIView.as_view(), name="news-list"),
    path('news/<int:pk>/', NewsRetrieveAPIView.as_view(), name="news-detail"),
    path('news/<int:pk>/', NewsUpdateAPIView.as_view(), name="news-update"),
    path('news/<int:pk>/', NewsDestroyAPIView.as_view(), name="news-delete"),
]
