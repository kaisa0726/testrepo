from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=50,verbose_name = "入力してください")
    content = models.TextField()
    date = models.DateField()
    datetime = models.DateTimeField()
    boolen =  models.BooleanField(default = False)
    

    def __str__(self):
        return self.title


