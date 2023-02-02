from django.urls import path
from get_outside.views.mappointView import MappointViewSet, RatingViewSet, MappointImageView
from get_outside.views.categoryView import CategoryViewSet, CategoryViewSet2, CategoryGetViewSet
from get_outside.views.favoritesView import FavoritePinView
from get_outside.views.commentsView import CommentsViewSet

urlpatterns = [
    path('category', CategoryViewSet.as_view()),
    path('category/public', CategoryGetViewSet.as_view()),
    path('category/<str:pk>', CategoryViewSet2.as_view()),

    path('mappoint', MappointViewSet.as_view()),
    path('mappoint/<str:pk>', MappointViewSet.as_view()),
    path('mappoint/upload/', MappointImageView.as_view()),

    path('rating/mappoint', RatingViewSet.as_view()),
    path('rating/mappoint/<str:pk>', RatingViewSet.as_view()),
    # path('rating/mappoint/<int:pk>', RatingViewSet.as_view()),

    path('favorites/pin/', FavoritePinView.as_view(), name='favoritePin'),

    path('mappoint/detail/comments/<str:pk>', CommentsViewSet.as_view()),
    path('mappoint/detail/comments', CommentsViewSet.as_view()),
]
