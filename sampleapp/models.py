from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from taggit.managers import TaggableManager
from django.contrib.auth.models import User

class NewsArticle(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=200)
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    main_image = models.ImageField(upload_to='news_images/', null=True, blank=True)
    og_image = models.ImageField(upload_to='og_images/', null=True, blank=True, verbose_name='Open Graph Image')
    tags = TaggableManager(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "News Article"
        verbose_name_plural = "News Articles"
        ordering = ['-date']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('news_article_detail', kwargs={'slug': self.slug})

    def get_og_image(self):
        if self.og_image:
            return self.og_image.url
        elif self.main_image:
            return self.main_image.url
        return None

class NewsArticleRelatedLink(models.Model):
    article = models.ForeignKey(NewsArticle, on_delete=models.CASCADE, related_name='related_links')
    name = models.CharField(max_length=255)
    url = models.URLField()

    def __str__(self):
        return f"{self.name} - {self.article.title}"