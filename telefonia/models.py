# -*- coding: utf-8 -*-

from django.db import models

#--------------------------------------------------------------------------------------
class Departamento(models.Model):
	nome = models.CharField(max_length=300)

	def __unicode__(self):
		return self.nome

#--------------------------------------------------------------------------------------
class Ramal(models.Model):
	nome = models.CharField(max_length=200)
	numero = models.CharField(max_length=20)

	def __unicode__(self):
		return self.nome + ' - ' + self.numero

	class Meta:
		verbose_name_plural = "ramais"

#--------------------------------------------------------------------------------------
class Problemas(models.Model):
	nome = models.CharField(max_length=500)

	def __unicode__(self):
		return self.nome

	class Meta:
		verbose_name_plural = "problemas"

#--------------------------------------------------------------------------------------
class Status(models.Model):
	nome = models.CharField(max_length=100)
	default = models.BooleanField(default=False)

	def __unicode__(self):
		return self.nome

	class Meta:
		verbose_name_plural = "status"

#--------------------------------------------------------------------------------------
class Urgencia(models.Model):
	nome = models.CharField(max_length=100)

	def __unicode__(self):
		return self.nome

#--------------------------------------------------------------------------------------
class Executor(models.Model):
	nome = models.CharField(max_length=100)
	default = models.BooleanField(default=False)

	def __unicode__(self):
		return self.nome

	class Meta:
		verbose_name_plural = "executores"

#--------------------------------------------------------------------------------------
class Chamado(models.Model):
	abertura = models.DateField()
	fechamento = models.DateField(blank=True, null=True)
	solicitante = models.CharField(max_length=300)
	departamento = models.ForeignKey('Departamento')
	ramal_atendimento = models.ForeignKey('Ramal', related_name="ramal_atendimento")
	ramal_contato = models.ForeignKey('Ramal', related_name="ramal_contato")
	problema = models.CharField(max_length=500, blank=True, null=True)
	execucao = models.CharField(max_length=300, blank=True, null=True)
	status = models.ForeignKey('Status')
	urgencia = models.ForeignKey('Urgencia')
	executor = models.ForeignKey('Executor')

	def __unicode__(self):
		return "Chamado : " + unicode(self.id)

#--------------------------------------------------------------------------------------
class TipoEquipamento(models.Model):
	nome = models.CharField(max_length=100)

	def __unicode__(self):
		return self.nome

#--------------------------------------------------------------------------------------
class TrocaEquipamento(models.Model):
	chamado = models.ForeignKey('Chamado')
	tipo_equipamento = models.ForeignKey('TipoEquipamento')
	serial_velho = models.CharField(max_length=50, null=True)
	serial_novo = models.CharField(max_length=50, null=True)
	motivo = models.CharField(max_length=500, blank=True, null=True)