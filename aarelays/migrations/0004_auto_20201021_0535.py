# Generated by Django 3.1.2 on 2020-10-21 05:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aarelays', '0003_auto_20201021_0529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relayconfigurations',
            name='destination_aadiscordbot',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='aarelays.destinationaadiscordbot'),
        ),
        migrations.AlterField(
            model_name='relayconfigurations',
            name='destination_webhook',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='aarelays.destinationwebhooks'),
        ),
        migrations.AlterField(
            model_name='relayconfigurations',
            name='source_channel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='aarelays.channels'),
        ),
        migrations.AlterField(
            model_name='relayconfigurations',
            name='source_server',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='aarelays.servers'),
        ),
    ]