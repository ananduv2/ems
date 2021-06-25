from django.db import models
import datetime

# Create your models here.

DEPARTMENT=(
    ('INTERNS','INTERNS'),
    ('BACKEND_DEVELOPER','BACKEND_DEVELOPER'),
    ('FRONTEND_DEVELOPER','FRONTEND_DEVELOPER'),
    ('DESIGNER','DESIGNER'),
    ('HR','HR'),
    ('MARKETING','MARKETING'),
    ('ADMINISTRATOR','ADMINISTRATOR')
)

class employee(models.Model):
    name =models.CharField(max_length=100)
    email = models.EmailField(max_length=300)
    mobile=models.IntegerField(null=True)
    dob=models.DateField(null=True)
    doj=models.DateField(default=datetime.date.today)
    department=models.CharField(max_length=50,choices=DEPARTMENT,default="INTERNS")


    def __str__(self):
        return self.name
