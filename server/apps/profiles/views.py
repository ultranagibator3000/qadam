from rest_framework.generics import (
    CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView)
from rest_framework.permissions import IsAuthenticated

from apps.profiles.models import Profile, Experience
from apps.profiles.serializers import (
    ProfileListSerializer, ProfileRetrieveSerializer, ProfileUpdateSerializer, ExperienceCreateUpdateSerializer)
from apps.profiles.permissions import IsProfileUser, IsExperienceOwner


class ProfileListAPIView(ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileListSerializer

    def get_queryset(self):
        search_query = self.kwargs["q"]
        return Profile.objects.filter(
            first_name__contains=search_query,
            last_name__contains=search_query
        )


class ProfileRetrieveAPIView(RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileRetrieveSerializer


class ProfileUpdateAPIView(UpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileUpdateSerializer
    permission_classes = (IsAuthenticated, IsProfileUser, )


# --- --- --- #


class ExperienceCreateAPIView(CreateAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceCreateUpdateSerializer
    permission_classes = (IsAuthenticated, )

    def get_profile(self):
        _profile = self.request.user.profile
        return _profile

    def perform_create(self, serializer):
        _profile = self.get_object()
        serializer.save(profile=_profile)



class ExperienceUpdateAPIView(UpdateAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceCreateUpdateSerializer
    permission_classes = (IsAuthenticated, IsExperienceOwner)


class ExperienceDestroyAPIView(DestroyAPIView):
    queryset = Experience.objects.all()
    permission_classes = (IsAuthenticated, IsExperienceOwner)
