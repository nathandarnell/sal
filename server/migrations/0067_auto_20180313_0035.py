# Generated by Django 1.10 on 2018-03-13 00:35


from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0066_auto_20180312_0846'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='machinedetailplugin',
            name='os_families',
        ),
        migrations.RemoveField(
            model_name='plugin',
            name='type',
        ),
    ]
