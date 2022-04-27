# from rest_framework import generics
from rest_framework.renderers import JSONRenderer

from django_filters import rest_framework as filters
from rest_framework import filters as rest_framework_filters

from api.v1.filters import StudentFilter
from api.v1.pagination import StudentPagination
from api.v1.throttles import AnonStudentThrottle
from students.models import Student
from api.v1.serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework_xml.renderers import XMLRenderer

# class StudentsView(generics.ListCreateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#
#
# class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = StudentPagination
    filter_backends = (
        filters.DjangoFilterBackend,
        rest_framework_filters.OrderingFilter,
    )
    filterset_class = StudentFilter
    ordering_fields = ['id', 'age', 'first_name', 'last_name']
    throttle_classes = [AnonStudentThrottle]
    # renderer_classes = [JSONRenderer, XMLRenderer]

'''
First
1. Создать viewset для модели Teacher
2. Создать viewset для модели Group

Second
1. Создать модель для курса валют. (Privatbank, monobank, http://vkurse.dp.ua/, binance?)

First
1. Добавить сортировку и фильтры для Teachers and Groups
2. Фильтр по поиску для Students and Teachers link

Second
1. Создать ListView и показать все рейты.
2. Сохранить курс валют приватбанк в таблицу rate (model Rate).
   Создать в виде селери задачи.
   Запускать каждые 15 минут использую селерибит.
   
https://github.com/DmytroKaminskiy/currency_6/blob/main/app/currency/tasks.py
'''
