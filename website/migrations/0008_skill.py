# Generated by Django 3.2.9 on 2021-11-06 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_aboutme_resume'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=250, verbose_name='skillset')),
                ('percentage', models.IntegerField(default='10')),
            ],
        ),
    ]