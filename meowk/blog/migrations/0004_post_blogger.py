# Generated by Django 3.2.6 on 2021-08-04 16:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='blogger',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.blogger'),
        ),
    ]
