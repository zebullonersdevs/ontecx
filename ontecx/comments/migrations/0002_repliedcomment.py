# Generated by Django 2.2.11 on 2020-03-18 09:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RepliedComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_replied', models.DateTimeField(auto_now_add=True)),
                ('replies', models.CharField(max_length=150, verbose_name='replies')),
                ('replied_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replied_by', to=settings.AUTH_USER_MODEL)),
                ('replied_on', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replied_on', to='comments.Comments')),
            ],
            options={
                'ordering': ('-date_replied',),
            },
        ),
    ]
