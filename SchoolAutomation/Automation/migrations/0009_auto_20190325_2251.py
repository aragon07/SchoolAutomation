# Generated by Django 2.1.7 on 2019-03-25 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Automation', '0008_auto_20190325_0241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/studentprofile'),
        ),
    ]