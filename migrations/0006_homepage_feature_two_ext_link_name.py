# Generated by Django 3.0.8 on 2020-09-25 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_homepage_feature_two_ext_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='feature_two_ext_link_name',
            field=models.CharField(blank=True, max_length=250, verbose_name='Name of the external link'),
        ),
    ]
