# Use of APIView
'''
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Poll, Choice
from .serializers import PollSerializer

class PollList(APIView):
    def get(self, request):
        polls = Poll.objects.all()[:20]
        data = PollSerializer(polls, many=True).data
        return Response(data)

class PollDetail(APIView):
    def get(self, request, pk):
        poll = get_object_or_404(Poll, pk=pk)
        data = PollSerializer(poll).data
        return Response(data)
'''

# Using DRF generic views to simplify code
from rest_framework import viewsets, generics, status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Poll, Choice, Vote
from .serializers import PollSerializer, ChoiceSerializer, VoteSerializer

# Poll ViewSet using ModelViewSet for full CRUD
class PollViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer

# Choice List tied to a specific Poll
class ChoiceList(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = Choice.objects.filter(poll_id=self.kwargs["pk"])
        return queryset
    serializer_class = ChoiceSerializer

# Custom Vote creation logic
class CreateVote(APIView):       
    def post(self, request, pk, choice_pk):
        voted_by = request.data.get("voted_by")
        data = {
            'choice': choice_pk,
            'poll': pk,
            'voted_by': voted_by
        }
        serializer = VoteSerializer(data=data)
        if serializer.is_valid():
            vote = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# We've used three different classes from rest_framework.generics.
# The names of the classes are representative of what they do:

# ListCreateAPIView: Get a list of entities, or create them. Allows GET and POST.
# RetrieveDestroyAPIView: Retrieve individual entity details, or delete the entity. Allows GET and DELETE.
# CreateAPIView: Allows creating entities, but not listing them. Allows POST.
