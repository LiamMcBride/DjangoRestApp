from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework import status
from rest_framework import permissions
from proj.models import Proj, Country, State
from .serializers import ProjSerializer, CountrySerializer, StateSerializer
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer


@api_view(('GET',))
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def statesByCountry(request, countryId):
    #return HttpResponse("<h1>" + str(countryId) + "</h1>")
    states = State.objects.filter(countryId=countryId)
    serializer = StateSerializer(states, many=True)
    
    return Response(serializer.data, status=status.HTTP_200_OK)
    #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CountryListApiView(APIView):
    def get(self,request,*args,**kwargs):
        country = Country.objects
        serializer = CountrySerializer(country, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self,request,*args,**kwargs):
        data = {
            'id' : request.data.get('id'), #here is where you make it update the id automatically
            'code' : request.data.get('code'),
            'name' : request.data.get('name'),
        }

        serializer = CountrySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @api_view(('GET',))
    #@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
    def statesById(request, countryId):
        
        # states = State.objects.filter(countryId= countryId)
        # serializer = StateSerializer(states, many=True)
        # return Response(serializer.data, status=status.HTTP_200_OK)
        #return HttpResponse("<h1>{}</h1>".format(countryId))
        state = State.objects.filter(countryId=countryId)
        serializer = StateSerializer(state, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

        

class StateListApiView(APIView):
    def get(self,request,*args,**kwargs):
        state = State.objects
        serializer = StateSerializer(state, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self,request,*args,**kwargs):
        data = {
            'id' : request.data.get('id'), #here is where you make it update the id automatically
            'code' : request.data.get('code'),
            'name' : request.data.get('name'),
            'countryId' : request.data.get('countryId'),
        }

        serializer = StateSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProjListApiView(APIView):
    def get(self,request, *args, **kwargs):
        projs = Proj.objects.filter(user = request.user.id)
        serializer = ProjSerializer(projs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self,request, *args, **kwargs):
        data = {
            'task': request.data.get('task'),
            'completed': request.data.get('completed'),
            'user': request.user.id,
        }

        serializer = ProjSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)