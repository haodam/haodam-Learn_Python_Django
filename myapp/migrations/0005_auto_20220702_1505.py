# Generated by Django 3.2.5 on 2022-07-02 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_baibao_publication'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reporter',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='reporter',
            name='first_name',
            field=models.CharField(max_length=30, verbose_name='Ten'),
        ),
        migrations.AlterField(
            model_name='reporter',
            name='last_name',
            field=models.CharField(max_length=30, verbose_name='Ho'),
        ),
    ]
