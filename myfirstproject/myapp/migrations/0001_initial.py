# Generated by Django 2.1.5 on 2019-02-06 17:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0004_auto_20190206_2258'),
        ('recruiter', '0005_auto_20190205_2137'),
    ]

    operations = [
        migrations.CreateModel(
            name='job_application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recruiter.job')),
                ('job_seeker_mail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.job_seeker')),
            ],
        ),
    ]
