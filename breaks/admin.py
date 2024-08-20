from django.contrib import admin

from .models import organisations, groups, replacements, dicts, breaks

#########
# INLINES
########
class ReplacementEmployeeInline(admin.TabularInline):
    model = replacements.ReplacementEmployee
    fields = ('employee' , 'status')
#########
# MODELS REGISTRATION
########

@admin.register(organisations.Organisation)
class OrganisationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'director', )
    
@admin.register(groups.Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'organisation', 'name', 'manager', 'replacement_count')
    list_display_links= ('id', 'name',)
    
    def replacement_count(self, obj):
        return obj.replacements.count()
@admin.register(replacements.Replacement)
class ReplacementAdmin(admin.ModelAdmin):
    list_display = ('id', 'group', 'date',)
    inlines = (
        ReplacementEmployeeInline,
    )
    
@admin.register(dicts.ReplacementStatus)
class ReplacementStatusAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'sort','is_active')
    
@admin.register(dicts.BreakStatus)
class BreakStatusAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'sort','is_active')
    
@admin.register(breaks.Break)
class BreakAdmin(admin.ModelAdmin):
    list_display = ('replacement', 'employee', 'break_start', 
                    'break_end', 'status',)
    
# @admin.register(replacements.Replacement)
# class ReplacementEmployeeAdmin(admin.ModelAdmin):
#     list_display = ('id', 'employee', 'replacement', 'status')
    