# Generated by Django 4.0.4 on 2022-10-30 20:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapi', '0007_remove_trip_cost_trip_revenue_cost_trip_costs'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ride',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('distance', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
            ],
        ),
        migrations.RemoveField(
            model_name='trip',
            name='costs',
        ),
        migrations.DeleteModel(
            name='Cost',
        ),
        migrations.AddField(
            model_name='ride',
            name='trip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapi.trip'),
        ),
        migrations.AddField(
            model_name='ride',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='trip',
            name='rides',
            field=models.ManyToManyField(related_name='rides', to='webapi.ride'),
        ),
    ]
