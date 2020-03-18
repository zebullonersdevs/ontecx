from django.db import models
from django.contrib.auth import  get_user_model
from django.utils.translation import ugettext_lazy as _

from publications.models import Publication

User = get_user_model()

# Create your models here.
class Comments(models.Model):
    comment_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comment_by")
    commented_on = models.ForeignKey(Publication, on_delete=models.CASCADE, related_name="commented_on")
    date_commented = models.DateTimeField(auto_now_add=True)
    comment = models.CharField(_("comment"), max_length=200)

    class Meta:
        ordering = ("-date_commented",)

    def __str__(self):
        return str(self.comment_by)


class RepliedComment(models.Model):
    replied_on = models.ForeignKey(Comments, on_delete=models.CASCADE, related_name="replied_on")
    date_replied = models.DateTimeField(auto_now_add=True)
    replies = models.CharField(_("replies"), max_length=150,)
    replied_by  = models.ForeignKey(User, on_delete=models.CASCADE, related_name="replied_by")

    class Meta:
        ordering = ("-date_replied",)

    def __str__(self):
        return str(self.replied_on)
