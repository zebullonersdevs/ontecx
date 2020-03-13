from django.urls import path

from publications.api import views as article_views

urlpatterns = [
    path('', article_views.PublicationListAPIView.as_view(), name='articles'),
    path('delete-feed/<int:pk>/', article_views.PublicationDeleteAPIVIew.as_view(), name="article_delete"),
    path('update-feed/<int:pk>/', article_views.PublicationUpdateAPIView.as_view(), name="article_update"),
    path('sponsored-feed/', article_views.SponsoredPublicationListAPIView.as_view(), name="sponsored_feed"),
    path('featured-feed/', article_views.FeaturedPublicationListAPIView.as_view(), name="featured_feed"),
    path('create-feed/', article_views.PublicationCreateAPIView.as_view(), name="create_article"),
    path('<str:category>/', article_views.PublicationFilterAPIView.as_view(), name="filter_by"),
]
