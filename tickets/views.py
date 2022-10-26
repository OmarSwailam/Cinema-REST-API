from django.http import Http404
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import filters, status
from rest_framework.views import APIView
from rest_framework import generics, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *


def no_rest(request):
    if request.method == 'GET':
        guests = Guest.objects.all()
        serializer = GuestSerializer(guests, many=True)
        return JsonResponse(serializer.data, safe=False)
   

# function based views
@api_view(['GET', 'POST'])
def fbv_list(request):
    if request.method == 'GET':
        guests = Guest.objects.all()
        serializer = GuestSerializer(guests, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = GuestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def fbv_pk(request, pk):
    try:
        guest = Guest.objects.get(pk=pk)
    except Guest.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = GuestSerializer(guest)
        return Response(serializer.data)
    elif request.method == 'PUT':   
        serializer = GuestSerializer(guest, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        guest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# class based views
class CbvList(APIView):
    
    def get(self, request):
        guests = Guest.objects.all()
        serializer = GuestSerializer(guests, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = GuestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    
class CbvPk(APIView):

    def get_object(self, pk):
        try:
            return Guest.objects.get(pk=pk)
        except Guest.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        guest = self.get_object(pk=pk)
        serializer = GuestSerializer(guest)
        return Response(serializer.data)
    
    def put(self, request, pk):
        guest = self.get_object(pk=pk)
        serializer = GuestSerializer(guest ,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        guest = Guest.objects.get(pk=pk)
        guest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Generics
class generics_list(generics.ListCreateAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer
    authentication_classes = [TokenAuthentication]


class generics_pk(generics.RetrieveUpdateDestroyAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer
    authentication_classes = [TokenAuthentication]



# viewsets
class viewsets_guest(viewsets.ModelViewSet):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer

class viewsets_movie(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backend = [filters.SearchFilter]
    search_fields = ['movie']

class viewsets_reservation(viewsets.ModelViewSet):

    queryset = Reservation.objects.all()
    serializer_class = Reservation

# function based views for the project logic
@api_view(['GET'])
def find_movie(request):
    print("--------------------------")
    print(request.data)
    movies = Movie.objects.filter(    
        movie = request.data['movie'],
    )
    serializer = MovieSerializer(movies, many= True)
    return Response(serializer.data)

@api_view(['POST'])
def new_reservation(request):

    movie = Movie.objects.get(
        hall = request.data['hall'],
        movie = request.data['movie'],
    )
    
    try:
        guest = Guest.objects.get(name=request.data['name'], mobile=request.data['mobile'])
    except Guest.DoesNotExist:      
        guest = Guest(name=request.data['name'], mobile=request.data['mobile'])
        guest.save()

    try:
        reservation = Reservation.objects.get(guest=guest, movie=movie)
    except Reservation.DoesNotExist:
        reservation = Reservation(guest=guest, movie=movie)
        reservation.save()
        return Response(status=status.HTTP_201_CREATED)       
    return Response(status=status.HTTP_208_ALREADY_REPORTED)
