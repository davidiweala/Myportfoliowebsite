# Generated by Django 3.2.9 on 2021-11-05 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutMe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='David Iweala', max_length=250, verbose_name='name')),
                ('date_of_birth', models.DateField(blank=True)),
                ('address', models.CharField(default='Lagos, Nigeria', max_length=250, verbose_name='address')),
                ('email', models.EmailField(default='iwealadavid@gmail.com', max_length=254)),
                ('phone', models.IntegerField(default='(+234) 9061341499')),
                ('no_of_projects', models.IntegerField(blank=True)),
            ],
        ),
    ]
