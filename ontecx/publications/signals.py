from django.dispatch import receiver
from django.db.models.signals import post_save

from publications.models import  PublicationCategory, Publication
from publications.api.serializers import PublicationSerializer
from notification.models import  DeviceID, send_message

@receiver(post_save, sender=PublicationCategory)
def send_push_notification_to_users(sender, created, instance, **kwargs):
    pass
    #if created:
        #device = DeviceID.objects.filter(active=True).values_list("registration_id")
        #publication = Publication.objects.get(publication_category=instance.pk)
        #publication_detail = PublicationSerializer(instance=publication).data
        #message_title = "{}".format(str(publication.title))
        #message_body = "{}".format(str(publication.content))
        #data_message = {
        #   "id": publication.pk,
        #   "data": publication_detail
        #}
        #send_message(message_title=message_title, message_body=message_body, data_message=data_message)




