from django.urls import path
from get_outside.views.mappointView import MappointViewSet, UploadImage
from get_outside.views.categoryView import CategoryViewSet, CategoryViewSet2
from get_outside.views.favoritesView import FavoritePinView
from get_outside.views.commentsView import CommentsViewSet

urlpatterns = [
    path('category', CategoryViewSet.as_view()),
    path('category/<int:pk>', CategoryViewSet2.as_view()),

    path('mappoint', MappointViewSet.as_view()),
    path('mappoint/<int:pk>', MappointViewSet.as_view()),
    path('mappoint/upload/<int:pk>', UploadImage.as_view()),

    path('favorites/pin/', FavoritePinView.as_view(), name='favoritePin'),
    path('mappoint/details/comments/<pk>', CommentsViewSet.as_view()),
    path('mappoint/details/comments', CommentsViewSet.as_view()),
]
