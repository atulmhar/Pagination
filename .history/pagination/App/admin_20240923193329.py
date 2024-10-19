from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):

    list_display = ('first_name', 'last_name', 'email', 'phone_number', 'position', 'department', 'hire_date', 'salary')

    search_fields = ('first_name', 'last_name', 'email', 'position', 'department')

    list_filter = ('position', 'department', 'hire_date')

    ordering = ('-hire_date',)

    fieldsets = (

        (None, {'fields': ('first_name', 'last_name', 'email', 'phone_number', 'position', 'department', 'hire_date', 'salary', 'address')}),
    )

    readonly_fields = ('hire_date',)


admin.site.register(Employee, UserAdmin)

