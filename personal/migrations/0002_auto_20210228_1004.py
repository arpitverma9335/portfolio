# Generated by Django 3.1.5 on 2021-02-28 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achievement',
            name='link_plat',
            field=models.CharField(default='None', max_length=50),
        ),
    ]
