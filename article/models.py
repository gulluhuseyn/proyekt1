from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
# Author content title created_date >> Article

class Article(models.Model):
    author = models.ForeignKey("auth.User",on_delete=models.CASCADE,verbose_name="Yazar")
    title = models.CharField(max_length=150,verbose_name="Başlıq")
    content = RichTextField(verbose_name="Məzmun")    #textarea
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Yaradılan tarix")
    image = models.FileField(upload_to="Article image",blank=True,null=True,verbose_name="Şəkil")

    def __str__(self):
        return f"{self.title} | {self.author}"