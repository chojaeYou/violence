from django.contrib import admin
from import_export.admin import ExportActionModelAdmin,ImportExportMixin,ImportMixin
from .models import Student
from .models import Student_check
# Register your models here.
@admin.register(Student)
class StudentAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display=('id','school','grade','name','phone','time','date','st_phone','fee_day','step','reg_date')
    search_fields=('id','school','grade','name','phone','time','date','st_phone','fee_day','step','reg_date')

@admin.register(Student_check)
class CheckAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display=('st_id','name','date')
    search_fields=('st_id','name','date')

