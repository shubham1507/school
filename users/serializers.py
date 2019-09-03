from rest_framework import serializers
from users.models import User, Teacher, Student

# class UserProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserProfile
#         fields = ('title', 'dob', 'address', 'country', 'city', 'zip', 'photo')


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
        profile_data = ('Teacherprofile')
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        Teacher.objects.create(user=user, **profile_data)
        return user

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')
        profile = instance.profile

        instance.email = validated_data.get('email', instance.email)
        instance.save()

        profile.subjectexprty = profile_data.get('subjectexprty',
                                                 profile.subjectexprty)
        profile.YearOfExp = profile_data.get('YearOfExp', profile.YearOfExp)
        # profile.address = profile_data.get('address', profile.address)
        # profile.country = profile_data.get('country', profile.country)
        # profile.city = profile_data.get('city', profile.city)
        # profile.zip = profile_data.get('zip', profile.zip)
        # profile.photo = profile_data.get('photo', profile.photo)
        profile.save()

        return instance