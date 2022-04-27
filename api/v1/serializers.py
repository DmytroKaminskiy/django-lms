from rest_framework import serializers

from groups.models import Group
from students.models import Student


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'name')


class StudentSerializer(serializers.ModelSerializer):
    group_obj = GroupSerializer(read_only=True, source='group')

    class Meta:
        model = Student
        fields = (
            'id',
            'first_name',
            'last_name',
            'age',
            'group_obj',
            # 'enroll_date',
        )
        # extra_kwargs = {
        #     'enroll_date': {'read_only': True},
        # }
