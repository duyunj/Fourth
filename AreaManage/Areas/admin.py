from django.contrib import admin


from Areas.models import AreaInfo
from Areas.models import HeroInfo

# Register your models here.


@admin.register(AreaInfo)
class AreaAdmin(admin.ModelAdmin):
	
	list_display = ('name', 'pid')

@admin.register(HeroInfo)
class HeroAdmin(admin.ModelAdmin):
	
	list_display = ('name', 'province', 'city', 'country')

	change_form_template = 'area.html'

