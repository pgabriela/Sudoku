from django.db import models


class Quiz(models.Model):
    solution = models.CharField(max_length=200)

    def __str__(self):
        return self.solution
