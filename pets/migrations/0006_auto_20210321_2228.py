# Generated by Django 3.1.5 on 2021-03-22 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0005_auto_20210321_2211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='upload_location'),
        ),
    ]