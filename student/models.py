from django.db import models


class Student(models.Model):
    first_name = models.TextField(verbose_name='First name', max_length=20)
    last_name = models.TextField(verbose_name='Last name', max_length=20)
    date_of_birth = models.DateField(verbose_name='DOB')
    email = models.EmailField()
    phone_no = models.IntegerField()
    classroom = models.ForeignKey('ClassRoom', on_delete=models.CASCADE, default=None)

class ClassRoom(models.Model):
    room_no = models.IntegerField()
    staff = models.ManyToManyField('Staff', blank=True)

class Staff(models.Model):
    first_name = models.TextField(verbose_name='First name', max_length=20)
    last_name = models.TextField(verbose_name='Last name', max_length=20)
    date_of_birth = models.DateField(verbose_name='DOB')
    email = models.EmailField()
    phone_no = models.IntegerField()

class Subject(models.Model):
    name = models.TextField(verbose_name='subject name', max_length=20)
    staff = models.ForeignKey('Staff', on_delete=models.CASCADE, default=None)

class Marks(models.Model):
    subject = models.ForeignKey('Subject',on_delete=models.CASCADE, default=None)
    student = models.ForeignKey('Student',on_delete=models.CASCADE, default=None)
    marks = models.IntegerField()

