# Generated by Django 3.0.8 on 2020-09-26 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20200925_1721'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='feature_three_ext_link',
            field=models.URLField(blank=True, null=True, verbose_name='Link to an external page instead of a wagtail page'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='feature_three_ext_link_name',
            field=models.CharField(blank=True, max_length=250, verbose_name='Name of the external link'),
        ),
    ]
