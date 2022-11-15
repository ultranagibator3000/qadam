from django.urls import path

from apps.register.views import ApplicationFormListCreateAPIView

urlpatterns = [
    path('application-forms/', ApplicationFormListCreateAPIView.as_view(),
         name='application-form-list-create')
]
