# Generated by Django 3.2.5 on 2023-03-01 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0009_document_type_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='year',
            name='image',
            field=models.ImageField(default='', upload_to='academics/images'),
        ),
    ]
