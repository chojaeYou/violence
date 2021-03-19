from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from check.models import Student
from .serializers import *
# Create your views here.

@csrf_exempt
def check(request):
    if request.method=='POST':
        num=JSONParser().parse(request)['num']
        reg_student=Student.objects.filter(number=num)

        if reg_student.exists():
            print('출석!')
            response=StudentSerializer(reg_student[0])
            return JsonResponse(response.data,safe=False)
        return JsonResponse({'name':'출석실패','phone':'학생없음'})
