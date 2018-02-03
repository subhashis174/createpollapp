from django.db import models

# Create your models here.
class BlogArticle(models.Model):
	blog_title	=	models.TextField()
	blog_content=	models.TextField()
	blog_pubdate=	models.DateTimeField('published date')
	blog_author	=	models.CharField(max_length=100)

	def __str_(self):
		return self.blog_title
