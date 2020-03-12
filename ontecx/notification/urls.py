from django.urls import path

from notification.api import views as notification_views

urlpatterns = [
    path('enable/', notification_views.NotificationEnableAPIView.as_view(), name='enable'),
    path('disable/<str:registration_id>/', notification_views.NotificationDisableAPIView.as_view(), name="disabled")
]
