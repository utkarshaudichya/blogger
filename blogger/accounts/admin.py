from django.contrib import admin
from .models import Profile, PermanentAddress, CorrespondenceAddress

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['pic', 'user', 'phone', 'gender', 'birth_date', 'permanent_address', 'correspondence_address']
    search_fields = ('user__username',)
    list_select_related = ('permanent_address', 'correspondence_address')
    list_filter = ('gender', 'permanent_address__city', 'correspondence_address__city')

    def pic(self, obj):
        if obj.profile_pic:
            return u'<img src="%s" width="100" height="125" />' % obj.profile_pic.url
        elif obj.gender == 'male':
            return u'<img src="/media/male.png" width="125" height="100" />'
        else:
            return u'<img src="/media/female.png" width="125" height="100" />'
    pic.allow_tags = True

class PermanentAddressAdmin(admin.ModelAdmin):
    list_display = ('street_address', 'city', 'state', 'pincode', 'country')
    search_fields = ('user__username',)
    list_filter = ('city', 'pincode', 'state', 'country')

class CorrespondenceAddressAdmin(admin.ModelAdmin):
    list_display = ('street_address', 'city', 'state', 'pincode', 'country')
    search_fields = ('user__username',)
    list_filter = ('city', 'pincode', 'state', 'country')

admin.site.register(Profile, ProfileAdmin)
admin.site.register(PermanentAddress, PermanentAddressAdmin)
admin.site.register(CorrespondenceAddress, CorrespondenceAddressAdmin)
