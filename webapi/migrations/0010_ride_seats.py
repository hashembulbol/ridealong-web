# Generated by Django 4.0.4 on 2022-11-01 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapi', '0009_alter_user_kmprice'),
    ]

    operations = [
        migrations.AddField(
            model_name='ride',
            name='seats',
            field=models.IntegerField(default=1),
        ),
    ]
