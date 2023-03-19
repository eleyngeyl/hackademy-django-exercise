from django.contrib import admin
from .models import Profile

admin.site.site_header = "Elaine's Admin Page"

class ProfileAdmin(admin.ModelAdmin):
   list_display =('first_name', 'last_name', 'description')

   def first_name(self, obj):
       return obj.user.first_name
    
   def last_name(self, obj):
      return obj.user.last_name
   
   def has_delete_permission(self, request, obj=None):
       return False

admin.site.register(Profile, ProfileAdmin)
