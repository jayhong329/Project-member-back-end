# Generated by Django 5.1.1 on 2024-10-11 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('superuser_id', models.AutoField(primary_key=True, serialize=False)),
                ('superuser_name', models.CharField(max_length=50, unique=True)),
                ('superuser_email', models.CharField(max_length=120, unique=True)),
                ('superuser_password', models.CharField(max_length=128)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MemberBasic',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=20, unique=True)),
                ('user_password', models.CharField(max_length=128)),
                ('user_phone', models.CharField(max_length=10, unique=True)),
                ('user_email', models.CharField(max_length=120, unique=True)),
                ('user_nickname', models.CharField(blank=True, max_length=20, null=True)),
                ('user_gender', models.CharField(blank=True, max_length=10, null=True)),
                ('user_birth', models.DateField(blank=True, null=True)),
                ('user_address', models.TextField(blank=True, null=True)),
                ('vip_status', models.IntegerField(default='0')),
                ('user_avatar', models.CharField(blank=True, max_length=50, null=True)),
                ('privacy_id', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'db_table': 'member_basic',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MemberCoupon',
            fields=[
                ('user_id', models.IntegerField(primary_key=True, serialize=False)),
                ('coupon_id', models.IntegerField()),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'db_table': 'member_coupon',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MemberFavorite',
            fields=[
                ('type_id', models.IntegerField(primary_key=True, serialize=False)),
                ('type_name', models.CharField(blank=True, max_length=50, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'db_table': 'member_favorite',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MemberLogin',
            fields=[
                ('login_id', models.IntegerField(primary_key=True, serialize=False)),
                ('provider', models.CharField(blank=True, max_length=50, null=True)),
                ('provider_id_google', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('provider_id_line', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('provider_id_fb', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('access_token', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'db_table': 'member_login',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MemberOrderdetails',
            fields=[
                ('user_id', models.IntegerField(primary_key=True, serialize=False)),
                ('ordernumber', models.IntegerField(db_column='orderNumber')),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'db_table': 'member_orderdetails',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MemberPhoto',
            fields=[
                ('user_avatar', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('image_url', models.CharField(blank=True, max_length=128, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'db_table': 'member_photo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MemberPrivacy',
            fields=[
                ('privacy_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_email', models.CharField(blank=True, max_length=120, null=True)),
                ('privacy_name', models.CharField(blank=True, max_length=50, null=True)),
                ('privacy_value', models.BooleanField(default=False)),
                ('phone_change', models.CharField(blank=True, max_length=10, null=True)),
                ('email_change', models.CharField(blank=True, max_length=50, null=True)),
                ('account_verify', models.BooleanField(default=False)),
                ('activity_checked', models.BooleanField(default=False)),
                ('double_verify', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'db_table': 'member_privacy',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MemberVerify',
            fields=[
                ('verify_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_email', models.CharField(blank=True, max_length=120, null=True)),
                ('verification_code', models.CharField(blank=True, max_length=6, null=True)),
                ('verification_token', models.CharField(blank=True, max_length=16, null=True)),
                ('code_used', models.BooleanField(default=False)),
                ('token_used', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('expires_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'member_verify',
                'managed': False,
            },
        ),
    ]
