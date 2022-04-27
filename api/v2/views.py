# from rest_framework import generics
from rest_framework.renderers import JSONRenderer

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
    # renderer_classes = [JSONRenderer, XMLRenderer]

'''
First
1. Создать viewset для модели Teacher
2. Создать viewset для модели Group

Second
1. Создать модель для курса валют. (Privatbank, monobank, http://vkurse.dp.ua/, binance?)
'''