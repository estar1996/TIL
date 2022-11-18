from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer
from django.contrib.auth import get_user_model
import urllib


@api_view(['POST'])
def signup(request):
	#1-1. Client에서 온 데이터를 받아서
    password = request.data.get('password')
    password_confirmation = request.data.get('passwordConfirmation')
		
	#1-2. 패스워드 일치 여부 체크
    if password != password_confirmation:
        return Response({'error': '비밀번호가 일치하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)
		
	#2. UserSerializer를 통해 데이터 직렬화
    serializer = UserSerializer(data=request.data)
    
	#3. validation 작업 진행 -> password도 같이 직렬화 진행
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        #4. 비밀번호 해싱 후 
        user.set_password(request.data.get('password'))
        user.save()
    # password는 직렬화 과정에는 포함 되지만 → 표현(response)할 때는 나타나지 않는다.
    return Response(serializer.data, status=status.HTTP_201_CREATED)

# code 요청
# @api_view(['GET'])
# def kakao_login(request):
#     app_rest_api_key = '061f19a9da5e194addf7f3d05a16f64c'
#     redirect_uri = "http://127.0.0.1:8000/accounts/login/kakao/callback"
#     return redirect(
#         f"https://kauth.kakao.com/oauth/authorize?client_id={app_rest_api_key}&redirect_uri={redirect_uri}&response_type=code"
#     )
    
    
# # access token 요청
# @api_view(['GET'])
# def kakao_callback(request):                                                                  
#     params = urllib.parse.urlencode(request.GET)                                      
#     return redirect(f'http://127.0.0.1:8000/accounts/login/kakao/callback?{params}') 



# @api_view(['GET'])
# def profile(request, username):
#     user = get_object_or_404(UserMovie, pk=request.data.get('user_pk'))
#     serializer = UserMovieSerializer(user)
#     return Response(serializer.data)


@api_view(['POST'])
def my_profile(request):
    user = get_object_or_404(get_user_model(), pk=request.data.get('user_id'))
    serializer = UserSerializer(user)
    return Response(serializer.data)


@api_view(['POST'])
def users_info(request):
    # print(request.data)
    users = request.data.get('users')
    movies = []
    ages = []
    for user in users:
        user = get_object_or_404(get_user_model(), pk=user)
        serializer = UserSerializer(user)
        age = serializer.data.get('age')
        like_movies = serializer.data.get('like_movies')
        dislike_movies = serializer.data.get('dislike_movies')
        wish_movies = serializer.data.get('wish_movies')
        watched_movies = serializer.data.get('watched_movies')
        for movie in like_movies:
            if movie not in movies:
                movies.append(movie)
            # 연령별 추천
            if age==user.age and movie not in ages:
                ages.append(movie)
    return Response([movies, ages])