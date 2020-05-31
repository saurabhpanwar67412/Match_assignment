# Generated by Django 3.0.6 on 2020-05-28 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0002_auto_20200528_0837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='imageUri',
            field=models.ImageField(upload_to='media/players/img'),
        ),
        migrations.AlterField(
            model_name='team',
            name='logoUri',
            field=models.ImageField(upload_to='media/teams/img/'),
        ),
    ]