from django.urls import path

from publications.api import views as article_views

urlpatterns = [
    path('', article_views.PublicationListAPIView.as_view(), name='articles'),
    path('<int:>/', article_views.PublicationDetailAPIVIew.as_view(), name="article_detail")
]
