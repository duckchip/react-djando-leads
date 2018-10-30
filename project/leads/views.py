from django.shortcuts import render
from leads.models import Lead
from leads.serializers import LeadSerializer
from rest_framework import generics

class LeadListCreate(generics.ListCreateAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer

class LeadListUpdate(generics.UpdateAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer

class LeadListDelete(generics.DestroyAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer