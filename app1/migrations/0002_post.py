# Generated by Django 3.0.1 on 2019-12-26 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User', models.EmailField(max_length=254)),
                ('Posttext', models.CharField(max_length=500)),
            ],
        ),
    ]
