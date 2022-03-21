from django.test import TestCase, Client
from django.urls import reverse
from core import models


class StudentsModel(TestCase):

    def setUp(self):
        self.student = models.Students.objects.create(second_name='Петров', cource_num=3)

    def testStr(self):
        self.assertEqual(
            str(self.student),
            self.student.second_name,
            'Строковое представление объекта student должно быть равно значению атрубута second_name',
        )


class StudentSearchTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.student1 = models.Students.objects.create(second_name='Иванов', cource_num=1)
        self.student2 = models.Students.objects.create(second_name='Сидоров', cource_num=2)

    def testWithoutParams(self):
        response = self.client.get(reverse('core:students_list'))
        self.assertSequenceEqual(
            list(response.context['object_list']),
            list(models.Students.objects.all()),
            'При поиске без параметров должны выводиться все студенты',
        )

    def testSearchByName(self):
        response = self.client.get(reverse('core:students_list'), data={'second_name': 'Иванов', 'cource_num': 1})
        self.assertEqual(1, response.context['object_list'].count())
        self.assertEqual(
            'Иванов',
            response.context['object_list'].first().second_name,
        )


class CuratorSearchTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.curator1 = models.Curator.objects.create(second_name='Сергеев')
        self.curator2 = models.Curator.objects.create(second_name='Ерохин')

    def testWithoutParams(self):
        response = self.client.get(reverse('core:curators_list'))
        self.assertSequenceEqual(
            list(response.context['object_list']),
            list(models.Curator.objects.all()),
            'При поиске без параметров должны выводиться все кураторы',
        )

    def testSearchByName(self):
        response = self.client.get(reverse('core:curators_list'), data={'second_name': 'Сергеев'})
        self.assertEqual(1, response.context['object_list'].count())
        self.assertEqual(
            'Сергеев',
            response.context['object_list'].first().second_name,
        )
