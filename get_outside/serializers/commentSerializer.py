from authentication.models import CustomUser
from get_outside.models.commentsModel import Comment
from rest_framework import serializers


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'profile_picture')


# Serializers define the API representation.
class CommentsSerializer(serializers.ModelSerializer):
    text = serializers.CharField(max_length=255)
    author = AuthorSerializer()

    class Meta:
        model = Comment
        fields = '__all__'
