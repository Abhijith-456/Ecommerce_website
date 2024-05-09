# Generated by Django 5.0.4 on 2024-05-08 09:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ShippingAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shipping_full_name', models.CharField(max_length=255)),
                ('shipping_email', models.CharField(max_length=255)),
                ('shipping_address1', models.CharField(max_length=255)),
                ('shipping_address2', models.CharField(blank=True, max_length=255, null=True)),
                ('shipping_city', models.CharField(max_length=255)),
                ('shipping_state', models.CharField(blank=True, max_length=255, null=True)),
                ('shipping_zipcode', models.CharField(blank=True, max_length=255, null=True)),
                ('shipping_country', models.CharField(max_length=255)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
