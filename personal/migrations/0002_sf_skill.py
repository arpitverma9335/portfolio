# Generated by Django 3.1.5 on 2021-07-03 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='sf_skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sf_area', models.CharField(max_length=40)),
                ('sf_percent', models.IntegerField(default=0)),
            ],
        ),
    ]