# Generated by Django 2.1.3 on 2018-11-27 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Test1', '0002_auto_20181122_1235'),
    ]

    operations = [
        migrations.AddField(
            model_name='testmodel',
            name='delete',
            field=models.BooleanField(default=False),
        ),
    ]