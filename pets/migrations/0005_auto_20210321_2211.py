# Generated by Django 3.1.5 on 2021-03-22 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0004_pet_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pet',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]