from django.urls import path

from LMSapp import views

urlpatterns = [
    path('teachers/',views.TeacherList.as_view()),
    path('teachers/<int:pk>/',views.TeacherDetail.as_view()),
]