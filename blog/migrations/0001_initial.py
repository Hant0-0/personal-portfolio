# Generated by Django 4.1.3 on 2022-11-27 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project_blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=450)),
                ('date', models.DateField()),
                ('description', models.CharField(max_length=250)),
            ],
        ),
    ]
