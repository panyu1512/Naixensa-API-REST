from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Events
from rest_framework import status
from . serializers import EventsSerializer


@api_view(['POST'])
@permission_classes([IsAdminUser])
def create_event(request):
    data = request.data
    event = Events.objects.create(
        title=data['title'],
        description=data['description'],
        date=data['date'],
    )
    serializer = EventsSerializer(event, many=False)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_events(request):
    events = Events.objects.all()
    serializer = EventsSerializer(events, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_event(request, pk):
    event = Events.objects.get(id=pk)
    serializer = EventsSerializer(event, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAdminUser])
def update_event(request, pk):
    data = request.data
    event = Events.objects.get(id=pk)
    event.title = data['title']
    event.description = data['description']
    event.date = data['date']
    event.save()
    serializer = EventsSerializer(event, many=False)
    return Response(serializer.data)

@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def delete_event(request, pk):
    event = Events.objects.get(id=pk)
    event.delete()
    return Response('Event deleted')

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def register_assistant(request, pk):
    event = Events.objects.get(id=pk)
    user = request.user
    event.assistants.add(user)
    return Response('User registered')

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unregister_assistant(request, pk):
    event = Events.objects.get(id=pk)
    user = request.user
    event.assistants.remove(user)
    return Response('User unregistered')

