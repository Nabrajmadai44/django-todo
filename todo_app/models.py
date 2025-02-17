from django.db import models

# Create your models here.
# create table todo(id int primary key auto_increament, title varchar(100));

# If there is any change in models.py, then run following commands:
# python manage.py makemigrations
# python  manage.py migrate


class Todo(models.Model): #PascalCase
    title = models.CharField(max_length= 100) #varchar, char
    
    def __str__(self):
        return self.title
