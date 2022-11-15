from django.urls import path, re_path

from apps.profiles.views import (ProfileListAPIView, ProfileRetrieveAPIView, ProfileUpdateAPIView,
                                 ExperienceCreateAPIView, ExperienceUpdateAPIView, ExperienceDestroyAPIView)

urlpatterns = [
    re_path(r'^profiles/(?P<q>[a-zA-Z]+)/$',
            ProfileListAPIView.as_view(), name='profiles-list'),
    path('profiles/<int:pk>/', ProfileRetrieveAPIView.as_view(),
         name='profile-detail'),
    path('profiles/<int:pk>/', ProfileUpdateAPIView.as_view(), name='profile-update'),

    path('profiles/<int:pk>/experience/',
         ExperienceCreateAPIView.as_view(), name='profile-experience-create'),
    path('profiles/experience/<int:pk>/',
         ExperienceUpdateAPIView.as_view(), name='profile-experience-update'),
    path('profiles/experience/<int:pk>/',
         ExperienceDestroyAPIView.as_view(), name='profile-experience-destroy'),
]
