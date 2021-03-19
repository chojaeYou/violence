from rest_framework import serializers
from check.models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Student
        fields = ['name', 'phone']


