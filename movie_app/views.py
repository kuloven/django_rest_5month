from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Director, Movie, Review
from .serializers import DirectorSerializer, MovieSerializer, ReviewSerializer



@api_view(['GET', 'POST'])
def director_list_api_view(request):
    if request.method == 'GET':
        directors = Director.objects.all()
        data = DirectorSerializer(directors, many=True).data
        return Response(data=data)
    elif request.method == "POST":
        name = request.data.get('name')
        directors = Director.objects.create(
            name = name
        )
        directors.save()


@api_view(['GET', 'PUT', 'DELETE'])
def director_detail_api_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'error': 'Movie not found!'})
    if request.method == 'GET':
        data = DirectorSerializer(director, many=False).data
        return Response(data=data)
    elif request.method == 'PUT':
        director.name=request.data.get('name')
        director.save()
        return Response(data=DirectorSerializer(director).data)
    elif request.method == 'DELETE':
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def movie_list_api_view(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        data = MovieSerializer(movies, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        title = request.data.get('title')
        description = request.data.get('description')
        duration = request.data.get('duration')
        director = request.data.get('director')
        reviews = request.data.get('reviews')
        ave_rating = request.data.get('ave_rating')
        movies = Movie.objects.create(
            title=title,
            description=description,
            duration=duration,
            director=director,
            reviews=reviews,
            ave_rating=ave_rating,
        )
        movies.save()



@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail_api_view(request, id):
    try:
        moviess = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'error': 'Movie not found!'})
    if request.method == 'GET':
        data = MovieSerializer(moviess, many=False).data
        return Response(data=data)
    elif request.method == 'PUT':
        moviess.title = request.data.get('title')
        moviess.description = request.data.get('description')
        moviess.duration = request.data.get('duration')
        moviess.director = request.data.get('director')
        moviess.reviews = request.data.get('reviews')
        moviess.ave_rating = (request.data.get('ave_rating'))
        moviess.save()
        return Response(status=status.HTTP_201_CREATED, data=MovieSerializer(Movie).data)
    elif request.method == 'DELETE':
        moviess.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET', 'POST'])
def review_list_api_view(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        data = ReviewSerializer(reviews, many=True).data
        return Response(status=status.HTTP_201_CREATED, data=data)
    elif request.method == 'POST':
        text = request.data.get('text')
        stars = request.data.get('stars')
        reviews = Review.objects.create(
            text=text,
            stars=stars,
        )
        reviews.save()

@api_view(['GET', 'PUT', 'DELETE'])
def review_detail_api_view(request, id):
    try:
        reviewss = Review.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'error': 'Movie not found!'})
    if request.method == 'GET':
        data = ReviewSerializer(reviewss, many=False).data
        return Response(data=data)
    elif request.method == 'PUT':
        reviewss.text = request.data.get('title')
        reviewss.stars = request.data.get('stars')
        reviewss.save()
        return Response(status=status.HTTP_201_CREATED, data=ReviewSerializer(Review).data)
    elif request.method == 'DELETE':
        reviewss.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

