from django.shortcuts import get_object_or_404
from posts.models import Group, Post
from rest_framework import permissions, viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import filters

from .permissions import IsAuthorOrReadOnlyPermission
from .serializers import CommentSerializer, GroupSerializer, PostSerializer, FollowSerializer

from rest_framework import mixins


#class CreateRetrieveViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin,
#                            viewsets.GenericViewSet):
#    pass 


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    permission_classes = (
        IsAuthorOrReadOnlyPermission,
    #    permissions.IsAuthenticated,
    )
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        post_id = self.kwargs.get('pk')
        if post_id is not None:
            return Post.objects.filter(id=post_id)
        return Post.objects.select_related('author', 'group')

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (
        IsAuthorOrReadOnlyPermission,
    #    permissions.IsAuthenticated,
    )

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, pk=post_id)
        return post.comments.all()

    def perform_create(self, serializer):
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, pk=post_id)
        serializer.save(author=self.request.user, post=post)


class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('user__username', 'following__username')

    def get_queryset(self):
        return self.request.user.follower.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)