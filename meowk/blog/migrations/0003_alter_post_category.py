# Generated by Django 3.2.6 on 2021-08-04 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('Tech', 'Tech'), ('Social', 'Social')], max_length=200, null=True),
        ),
    ]
