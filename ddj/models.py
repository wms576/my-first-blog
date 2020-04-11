from django.db import models

class Ddjw(models.Model):
    zjh=models.SmallIntegerField()
    zjw=models.TextField()

    def __str__(self):
        return str(self.zjh)+':'+self.zjw
