from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _

from model_utils import Choices
from config.settings.local import  PrivateS3Boto3Storage


# Create your models here.

User = get_user_model()


class Publication(models.Model):
    title = models.CharField(_('title'), max_length=250)
    image = models.FileField(_("image"), storage=PrivateS3Boto3Storage())
    content = models.TextField(_('content'))
    date_created = models.DateTimeField(_('date_created'), auto_now_add=True)
    publication_category = Choices('startup', 'life_style', "events", "technology jobs",
    "government in tech", "funding", "reviews and deals", "technologies and gadgets"
    )
    published_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="published_by")

    class Meta:
        get_latest_by = "-date_created"
        #app_label = "publications"

    def __str__(self):
        return "Article published by {}".format(self.title)



