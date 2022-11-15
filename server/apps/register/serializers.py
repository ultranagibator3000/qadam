from rest_framework import serializers

from apps.register.models import ApplicationForm


class ApplicationFormListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationForm
        fields = ["name", "contacts"]
