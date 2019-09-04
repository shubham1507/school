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
                  'address', 'phone_number', 'Teacherprofile')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):

        profile_data = validated_data.pop('Teacherprofile')
        print(profile_data)
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        Teacher.objects.create(user=user, **profile_data)
        print(profile_data)
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


class UserSerializer2(serializers.HyperlinkedModelSerializer):

    Studentprofile = StudentProfileSerializer(required=True)

    class Meta:

        model = User
        fields = ('url', 'email', 'first_name', 'last_name', 'password',
                  'address', 'phone_number', 'Studentprofile')

        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        profile_data = validated_data.pop('Studentprofile')
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        Student.objects.create(user=user, **profile_data)
        return user

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')
        profile = instance.profile

        instance.email = validated_data.get('email', instance.email)
        instance.save()

        profile.std = profile_data.get('std', profile.std)
        profile.div = profile_data.get('div', profile.div)
