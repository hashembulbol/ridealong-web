# Generated by Django 4.0.4 on 2022-10-30 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapi', '0005_alter_trip_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='kmprice',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=2),
            preserve_default=False,
        ),
    ]