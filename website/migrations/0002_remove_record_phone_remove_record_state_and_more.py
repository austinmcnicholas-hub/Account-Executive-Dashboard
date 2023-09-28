# Generated by Django 4.2.5 on 2023-09-22 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='record',
            name='state',
        ),
        migrations.AlterField(
            model_name='record',
            name='renewal_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='start_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]