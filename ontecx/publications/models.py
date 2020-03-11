from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _

from model_utils import Choices
from config.settings.local import  PrivateS3Boto3Storage


# Create your models here.

User = get_user_model()



class PublicationCategory(models.Model):
    ARTICLE_CATEGORIES = (
        ('startup', 'STARTUP'),
        ('life style', 'LIFE STYLE'),
        ('events', 'EVENTS'),
        ('technology jobs', 'TECHNOLOGY JOBS'),
        ('funding', 'FUNDING'),
        ('reviews and deals', 'REVIEWS AND DEALS'),
        ('technologies and gadgets', 'TECHNOLOGIES AND GADGETS'),

    )
    category = models.CharField(max_length=200, choices=ARTICLE_CATEGORIES, null=True)
    published_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="published_by")


class Publication(models.Model):

    title = models.CharField(_('title'), max_length=250)
    image = models.URLField(default="https://images.unsplash.com/photo-1536137011311-182058a260ba?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2550&q=80") #models.FileField(_("image"), storage=PrivateS3Boto3Storage())
    content = models.TextField(_('content'))
    date_created = models.DateTimeField(_('date_created'), auto_now_add=True)
    featured_publication = models.ForeignKey('self', on_delete=models.CASCADE, related_name="featured", null=True)
    sponsored_publication = models.ForeignKey('self', on_delete=models.CASCADE, related_name="sponsored", null=True)
    publication_category = models.ForeignKey(PublicationCategory, on_delete=models.CASCADE, related_name="publication_category", null=True)


    class Meta:
        get_latest_by = ("-date_created",)
        #app_label = "publications"

    def __str__(self):
        return "Article published by {}".format(self.title)


#class FeaturedPublication(models.Model):
#    publication = models.ForeignKey(Publication, on_delete=models.CASCADE, related_name="featured")

#    def __str__(self):
#        return str(self.publication)


#class SponsoredPublication(models.Model):
#    sponsored = models.ForeignKey(Publication, on_delete=models.CASCADE, related_name="sponsored_category")



