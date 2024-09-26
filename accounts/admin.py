from django.contrib import admin
from accounts.models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    # Specify the fields to display in the list view
    list_display = ('eno', 'ename', 'esal', 'eaddr')
    
    # Enable search functionality for the specified fields
    search_fields = ('ename', 'eaddr')

# Register your model with the custom admin class
admin.site.register(Employee, EmployeeAdmin)