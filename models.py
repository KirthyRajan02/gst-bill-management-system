# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_flag = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class GstbillingappBillingprofile(models.Model):
    plan_start_date = models.DateField(blank=True, null=True)
    plan_end_date = models.DateField(blank=True, null=True)
    plan = models.ForeignKey('GstbillingappPlan', models.DO_NOTHING, blank=True, null=True)
    user = models.OneToOneField(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'gstbillingapp_billingprofile'


class GstbillingappBook(models.Model):
    current_balance = models.FloatField()
    customer = models.ForeignKey('GstbillingappCustomer', models.DO_NOTHING, blank=True, null=True)
    last_log = models.ForeignKey('GstbillingappBooklog', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gstbillingapp_book'


class GstbillingappBooklog(models.Model):
    date = models.DateTimeField(blank=True, null=True)
    last_modified = models.DateTimeField()
    change_type = models.IntegerField()
    change = models.FloatField()
    description = models.TextField(blank=True, null=True)
    associated_invoice = models.ForeignKey('GstbillingappInvoice', models.DO_NOTHING, blank=True, null=True)
    parent_book = models.ForeignKey(GstbillingappBook, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gstbillingapp_booklog'


class GstbillingappCustomer(models.Model):
    customer_name = models.CharField(max_length=200)
    customer_address = models.TextField(blank=True, null=True)
    customer_phone = models.CharField(max_length=10, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    customer_gst = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gstbillingapp_customer'


class GstbillingappInventory(models.Model):
    current_stock = models.IntegerField()
    alert_level = models.IntegerField()
    last_log = models.ForeignKey('GstbillingappInventorylog', models.DO_NOTHING, blank=True, null=True)
    product = models.ForeignKey('GstbillingappProduct', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gstbillingapp_inventory'


class GstbillingappInventorylog(models.Model):
    date = models.DateTimeField(blank=True, null=True)
    change = models.IntegerField()
    change_type = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    associated_invoice = models.ForeignKey('GstbillingappInvoice', models.DO_NOTHING, blank=True, null=True)
    product = models.ForeignKey('GstbillingappProduct', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    last_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'gstbillingapp_inventorylog'


class GstbillingappInvoice(models.Model):
    invoice_number = models.IntegerField()
    invoice_date = models.DateField()
    invoice_json = models.TextField()
    invoice_customer = models.ForeignKey(GstbillingappCustomer, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    books_reflected = models.BooleanField()
    inventory_reflected = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'gstbillingapp_invoice'


class GstbillingappPlan(models.Model):
    plan_name = models.TextField(blank=True, null=True)
    plan_value = models.IntegerField(blank=True, null=True)
    monthly_invoice_limit = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gstbillingapp_plan'


class GstbillingappProduct(models.Model):
    product_name = models.CharField(max_length=200)
    product_unit = models.CharField(max_length=50)
    product_gst_percentage = models.FloatField()
    product_rate_with_gst = models.FloatField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    product_hsn = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gstbillingapp_product'


class GstbillingappUserprofile(models.Model):
    business_address = models.TextField(blank=True, null=True)
    business_email = models.CharField(max_length=100, blank=True, null=True)
    business_phone = models.CharField(max_length=10, blank=True, null=True)
    business_gst = models.CharField(max_length=15, blank=True, null=True)
    user = models.OneToOneField(AuthUser, models.DO_NOTHING)
    business_title = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gstbillingapp_userprofile'


class SocialAuthAssociation(models.Model):
    server_url = models.CharField(max_length=255)
    handle = models.CharField(max_length=255)
    secret = models.CharField(max_length=255)
    issued = models.IntegerField()
    lifetime = models.IntegerField()
    assoc_type = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'social_auth_association'
        unique_together = (('server_url', 'handle'),)


class SocialAuthCode(models.Model):
    email = models.CharField(max_length=254)
    code = models.CharField(max_length=32)
    verified = models.BooleanField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'social_auth_code'
        unique_together = (('email', 'code'),)


class SocialAuthNonce(models.Model):
    server_url = models.CharField(max_length=255)
    timestamp = models.IntegerField()
    salt = models.CharField(max_length=65)

    class Meta:
        managed = False
        db_table = 'social_auth_nonce'
        unique_together = (('server_url', 'timestamp', 'salt'),)


class SocialAuthPartial(models.Model):
    token = models.CharField(max_length=32)
    next_step = models.PositiveSmallIntegerField()
    backend = models.CharField(max_length=32)
    timestamp = models.DateTimeField()
    data = models.JSONField()

    class Meta:
        managed = False
        db_table = 'social_auth_partial'


class SocialAuthUsersocialauth(models.Model):
    provider = models.CharField(max_length=32)
    uid = models.CharField(max_length=255)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    extra_data = models.JSONField()

    class Meta:
        managed = False
        db_table = 'social_auth_usersocialauth'
        unique_together = (('provider', 'uid'),)
