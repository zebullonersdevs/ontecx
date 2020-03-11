# Generated by Django 2.2.11 on 2020-03-09 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0003_publication_publication_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='publication_category',
            field=models.CharField(choices=[('startup', 'STARTUP'), ('life style', 'LIFE STYLE'), ('events', 'EVENTS'), ('technology jobs', 'TECHNOLOGY JOBS'), ('funding', 'FUNDING'), ('reviews and deals', 'REVIEWS AND DEALS'), ('technologies and gadgets', 'TECHNOLOGIES AND GADGETS')], max_length=200, null=True),
        ),
    ]