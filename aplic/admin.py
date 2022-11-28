from django.contrib import admin
from .models import Funcionario, Cargo

class FuncionarioAdmin(admin.ModelAdmin):
	list_display = ('cargo', 'salario')
	class meta:
		model = Funcionario


	
admin.site.register(Funcionario, FuncionarioAdmin)
admin.site.register(Cargo)