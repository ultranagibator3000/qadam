from rest_framework.generics import (
    CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView)
from rest_framework.permissions import IsAuthenticated

from apps.blogs.models import Blog
from apps.blogs.serializers import (
    BlogAssetsSerializer, BlogCreateUpdateSerializer, BlogListSerializer, BlogRetrieveSerializer)
from apps.blogs.pagination import BlogLimitOffsetPagination
from apps.blogs.permissions import IsAuthor


class BlogAssetsCreateAPIView(CreateAPIView):
    serializer_class = BlogAssetsSerializer
    permission_classes = (IsAuthenticated, )


class BlogCreateAPIView(CreateAPIView):
    serializer_class = BlogCreateUpdateSerializer
    permission_classes = (IsAuthenticated, )

    def perform_create(self, serializer):
        _author = self.request.user.profile
        serializer.save(author=_author)


class BlogListAPIView(ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogListSerializer
    pagination_class = BlogLimitOffsetPagination

    def get_queryset(self):
        search_query = self.kwargs["q"]
        return Blog.objects.filter(title__contains=search_query)


class BlogRetrieveAPIView(RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogRetrieveSerializer


class BlogUpdateAPIView(UpdateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogCreateUpdateSerializer
    permission_classes = (IsAuthenticated, IsAuthor)


class BlogDestroyAPIView(DestroyAPIView):
    queryset = Blog.objects.all()
    permission_classes = (IsAuthenticated, IsAuthor)
