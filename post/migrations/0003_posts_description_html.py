# Generated by Django 3.0.7 on 2020-09-02 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20200624_0728'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='description_html',
            field=models.TextField(blank=True, default='', editable=False, null=True),
        ),
    ]
