# Generated by Django 3.2.9 on 2021-11-05 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_alter_aboutme_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutme',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
