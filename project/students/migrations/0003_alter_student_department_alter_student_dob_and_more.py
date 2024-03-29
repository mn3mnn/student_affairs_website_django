# Generated by Django 4.2.1 on 2023-05-16 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_rename_date_student_dob_alter_student_gpa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='department',
            field=models.CharField(max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='dob',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='gpa',
            field=models.DecimalField(decimal_places=1, max_digits=4, null=True),
        ),
    ]
