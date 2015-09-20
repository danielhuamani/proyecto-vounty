from django.db import models

# Create your models here.
ESTADO = (
  ('P', 'PUBLICADO'),
  ('R', 'REVISADO'),
  )


class Noticia(models.Model):
    titulo = models.CharField("Titulo", max_length=120)
    estado = models.CharField("Estado", max_length=120, choices=ESTADO, default='P')
    fecha = models.DateField('Fecha', auto_now=True)
    imagen = models.ImageField('imagen', upload_to="imagen")
    contenido = models.TextField("Contenido")

    class Meta:
        verbose_name = "Noticia"
        verbose_name_plural = "Noticias"

    def __unicode__(self):
        return self.codigo
