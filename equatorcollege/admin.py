from django.contrib import admin
from .models import Department,CourseLevel,CourseName,StudentInformation

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('department_name', 'user')
    list_filter = ('user', )
    search_fields = ('department_name', 'user__username')

admin.site.register(Department, DepartmentAdmin)

class CourseLevelAdmin(admin.ModelAdmin):
    list_display = ('courselevel_name',)
admin.site.register(CourseLevel, CourseLevelAdmin)

class CourseNameAdmin(admin.ModelAdmin):
    list_display = ('course_name',)
admin.site.register(CourseName, CourseNameAdmin)

class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_id','gender')
admin.site.register(StudentInformation, StudentAdmin)



