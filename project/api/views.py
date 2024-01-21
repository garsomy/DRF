from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Posts
from .serializers import PostsSerializer


class PostsView(ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer


@api_view(['GET'])
def postsList(request):
    posts = Posts.objects.all()
    serializer = PostsSerializer(posts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def postGet(request, pk):
    post = Posts.objects.all(pk=pk)
    serializer = PostsSerializer(post)
    return Response(serializer.data)


@api_view(['DELETE'])
def postDel(request, pk):
    post = Posts.objects.all(pk=pk)
    post.delete()
    return Response('Post deleted')


@api_view(['POST'])
def postCreate(request):
    serializer = PostsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['PUT'])
def postPut(request, pk):
    post = Posts.objects.all(pk=pk)
    serializer = PostsSerializer(data=request.data, instance=post)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['PATCH'])
def postPatch(request, pk):
    post = Posts.objects.all(pk=pk)
    serializer = PostsSerializer(data=request.data, instance=post, partial=True)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)