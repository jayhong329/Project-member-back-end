# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthUser(models.Model):
    superuser_id = models.AutoField(primary_key=True)
    superuser_name = models.CharField(unique=True, max_length=50)
    superuser_email = models.CharField(unique=True, max_length=120)
    superuser_password = models.CharField(max_length=128)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_user'


class MemberBasic(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(unique=True, max_length=20)
    user_password = models.CharField(max_length=128)
    user_phone = models.CharField(unique=True, max_length=10)
    user_email = models.CharField(unique=True, max_length=120)
    user_nickname = models.CharField(max_length=20, blank=True, null=True)
    user_gender = models.CharField(max_length=10, blank=True, null=True)
    user_birth = models.DateField(blank=True, null=True)
    user_address = models.TextField(blank=True, null=True)
    vip_status = models.IntegerField(blank=True, null=True)
    user_avatar = models.CharField(max_length=50, blank=True, null=True)
    privacy_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'member_basic'


class MemberCoupon(models.Model):
    user_id = models.IntegerField(primary_key=True)
    coupon_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'member_coupon'


class MemberFavorite(models.Model):
    type_id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(MemberBasic, models.DO_NOTHING)
    type_name = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'member_favorite'


class MemberLogin(models.Model):
    login_id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(MemberBasic, models.DO_NOTHING)
    provider = models.CharField(max_length=50, blank=True, null=True)
    provider_id_google = models.CharField(unique=True, max_length=50, blank=True, null=True)
    provider_id_line = models.CharField(unique=True, max_length=50, blank=True, null=True)
    provider_id_fb = models.CharField(unique=True, max_length=50, blank=True, null=True)
    access_token = models.CharField(unique=True, max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'member_login'


class MemberOrderdetails(models.Model):
    user_id = models.IntegerField(primary_key=True)
    ordernumber = models.IntegerField(db_column='orderNumber')  # Field name made lowercase.
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'member_orderdetails'


class MemberPhoto(models.Model):
    user_avatar = models.CharField(primary_key=True, max_length=50)
    user = models.ForeignKey(MemberBasic, models.DO_NOTHING)
    image_url = models.CharField(max_length=128, blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'member_photo'


class MemberPrivacy(models.Model):
    privacy_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(MemberBasic, models.DO_NOTHING)
    user_email = models.CharField(max_length=120, blank=True, null=True)
    privacy_name = models.CharField(max_length=50, blank=True, null=True)
    privacy_value = models.IntegerField(blank=True, null=True)
    phone_change = models.CharField(unique=True, max_length=10, blank=True, null=True)
    email_change = models.CharField(unique=True, max_length=50, blank=True, null=True)
    account_verify = models.IntegerField(blank=True, null=True)
    activity_checked = models.IntegerField(blank=True, null=True)
    double_verify = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'member_privacy'


class MemberVerify(models.Model):
    verify_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(MemberBasic, models.DO_NOTHING, blank=True, null=True)
    user_email = models.CharField(max_length=50, blank=True, null=True)
    verification_code = models.CharField(max_length=6, blank=True, null=True)
    verification_token = models.CharField(max_length=16, blank=True, null=True)
    code_used = models.IntegerField(blank=True, null=True)
    token_used = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    expires_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'member_verify'
