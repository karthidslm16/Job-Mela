# Generated by Django 2.1.5 on 2019-02-07 02:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recruiter', '0005_auto_20190205_2137'),
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='job',
            fields=[
                ('job_id', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('job_name', models.CharField(max_length=30)),
                ('job_desc', models.CharField(max_length=300)),
                ('job_location', models.CharField(default='', max_length=20)),
                ('job_req_1', models.CharField(default='', max_length=50)),
                ('job_req_2', models.CharField(default='', max_length=50)),
                ('job_req_3', models.CharField(default='', max_length=50)),
                ('job_req_4', models.CharField(default='', max_length=50)),
                ('job_poster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recruiter.recruiter')),
            ],
        ),
        migrations.AlterField(
            model_name='job_application',
            name='job_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.job'),
        ),
    ]
