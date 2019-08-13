from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Customer5, Plan1, MyDBArray, PrepaidPlan, PostpaidPlan, Dongle5


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        instance.set_password(password)
        instance.save()


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer5
        # fields=['id','name','address','pincode','email','select_num','prepostdon','plan','kyc_date']
        fields = "__all__"


class Plan1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Plan1
        # fields=['id','name','address','pincode','email','select_num','prepostdon','plan','kyc_date']
        fields = "__all__"


class MyDBArraySerializer(serializers.ModelSerializer):
    class Meta:
        model = MyDBArray
        fields = "__all__"


class PrepaidPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrepaidPlan
        fields = "__all__"


class PostpaidPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostpaidPlan
        fields = "__all__"


class Dongle2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Dongle5
        fields = "__all__"
