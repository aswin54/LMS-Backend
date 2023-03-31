from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, permissions

from LMSapp.models import Teacher
from LMSapp.serializer import TeacherSerializer


# Create your views here.
class TeacherList(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    # permission_classes = [permissions.IsAuthenticated]


class TeacherDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    # permission_classes = [permissions.IsAuthenticated]


@csrf_exempt
def login_view(request):
    email = request.POST['email']
    password = request.POST['password']
    teacherData = Teacher.objects.get(email=email, password=password)
    if teacherData:
        return JsonResponse({'bool': True})
    else:
        return JsonResponse({'bool': False})
