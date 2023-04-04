from django.db import models


# Create your models here.
class Teacher(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    qualification = models.CharField(max_length=50,null=True)
    mobile_no = models.CharField(max_length=50)
    skills = models.TextField()

    class Meta:
        verbose_name_plural = "1.Teachers"


class CourseCategory(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()

    class Meta:
        verbose_name_plural = "2.Course Categories"

    def __str__(self):
        return self.title

class Course(models.Model):
    category = models.ForeignKey(CourseCategory,on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()
    featured_img = models.ImageField(upload_to='course_img',null=True)
    technology = models.TextField(null=True)

    class Meta:
        verbose_name_plural = "3.Courses"

class Student(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    mobile_no = models.CharField(max_length=50)
    address = models.TextField()
    interested_categories = models.TextField()

    class Meta:
        verbose_name_plural = "4.Students"
