from django.http import HttpResponse
from django.shortcuts import HttpResponseRedirect, get_object_or_404
from rest_framework import permissions, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from authentication.models import CustomUser
from get_outside.serializers.commentSerializer import CommentsSerializer, CommentsPostSerializer
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

from get_outside.models.commentsModel import Comment


# ViewSets define the view behavior.
class CommentsViewSet(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        pin_id = request.data.get('mappointID')  # pin id
        text = request.data.get('text')
        data = {
            'mappointPin': pin_id,
            'text': text,
            'author': request.user.uuid,
        }
        serializer = CommentsPostSerializer(data=data)
        if serializer.is_valid():
            comment = serializer.save()  
            if comment:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        comment = get_object_or_404(Comment, uuid=pk)
        userCreatedComment = comment.author_id
        user_id = self.request.user.uuid
        if user_id == userCreatedComment:
            comment.delete()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    def get(self, request, pk):
        comment = Comment.objects.filter(mappointPin=pk)
        serializer = CommentsSerializer(comment, many=True)
        if comment:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({}, status=status.HTTP_200_OK)
