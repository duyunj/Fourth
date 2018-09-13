from django.db import models

# Create your models here.


class AreaInfo(models.Model):
	"""地区模型类"""

	name = models.CharField(max_length = 50)
	pid = models.ForeignKey('self', related_name = 'areas',null=True, blank=True, on_delete = models.SET_NULL)
	

	def __str__(self):
		return self.name
	
		
	class Meta:
		db_table = 'areainfo'
		
		verbose_name = '地区信息'
		verbose_name_plural = verbose_name
		

class HeroInfo(models.Model):
	
	name = models.CharField(max_length = 10)
	# on_delete 表示关联的外键表删除数据时，该条数据不变，外键置为空
	province = models.ForeignKey(AreaInfo, null=True, blank=True, on_delete = models.SET_NULL)
	city = models.ForeignKey(AreaInfo, related_name = 'areainfo', null=True, blank=True, on_delete = models.SET_NULL)
	country = models.ForeignKey(AreaInfo, related_name = 'areainfos', null=True, blank=True, on_delete = models.SET_NULL)
	
	def __str__(self):
		return self.name
	
	class Meta:
		db_table = 'heroinfo'
		
		verbose_name = '人物信息'
		verbose_name_plural = verbose_name

