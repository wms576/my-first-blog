# Generated by Django 3.0.1 on 2020-04-11 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ddjw',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zjh', models.SmallIntegerField()),
                ('zjw', models.TextField()),
            ],
        ),
    ]
