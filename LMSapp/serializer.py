from rest_framework import serializers

from LMSapp.models import Teacher


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'name', 'email', 'password','qualification', 'mobile_no', 'skills']


