# Generated by Django 4.0.4 on 2022-05-28 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_info'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Info',
        ),
        migrations.RemoveField(
            model_name='newschedule',
            name='name',
        ),
        migrations.AddField(
            model_name='newschedule',
            name='desc',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='newschedule',
            name='time',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='newschedule',
            name='title',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
