from rest_framework.generics import ListCreateAPIView

from apps.register.models import ApplicationForm
from apps.register.serializers import ApplicationFormListCreateSerializer
from apps.register.permissions import IsAllowed


class ApplicationFormListCreateAPIView(ListCreateAPIView):
    queryset = ApplicationForm.objects.all()
    serializer_class = ApplicationFormListCreateSerializer
    permission_classes = (IsAllowed, )
