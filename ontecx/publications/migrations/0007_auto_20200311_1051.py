# Generated by Django 2.2.11 on 2020-03-11 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0006_auto_20200311_0955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='image',
            field=models.URLField(default='https://images.unsplash.com/photo-1536137011311-182058a260ba?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2550&q=80'),
        ),
    ]
