from rest_framework import serializers
from users.models import User, Teacher, Student


class TeacherProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('subjectexprty', 'YearOfExp')


class StudentProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('div', 'std', 'rollno', 'ParentileContact', 'bloodgroup',
                  'familyIncome')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    Teacherprofile = TeacherProfileSerializer(required=True)
    Studentprofile = StudentProfileSerializer(required=True)

    class Meta:
        model = User
        fields = ('url', 'email', 'first_name', 'last_name', 'password',
                  'address', 'phone_number', 'Teacherprofile',
                  'Studentprofile')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):

        profile_data1 = validated_data.pop('Teacherprofile')
        profile_data2 = validated_data.pop('Studentprofile')

        password = validated_data.pop('password')
        user = User(**validated_data)

        user.set_password(password)
        user.save()
        if self.context['context'] is 'teacher':
            Teacher.objects.create(user=user, **profile_data1)
            return user

        if self.context['context'] is 'student':
            Student.objects.create(user=user, **profile_data2)
            return user

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')
        profile = instance.profile

        instance.email = validated_data.get('email', instance.email)
        instance.save()

        profile.subjectexprty = profile_data.get('subjectexprty',
                                                 profile.subjectexprty)
        profile.YearOfExp = profile_data.get('YearOfExp', profile.YearOfExp)

        profile.save()

        return instance
