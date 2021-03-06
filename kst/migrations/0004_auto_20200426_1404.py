# Generated by Django 3.0.1 on 2020-04-26 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kst', '0003_auto_20200419_1721'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('csm', models.CharField(max_length=100, verbose_name='参数名')),
                ('csz', models.CharField(max_length=100, verbose_name='参数值')),
                ('csh', models.SmallIntegerField(verbose_name='序号')),
            ],
        ),
        migrations.AlterField(
            model_name='dg',
            name='pm',
            field=models.CharField(max_length=100, verbose_name='品名'),
        ),
    ]
