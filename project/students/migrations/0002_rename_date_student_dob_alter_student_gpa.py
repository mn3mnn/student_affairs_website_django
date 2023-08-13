# Generated by Django 4.2.1 on 2023-05-16 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='date',
            new_name='dob',
        ),
        migrations.AlterField(
            model_name='student',
            name='gpa',
            field=models.DecimalField(decimal_places=1, max_digits=4),
        ),
    ]
