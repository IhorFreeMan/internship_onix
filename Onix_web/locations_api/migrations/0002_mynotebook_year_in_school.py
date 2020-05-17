# Generated by Django 3.0.1 on 2020-05-15 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mynotebook',
            name='year_in_school',
            field=models.CharField(choices=[('FR', 'Freshman'), ('SO', 'Sophomore'), ('JR', 'Junior'), ('SR', 'Senior'), ('GR', 'Graduate')], default='FR', max_length=2),
        ),
    ]
