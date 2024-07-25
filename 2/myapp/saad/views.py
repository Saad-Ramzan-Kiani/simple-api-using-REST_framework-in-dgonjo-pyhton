from django.shortcuts import render, HttpResponse
from rest_framework import viewsets
from .models import YourModel  # Replace YourModel with your actual model
from .serializers import YourModelSerializer

# Create your views here.
def home(request):
    return HttpResponse("hello world, this is home page")


class YourModelViewSet(viewsets.ModelViewSet):
    queryset = YourModel.objects.all()
    serializer_class = YourModelSerializer
