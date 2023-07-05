from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()

class user_details(models.Model):
    name = models.CharField(default='name', max_length=255)
    dob = models.DateField()
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default='Gender')
    SEMESTER_CHOICES = (
        ('Semester 1', 'Semester 1'),
        ('Semester 2', 'Semester 2'),
        ('Semester 3', 'Semester 3'),
        ('Semester 4', 'Semester 4'),
        ('Semester 5', 'Semester 5'),
        ('Semester 6', 'Semester 6'),
        ('Semester 7', 'Semester 7'),
        ('Semester 8', 'Semester 8'),
    )
    semester = models.CharField(max_length=10, choices=SEMESTER_CHOICES)
    
    BRANCH_CHOICES = (
        ('CSE', 'CSE'),
        ('AIE', 'AIE'),
        ('EEE', 'EEE'),
        ('ECE', 'ECE'),
        ('ELC', 'ELC'),
        ('MECH', 'MECH'),
        ('BCA', 'BCA'),
        ('MCA', 'MCA'),
        ('MTECH', 'MTECH'),
        ('BCOM', 'BCOM'),
        ('MCOM', 'MCOM'),
        ('PHYSICS', 'PHYSICS'),
        ('CHEMISTRY', 'CHEMISTRY'),
        ('MATHS', 'MATHS'),
        ('MBBS', 'MBBS'),
        ('BAMS', 'BAMS'),
        ('BDS', 'BDS'),
    )
    branch = models.CharField(max_length=10, choices=BRANCH_CHOICES, default='branch')
    college_mail = models.EmailField(max_length=255, default='College mail')
    phone_num = models.CharField(max_length=20)
    address= models.TextField()
    
    def __str__(self):
        return self.college_mail     
