# Generated by Django 4.2.5 on 2023-09-23 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_alter_record_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='notes',
            field=models.CharField(max_length=800),
        ),
    ]
