from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Movie, Review, Genre
from django.contrib.auth import get_user_model
import jwt
from django.conf import settings
from .serializers import MovieListSerializer, MovieSerializer, ReviewListSerializer, ReviewSerializer
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

# Create your views here.
@api_view(['GET'])
def movies(request):
    movie_list = get_list_or_404(Movie)
    serializer = MovieSerializer(movie_list, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def reviews(request, movie_pk):
    if request.method == 'GET':
        review_list = Review.objects.all().filter(movie_id=movie_pk)
        serializer = ReviewListSerializer(review_list, many=True)
        return Response(serializer.data)

    else:
        serializer = ReviewListSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            movie = get_object_or_404(Movie, pk=request.data.get('movie'))

            pre_point = movie.vote_average * movie.vote_count
            
            point = pre_point+int(request.data.get('rank'))
            count = movie.vote_count + 1
            new_vote_average = round(point/count, 2)

            movie.vote_average = new_vote_average
            movie.vote_count = count
            movie.save()
            # print(request.user)
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def my_review(request, my_pk):
    if request.method == 'GET':
        review_list = Review.objects.all().filter(user_id=my_pk)
        serializer = ReviewListSerializer(review_list, many=True)
        return Response(serializer.data)



# authentication_classes 붙여줘야함!
@api_view(['PUT', 'DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def review_update_delete(request, review_pk):
  review = get_object_or_404(Review, pk=review_pk)
  if not request.user.reviews.filter(pk=review_pk).exists():
    return Response({'message': '권한이 없습니다.'})

  if request.method == 'PUT':
    serializer = ReviewListSerializer(review, data=request.data)
    

    # if serializer.is_valid(raise_exception=True):
    if serializer.is_valid(raise_exception=True):
      movie = get_object_or_404(Movie, pk=request.data.get('movie'))
      pre_point = movie.vote_average * (movie.vote_count - 1)
      point = pre_point+int(request.data.get('rank'))
      count = movie.vote_count
      new_vote_average = round(point/count, 2)
      movie.vote_average = new_vote_average
      movie.vote_count = count
      movie.save()
      serializer.save(user=request.user)
      return Response(serializer.data)

  else:
    review = get_object_or_404(Review, pk=review_pk)
    # token = request.headers['Authorization'].split()[1]
    # SECRET_KEY = settings.SECRET_KEY
    # print(token)
    # 디코드하려면 재료 3개
    # payload = jwt.decode(token,SECRET_KEY,algorithms=['HS256'])
    # print(payload['user_id'])
    movie = get_object_or_404(Movie, pk=review.movie_id)
    pre_point = movie.vote_average * (movie.vote_count)
    # pre_count = movie.vote_count
    point = pre_point - review.rank
    count = movie.vote_count-1
    new_vote_average = round(point/count, 2)
    movie.vote_average = new_vote_average
    movie.vote_count = count
    movie.save()
    # print(request.user) 익명으로 안받아와짐 그래서 토큰으로 받아줌
    review.delete()
    return Response({ 'id': review_pk })


@api_view(['POST'])
def recommend(request):
    me_like = request.data.get('me_like')

    # 인기순
    favorite_movies = Movie.objects.all().order_by('-vote_average')[:10]
    favorite_serialize = MovieSerializer(favorite_movies, many=True)
    # 리뷰 기반 장르기반 추천
    user_movies_review = []
    # 배우기반 추천
    user_movies_actor = []
    # 감독기반 추천
    user_movies_director = []
    # 개봉년도
    # 제작 국가
    # 리뷰 기반 장름별
    reviews = Review.objects.all()
    for review in reviews:
        movie = Movie.objects.get(pk=review.movie_id)
        if not movie in user_movies_review:
            user_movies_review.append(movie)

    # 좋아요 기반추천
    my_user_like_movies = []
    user_like_movies = []
    # 좋아요 기반 추천
    like_movies = request.data.get('like_movies')
    for like_movie in like_movies:
        movie = get_object_or_404(Movie, pk=like_movie)
        if not movie in my_user_like_movies:
            my_user_like_movies.append(movie)
    # 내가 좋아요 한 것 제거
    for like_movie in my_user_like_movies:
        # print(me_like)
        if like_movie.id not in me_like:
            user_like_movies.append(like_movie)
    # print(user_like_movies)
            
    
    # user_genre_serialize = MovieSerializer(user_movies_review, many=True)
    user_like_serialize = MovieSerializer(user_like_movies, many=True)
    
    # 연령대
    user_movies_age = []
    # 연령별 기반 추천
    me_age = request.data.get('me_age')
    for age in me_age:
        movie = get_object_or_404(Movie, pk=age)
        if not movie in user_movies_age:
            user_movies_age.append(movie)

    user_movies_age_serializer = MovieSerializer(user_movies_age, many=True)
    return Response([favorite_serialize.data, user_like_serialize.data, user_movies_age_serializer.data])

@api_view(['POST'])
# @authentication_classes([JSONWebTokenAuthentication])
# @permission_classes([IsAuthenticated])
def my_movie_like(request, my_pk):
    me = get_object_or_404(get_user_model(), pk=my_pk)
    # print(me)
    data = []
    movies = request.data
    for movie_pk in movies:
        movie = get_object_or_404(Movie, pk=movie_pk)
        serializer = MovieSerializer(movie)
        data.append(serializer.data)
    
    return Response(data)

@api_view(['POST'])
def my_movie_dislike(request, my_pk):
    me = get_object_or_404(get_user_model(), pk=my_pk)
    # print(me)
    data = []
    movies = request.data
    for movie_pk in movies:
        movie = get_object_or_404(Movie, pk=movie_pk)
        serializer = MovieSerializer(movie)
        data.append(serializer.data)
    
    return Response(data)
    
@api_view(['POST'])
def my_movie_wish(request, my_pk):
    me = get_object_or_404(get_user_model(), pk=my_pk)
    # print(me)
    data = []
    movies = request.data
    for movie_pk in movies:
        movie = get_object_or_404(Movie, pk=movie_pk)
        serializer = MovieSerializer(movie)
        data.append(serializer.data)
    
    return Response(data)

@api_view(['POST'])
def movie_like(request, my_pk, movie_title):
  movie = get_object_or_404(Movie, title=movie_title)
  me = get_object_or_404(get_user_model(), pk=my_pk)
  if me.like_movies.filter(pk=movie.pk).exists():
      me.like_movies.remove(movie.pk)
      liking = False
      
  else:
      me.like_movies.add(movie.pk)
      liking = True
  
  return Response(liking)

@api_view(['POST'])
def movie_dislike(request, my_pk, movie_title):
  movie = get_object_or_404(Movie, title=movie_title)
  me = get_object_or_404(get_user_model(), pk=my_pk)
  if me.dislike_movies.filter(pk=movie.pk).exists():
      me.dislike_movies.remove(movie.pk)
      disliking = False
      
  else:
      me.dislike_movies.add(movie.pk)
      disliking = True
  
  return Response(disliking)

@api_view(['POST'])
def movie_wish(request, my_pk, movie_title):
  movie = get_object_or_404(Movie, title=movie_title)
  me = get_object_or_404(get_user_model(), pk=my_pk)
  if me.wish_movies.filter(pk=movie.pk).exists():
      me.wish_movies.remove(movie.pk)
      wishing = False
      
  else:
      me.wish_movies.add(movie.pk)
      wishing = True
  
  return Response(wishing)

@api_view(['POST'])
def like_movie_users(request, my_pk):
  # print(request.data)
  users = []
  movies = request.data.get('movies')

  for movie in movies:
    movie = get_object_or_404(Movie, pk=movie)
    serializer = MovieSerializer(movie)

    for user in serializer.data.get('like_users'):
      if user not in users:
        users.append(user)
    
  return Response(users)

@api_view(['POST'])
def dislike_movie_users(request, my_pk):
  # print(request.data)
  users = []
  movies = request.data.get('movies')

  for movie in movies:
    movie = get_object_or_404(Movie, pk=movie)
    serializer = MovieSerializer(movie)

    for user in serializer.data.get('dislike_users'):
      if user not in users:
        users.append(user)
    
  return Response(users)

@api_view(['POST'])
def wish_movie_users(request, my_pk):
  # print(request.data)
  users = []
  movies = request.data.get('movies')

  for movie in movies:
    movie = get_object_or_404(Movie, pk=movie)
    serializer = MovieSerializer(movie)

    for user in serializer.data.get('wish_users'):
      if user not in users:
        users.append(user)
    
  return Response(users)