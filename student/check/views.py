from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from check.models import Student
from check.models import Student_check
from .serializers import *
from .kakaosend import send_kakao
from datetime import datetime
# Create your views here.


# @csrf_exempt
# def check(request):
#     if request.method == 'GET':
#         num = request.GET.get('violence',None)
#         reg_student = Student.objects.filter(id=num)
#         time = str(datetime.now())[:-10]
#         if reg_student.exists():

#             text = reg_student[0].name+' 학생이 '+time+'에 등원했습니다'
#             print(text)
#             obj = Student_check(st_id=reg_student[0],name=reg_student[0].name)
#             obj.save()
#             try:
#                 send_kakao(text, reg_student[0].phone)
#             except Exception as e:
#                 print('전송오류',e)
#                 return JsonResponse({'name': '전송실패', 'phone': '전송오류'})
#             response = StudentSerializer(reg_student[0])
#             return JsonResponse(response.data, safe=False)
#         return JsonResponse({'name': '출석실패', 'phone': '학생없음'})
@csrf_exempt
def check(request):
    if request.method == 'GET':
        num = request.GET.get('violence',None)
        time = str(datetime.now())[:-10]


        text = time+' 폭력발생!!'
        print(text)

        try:
            send_kakao(text, '01048760864')
        except Exception as e:
            print('전송오류',e)
            return JsonResponse({'name': '전송실패', 'phone': '전송오류'})

        return JsonResponse({'name': '전송성공', 'phone': 'sucesse'})

