from django.urls import path

from publications.api import views as article_views

urlpatterns = [
    path('', article_views.PublicationListAPIView.as_view(), name='articles'),
    path('<int:pk>/', article_views.PublicationDetailAPIVIew.as_view(), name="article_detail"),
    path('sponsored-feed/', article_views.SponsoredPublicationListAPIView.as_view(), name="sponsored_feed"),
    path('featured-feed/', article_views.FeaturedPublicationListAPIView.as_view(), name="featured_feed"),
    path('<str:category>/', article_views.PublicationFilterAPIView.as_view(), name="filter_by"),
    path('create-feed/', article_views.PublicationCreateAPIView.as_view(), name="create_article")
]
