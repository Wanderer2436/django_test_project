from django.db import models


class Department(models.Model):
    name = models.CharField('Название', max_length=15)

    class Meta:
        ordering = ['-name']
        verbose_name = 'Кафедра'
        verbose_name_plural = 'Кафедры'

    def __str__(self):
        return self.name


class Curator(models.Model):
    first_name = models.CharField('Имя', max_length=15)
    second_name = models.CharField('Фамилия', max_length=15)
    department = models.ForeignKey('core.Department', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        ordering = ['-first_name']
        verbose_name = 'Куратор'
        verbose_name_plural = 'Кураторы'

    def __str__(self):
        return self.second_name


class Students(models.Model):
    first_name = models.CharField('Имя', max_length=15)
    second_name = models.CharField('Фамилия', max_length=15)
    cource_num = models.IntegerField('Курс')
    direction = models.CharField('Направление', max_length=15)
    curator = models.ForeignKey('core.Curator', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        ordering = ['-first_name']
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'

    def __str__(self):
        return self.second_name
