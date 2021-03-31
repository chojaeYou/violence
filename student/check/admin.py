from django.contrib import admin
from import_export.admin import ExportActionModelAdmin,ImportExportMixin,ImportMixin
from .models import Student
# Register your models here.

class StudentAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display=('id','school','grade','name','phone','time','date','st_phone','fee_day','step')

admin.site.register(Student,StudentAdmin)