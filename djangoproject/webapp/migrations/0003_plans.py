# Generated by Django 2.2.5 on 2019-09-30 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('webapp', '0002_delete_plans'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plans',
            fields=[
                ('plan_id', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('free_talktime', models.IntegerField()),
                ('free_sms', models.IntegerField()),
                ('free_data', models.IntegerField()),
                ('call_rate', models.IntegerField()),
                ('sms_rate', models.DecimalField(decimal_places=2, max_digits=30)),
                ('data_rate', models.DecimalField(decimal_places=2, max_digits=30)),
                ('price', models.DecimalField(decimal_places=2, max_digits=30)),
            ],
        ),
    ]
