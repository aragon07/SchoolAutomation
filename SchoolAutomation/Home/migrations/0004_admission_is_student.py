# Generated by Django 2.1.7 on 2019-03-21 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_auto_20190321_1807'),
    ]

    operations = [
        migrations.AddField(
            model_name='admission',
            name='is_student',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
