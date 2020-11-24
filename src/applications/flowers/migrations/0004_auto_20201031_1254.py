# Generated by Django 3.1.2 on 2020-10-31 09:54

import applications.flowers.models.image
from django.db import migrations, models
import django.db.models.deletion
import storages.backends.s3boto3


class Migration(migrations.Migration):

    dependencies = [
        ('flowers', '0003_auto_20201027_1138'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('flowers', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='flowers.flowers')),
                ('original', models.FileField(blank=True, null=True, storage=storages.backends.s3boto3.S3Boto3Storage(), upload_to=applications.flowers.models.image.upload_to)),
            ],
        ),
        migrations.AddField(
            model_name='flowers',
            name='species',
            field=models.TextField(blank=True, null=True),
        ),
    ]
