from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import *

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["id", "username", "email", "first_name", "last_name", "password"]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        return user


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = '__all__'


class SubDistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubDistrict
        fields = '__all__'


class UnionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Union
        fields = '__all__'


class SemiMetroAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SemiMetroArea
        fields = '__all__'


class UnionCustomSerializer(serializers.ModelSerializer):
    Semi_Metro = serializers.SerializerMethodField()
    LatLong = serializers.SerializerMethodField()
    Union_regex = serializers.CharField(source='regex')
    _isSuggested = serializers.BooleanField(source='is_suggested')

    class Meta:
        model = Union
        fields = ['Union_regex', 'thana_no', 'LatLong', '_isSuggested', 'postcode', 'Semi_Metro']

    def get_LatLong(self, obj):
        return [obj.lat, obj.long]

    def get_Semi_Metro(self, obj):
        return {
            sm.name: {
                "Area_regex": sm.regex,
                "LatLong": [sm.lat, sm.long]
            } for sm in obj.semi_metros.all()
        }


class SubDistrictCustomSerializer(serializers.ModelSerializer):
    Union = serializers.SerializerMethodField()
    Subdistrict_regex = serializers.CharField(source='regex')
    LatLong = serializers.SerializerMethodField()

    class Meta:
        model = SubDistrict
        fields = ['Subdistrict_regex', 'Union', 'LatLong']

    def get_Union(self, obj):
        return {
            union.name: UnionCustomSerializer(union).data
            for union in obj.unions.all()
        }

    def get_LatLong(self, obj):
        return [obj.lat, obj.long]


class DistrictCustomSerializer(serializers.ModelSerializer):
    Sub_District = serializers.SerializerMethodField()
    District_regex = serializers.CharField(source='regex')

    class Meta:
        model = District
        fields = ['District_regex', 'Sub_District']

    def get_Sub_District(self, obj):
        return {
            sub.name: SubDistrictCustomSerializer(sub).data
            for sub in obj.subdistricts.all()
        }
