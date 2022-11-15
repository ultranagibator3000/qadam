from rest_framework import serializers

from apps.profiles.models import Profile, Experience


class ProfileListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["id", "first_name", "last_name", "image"]


class ProfileRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        exclude = ["user"]
         

class ProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        exclude = ["user"]
        read_only_fields = ["user"]


class ExperienceCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        exclude = ["profile"]
