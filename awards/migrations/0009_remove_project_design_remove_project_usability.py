# Generated by Django 4.0.5 on 2022-06-14 23:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0008_project_design_project_usability'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='design',
        ),
        migrations.RemoveField(
            model_name='project',
            name='usability',
        ),
    ]
