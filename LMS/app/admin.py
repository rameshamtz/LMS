from django.contrib import admin
from .models import *

class WhatYouLearnTabularInline(admin.TabularInline):
    model=WhatYouLearn
class RequirementsTabularInline(admin.TabularInline):
    model=Requirement
class VideoTabularInline(admin.TabularInline):
    model=Video

class CourseAdmin(admin.ModelAdmin):
    inlines=(WhatYouLearnTabularInline,RequirementsTabularInline,VideoTabularInline)

admin.site.register(Categories)
admin.site.register(Author)
admin.site.register(Course,CourseAdmin)
admin.site.register(Level)
admin.site.register(WhatYouLearn)
admin.site.register(Requirement)
admin.site.register(Lesson)
