from django.db import models


class Students(models.Model):
    first_name = models.CharField('Имя', max_length=15)
    second_name = models.CharField('Фамилия', max_length=15)
    cource_num = models.IntegerField('Курс')
    direction = models.CharField('Направление', max_length=15)

    def __str__(self):
        return self.first_name
