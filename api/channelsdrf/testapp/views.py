from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from testapp.models import Animal
from testapp.serializers import AnimalSerializer

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

# Create your views here.

@csrf_exempt
def animals(request):
    if request.method == 'GET':
        animals = Animal.objects.all()
        serializer = AnimalSerializer(animals, many=True)
        return JsonResponse(serializer.data, safe=False) 
    
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AnimalSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            send_message(serializer.data)
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

def send_message(animal):
    layer = get_channel_layer()
    async_to_sync(layer.group_send)('test', {
        'type': 'test.message',
        'message': animal
    })