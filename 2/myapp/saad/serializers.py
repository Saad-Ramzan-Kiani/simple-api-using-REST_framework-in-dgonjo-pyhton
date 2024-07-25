# saad/serializers.py
from rest_framework import serializers
from .models import YourModel  # Replace YourModel with your actual model

class YourModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = YourModel
        fields = '__all__'  # or specify the fields you want to include
