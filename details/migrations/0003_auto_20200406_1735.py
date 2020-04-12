# Generated by Django 2.1.11 on 2020-04-06 12:05

import details.models
from django.db import migrations
import djongo.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0002_auto_20200406_0238'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faculty',
            name='accomplishments',
        ),
        migrations.AddField(
            model_name='faculty',
            name='certifications',
            field=djongo.models.fields.ArrayField(model_container=details.models.Certification, null=True),
        ),
    ]
