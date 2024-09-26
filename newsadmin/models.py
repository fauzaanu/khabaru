from django.contrib.auth.models import User
from django.db import models
from taggit.managers import TaggableManager


class NewsArticle(models.Model):
    title = models.CharField(max_length=200, help_text="Enter the title of the news article.")
    slug = models.SlugField(unique=True, max_length=200, help_text="Enter a unique slug for the article.")
    date = models.DateField("Post date", help_text="Select the date of the article.")
    intro = models.CharField(max_length=250, null=True, blank=True, help_text="Enter a brief introduction for the article.")
    body = models.TextField(null=True, blank=True, help_text="Enter the main content of the article.")
    author = models.ForeignKey(User, on_delete=models.CASCADE, help_text="Select the author of the article.")
    main_image = models.ImageField(upload_to='news_images/', null=True, blank=True, help_text="Upload the main image for the article.")
    og_image = models.ImageField(upload_to='og_images/', null=True, blank=True, verbose_name='Open Graph Image', help_text="Upload an Open Graph image for social media sharing.")
    featured_media = models.FileField(upload_to='featured_media/', null=True, blank=True, help_text="Upload any featured media (video, audio, etc.).")
    featured_youtube = models.URLField(max_length=200, null=True, blank=True, help_text="Enter the URL of the featured YouTube video.")
    tags = TaggableManager(blank=True, help_text="Add tags to categorize the article, separated by commas.")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "News Article"
        verbose_name_plural = "News Articles"
        ordering = ['-date']

    def __str__(self):
        return self.title
