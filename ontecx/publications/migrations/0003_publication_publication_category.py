# Generated by Django 2.2.11 on 2020-03-09 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0002_auto_20200309_0720'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='publication_category',
            field=models.CharField(choices=[('startup', 'STARTUP'), ('life style', 'LIFE STYLE'), ('events', 'EVENTS'), ('technology jobs', 'TECHNOLOGY JOBS'), ('funding', 'FUNDING'), ('reviews and deals', 'REVIEWS AND DEALS'), ('technologies and gadgets', 'TECHNOLOGIES AND GADGETS')], max_length=1, null=True),
        ),
    ]
