# Generated by Django 1.10 on 2018-09-11 04:16


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0008_auto_20161012_2329'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventory',
            name='inventory_str',
            field=models.TextField(blank=True, null=True),
        ),
    ]
