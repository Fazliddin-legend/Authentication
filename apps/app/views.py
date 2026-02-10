from django.shortcuts import render
from .models import Item
from .serializer import ItemSerializer
from rest_framework import generics
from apps.users.permissions import IsOwner
from rest_framework.permissions import IsAuthenticated

class ItemCreateView(generics.CreateAPIView):
  serializer_class = ItemSerializer
  permission_classes = [IsAuthenticated]
  def perform_create(self, serializer):
    serializer.save(owner=self.request.user)

class ItemUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
  queryset = Item.objects.all()
  serializer_class = ItemSerializer
  permission_classes = [IsAuthenticated, IsOwner]