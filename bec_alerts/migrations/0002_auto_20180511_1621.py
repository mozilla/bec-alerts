# Generated by Django 2.0.4 on 2018-05-11 21:21

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bec_alerts', '0001_squashed_0007_issue_groupid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='stack_frames',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=list),
        ),
    ]
