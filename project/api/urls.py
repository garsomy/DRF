from django.urls import path
from rest_framework import routers
from .views import *

urlpatterns = [
    path('', PostsView.as_view({'get': 'list', 'post': 'create'})),
    path('posts/', postsList),
    path('posts/<int:pk>/', postGet),
    path('postsdel/<int:pk>/', postDel),
    path('postsadd/', postCreate),
    path('postsput/<int:pk>', postPut),
    path('postspatch/<int:pk>', postPatch),
]