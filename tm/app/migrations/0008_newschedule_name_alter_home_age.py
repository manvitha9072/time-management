# Generated by Django 4.0.4 on 2022-05-29 10:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_delete_info_remove_newschedule_name_newschedule_desc_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='newschedule',
            name='name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.home'),
        ),
        migrations.AlterField(
            model_name='home',
            name='age',
            field=models.CharField(default='122', max_length=122),
        ),
    ]