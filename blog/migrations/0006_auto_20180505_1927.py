# Generated by Django 2.0.3 on 2018-05-05 19:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20180501_2011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='_featured_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
    ]
