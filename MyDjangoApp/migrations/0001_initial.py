# Generated by Django 2.2.5 on 2019-10-21 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tab',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value_a', models.CharField(max_length=10)),
                ('value_b', models.CharField(max_length=10)),
                ('result', models.CharField(max_length=10)),
            ],
        ),
    ]
