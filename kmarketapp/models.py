from django.db import models

class UserRole(models.Model):
    Role = models.CharField(max_length=10)

    class Meta:
        db_table = 'userrole'

class Master(models.Model):
    UserRole = models.ForeignKey(UserRole, on_delete=models.CASCADE)
    Email = models.EmailField(unique=True)
    Password =models.CharField(max_length=12)
    isActive=models.BooleanField(default=False)
    DateCreated = models.DateTimeField(auto_now_add=True)
    DateModified = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'master'

gender_choices = (
    ('m', 'male'),
    ('f', 'female'),
)

class UserProfile(models.Model):
    Master = models.ForeignKey(Master, on_delete=models.CASCADE)
    ProfileImage = models.FileField(upload_to="profiles/", default='avatar.png')
    FullName = models.CharField(max_length=30, blank=True, default='')
    Gender = models.CharField(max_length=10, choices=gender_choices)
    Mobile = models.CharField(max_length=10, blank=True, default='')
    BirthDate = models.DateField(default="1990-01-01")
    Country = models.CharField(max_length=30, blank=True, default='')
    State = models.CharField(max_length=30, blank=True, default='')
    City = models.CharField(max_length=30, blank=True, default='')
    Address = models.CharField(max_length=30, blank=True, default='')

    class Meta:
        db_table = 'userprofile'