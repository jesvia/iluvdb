from django.urls import path, include
# from watchlist.API.views import movie_list, movie_details
from watchlist.API.views import WatchListAV, WatchDetailsAV,StreamPlatListAV, StreamPlatDetailsAV
urlpatterns = [
    # path('list/', movie_list, name='movie-list'),
    # path('<int:pk>', movie_details, name='movie-details'),
    path('list/', WatchListAV.as_view(), name='watch-list'),
    path('<int:pk>', WatchDetailsAV.as_view(), name='watch-details'),
    path('splist/', StreamPlatListAV.as_view(), name='sp-list'),
    path('splist/<int:pk>', StreamPlatDetailsAV.as_view(), name='sp-details')
]