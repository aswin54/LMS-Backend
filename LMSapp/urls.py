from django.urls import path

from LMSapp import views

urlpatterns = [
    path('teachers/',views.TeacherList.as_view()),
    path('teachers/<int:pk>/',views.TeacherDetail.as_view()),
    path('login_view/',views.login_view,name='login_view'),
]