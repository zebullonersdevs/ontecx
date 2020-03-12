# Create your models here.
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

class DeviceID(models.Model):
    active = models.BooleanField(
        verbose_name=_("Is active"), default=True,
        help_text=_("Inactive devices will not be sent notifications"))

    date_created = models.DateTimeField(
        verbose_name=_("Creation date"), auto_now_add=True)

    registration_id = models.TextField(_('registration_id'))

    def __str__(self):
        return "{} {}".format(self.registration_id)



def send_message(self, message_title, message_body, data_message=None):
        from pyfcm import FCMNotification
        push_service = FCMNotification(api_key=settings.NOTICATION_KEY)
        extra_notification_kwargs = {
            'android_channel_id': 'ONTECX-DEFAULT'
        }
        if data_message is not None:
            return push_service.notify_multiple_devices(registration_id=self.registration_id, message_title=message_title, message_body=message_body, data_message=data_message, extra_notification_kwargs=extra_notification_kwargs)
        return push_service.notify_multiple_devices(registration_id=self.registration_id, message_title=message_title, message_body=message_body, data_message=data_message, extra_notification_kwargs=extra_notification_kwargs)
