# from .models import QuestionCategory
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Task


class SignUpSerializer(serializers.ModelSerializer):
    # len_name = serializers.SerializerMethodField()
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        extre_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({"error":"Both Password Are Not Same"})

        if User.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({"error":"Email Already Exist"})


        account = User(email=self.validated_data['email'],username=self.validated_data['username'])
        account.set_password(password)
        account.save()
        return account

    # def get_len_name(self, object):
    #     return len(object.name)

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class UserTaskSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True)
    class Meta:
        model = User
        fields = '__all__'

