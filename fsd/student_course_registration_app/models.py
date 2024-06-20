from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    topic = models.CharField(max_length=100, default='') # Added default value for topic
    languages_used = models.CharField(max_length=100, default='')
    duration = models.CharField(max_length=100,default='')
    def  __str__ (self):
        return self.topic

class Student(models.Model):
    first_name = models.CharField(max_length=255, default='')
    last_name = models.CharField(max_length=255, default='')
    email = models.EmailField(unique=True, default='')
    courses = models.ManyToManyField(Course, related_name='students', blank=True)
    projects = models.ManyToManyField(Project, blank=True)
    def  __str__ (self):
        return f"{self.first_name} {self.last_name}"