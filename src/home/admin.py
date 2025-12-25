from django.contrib import admin
from .models import AuthController,Notification,PasswordResetToken,Payment,Point,Profile,Session,Subscription,UserSetting,VerificationID,VideoCall


@admin.register(AuthController,)
class AuthControllerAdmin(admin.ModelAdmin):

    fieldsets = (
        ('Basic Info', {
            'fields': ('name', 'username', 'email', 'phone', 'avatar')
        }),
        ('Security', {
            'fields': (
                'password',
                'two_factor_enabled',
                'two_factor_method',
                'failed_login_attempts',
                'max_concurrent_sessions',
            )
        }),
        ('Status & Role', {
            'fields': ('role', 'status')
        }),
        ('Login Info', {
            'fields': (
                'last_login_at',
                'last_login_ip',
                'login_count',
            )
        }),
        ('Verification', {
            'fields': (
                'email_verified_at',
                'phone_verified_at',
            )
        }),
        ('Preferences', {
            'fields': (
                'language',
                'notification_preferences',
                'privacy_settings',
            )
        }),
        ('Audit', {
            'fields': (
                'password_changed_at',
                'password_change_required',
                'password_history',
            )
        }),
    )


#@admin.register(AuthController)
#class AuthControllerAdmin(admin.ModelAdmin):
 #   list_display = (
  #      'id',
   #     'name',
    #    'username',
     #   'email',
      #  'role',
       # 'status',
       # 'last_login_at',
    #)

    #list_filter = (
        #'role',
        #'status',
        #'two_factor_enabled',
        #'language',
    #)

    #search_fields = (
     #   'name',
      #  'username',
       # 'email',
        #'phone',
    #)

    #ordering = ('-id',)
admin.site.register(Notification)
admin.site.register(PasswordResetToken)
admin.site.register(Payment)
admin.site.register(Profile)
admin.site.register(Session)
admin.site.register(Subscription)
admin.site.register(UserSetting)
admin.site.register(VerificationID)
admin.site.register(VideoCall)
