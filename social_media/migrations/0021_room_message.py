# Generated by Django 4.2.7 on 2024-01-18 10:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('social_media', '0020_alter_account_date_of_birth'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(auto_now_add=True, null=True)),
                ('updated_date', models.DateField(auto_now=True, null=True)),
                ('deleted_date', models.DateField(blank=True, null=True)),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'ordering': ['-id'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(auto_now_add=True, null=True)),
                ('updated_date', models.DateField(auto_now=True, null=True)),
                ('deleted_date', models.DateField(blank=True, null=True)),
                ('active', models.BooleanField(default=True)),
                ('who_sent', models.CharField(max_length=1000)),
                ('content', models.CharField(max_length=10000)),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message_receiver_set', to='social_media.account')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='social_media.room')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message_sender_set', to='social_media.account')),
            ],
            options={
                'ordering': ['-id'],
                'abstract': False,
            },
        ),
    ]