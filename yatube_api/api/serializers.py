from django.contrib.auth import get_user_model
from posts.models import Comment, Group, Post, Follow
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator


User = get_user_model()

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = Comment


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
        default=serializers.CurrentUserDefault(),
    )

    following = serializers.SlugRelatedField(
        slug_field='username',
        default=serializers.CurrentUserDefault(),
        queryset = User.objects.all(),
    )


    class Meta:
        fields = '__all__'
        model = Follow
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('user', 'following'),
                message=('Разрешена только однократная подписка на автора!'),
            ),
        ]

    def validate_following(self, data):
#        if self.context['request'].user == data['following']:
#            raise serializers.ValidationError(
#                'Подписка на самого себя запрещена')
#        return data
#        if data['color'] == data['name']:
#            raise serializers.ValidationError(
#                'Нельзя подписаться на самого себя!')
        print('self=', self.context.get('request').user)
        print('data=', data['following'])
        return data 