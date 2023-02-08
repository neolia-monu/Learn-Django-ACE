# Generated by Django 4.1.6 on 2023-02-06 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university_app', '0004_college_created_at_course_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='college',
            name='course',
            field=models.ManyToManyField(related_name='college', to='university_app.course'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='course',
            field=models.ManyToManyField(related_name='staff', to='university_app.course'),
        ),
    ]
