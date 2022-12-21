from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# MODELO CATEGORÍA
class Category (models.Model):
	name = models.CharField(max_length=200, unique=True, verbose_name='Nombre')
	active = models.BooleanField(default=True, verbose_name='Activo')
	created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
	updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')

	class Meta:
		verbose_name = 'Categoría'
		verbose_name_plural = 'Categorías'
		ordering = ['name']

	def __str__(self):
		return self.name

# MODELO DE ETIQUETAS
class Tag (models.Model):
	name = models.CharField(max_length=200, unique=True, verbose_name='Nombre')
	active = models.BooleanField(default=True, verbose_name='Activo')
	created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
	updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')

	class Meta:
		verbose_name = 'Etiqueta'
		verbose_name_plural = 'Etiquetas'
		ordering = ['name']

	def __str__(self):
		return self.name

# MODELO DE AUTOR = USUARIOS REGISTRADOS EN LA APLICACION => importando la tabla de usuarios

# MODELO DE LOS POSTS
class Post(models.Model):
	title = models.CharField(max_length=250, verbose_name='Título')
	excerpt = models.TextField(verbose_name='Bajada')
	content = RichTextField(verbose_name='Contenido')
	image = models.ImageField(upload_to='posts', null=True, blank=True, verbose_name='Imagen')
	published = models.BooleanField(default=False, verbose_name='Publicado')

	# Campos con relaciones
	category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='get_posts', verbose_name='Categoría')
	author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='get_posts', verbose_name='Autor')
	tags = models.ManyToManyField(Tag, verbose_name='Etiquetas')

	created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
	updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')

	class Meta:
		verbose_name = 'Publicación'
		verbose_name_plural = 'Publicaciones'
		ordering = ['-created']

	def __str__(self):
		return self.title

##########################################################

# MODELO ABOUT
class About(models.Model):
	description = models.CharField(max_length=350, verbose_name='Descripción')
	created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
	updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')

	class Meta:
		verbose_name = 'Acerca de'
		verbose_name_plural = 'Acerca de Nosotros'
		ordering = ['-created']

	def __str__(self):
		return self.description


# MODELO LINK = REDES SOCIALES
class Link(models.Model):
	key = models.CharField(max_length=100, verbose_name='Key Link')
	name = models.CharField(max_length=120, verbose_name='Red Social')
	url = models.URLField(max_length=350, blank=True, null=True, verbose_name='Enlace')
	icon = models.CharField(max_length=100, blank=True, null=True, verbose_name='Icono')
	created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
	updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')

	class Meta:
		verbose_name = 'Red Social'
		verbose_name_plural = 'Redes Sociales'
		ordering = ['name']

	def __str__(self):
		return self.name
