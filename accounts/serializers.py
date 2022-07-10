from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from accounts.models import Student,Teacher, User
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username', 'password')


class StudentCustomRegistrationSerializer(RegisterSerializer):
    student = serializers.PrimaryKeyRelatedField(read_only=True,) #by default allow_null = False
    age=serializers.IntegerField(required=False)
    def get_cleaned_data(self):
            data = super(StudentCustomRegistrationSerializer, self).get_cleaned_data()
            extra_data = {
                'age' : self.validated_data.get('age', ''),
            }
            data.update(extra_data)
            return data

    def save(self, request):
        user = super(StudentCustomRegistrationSerializer, self).save(request)
        user.is_student = True
        user.save()
        student = Student(student=user, age=self.cleaned_data.get('age'))
        student.save()
        return 

class TeacherCustomRegistrationSerializer(RegisterSerializer):
    teacher = serializers.PrimaryKeyRelatedField(read_only=True,) #by default allow_null = False
    
    def get_cleaned_data(self):
            data = super(TeacherCustomRegistrationSerializer, self).get_cleaned_data()
            # extra_data = {
            #     'country' : self.validated_data.get('country', ''),
            # }
            # data.update(extra_data)
            return data

    def save(self, request):
        user = super(TeacherCustomRegistrationSerializer, self).save(request)
        user.is_teacher = True
        user.save()
        teacher = Teacher(teacher=user)
        teacher.save()
        return user

class TokenSerializer(serializers.ModelSerializer):
    user_type = serializers.SerializerMethodField()

    class Meta:
        model = Token
        fields = ('key', 'user', 'user_type')

    def get_user_type(self, obj):
        serializer_data = UserSerializer(
            obj.user
        ).data
        is_student = serializer_data.get('is_student')
        is_teacher = serializer_data.get('is_teacher')
        return {
            'is_student': is_student,
            'is_teacher': is_teacher
        }