from django.db import models
from django.utils.text import slugify
# Create your models here.


class Project(models.Model):
    """
    Create Porfolio projects
    """
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=25)
    image = models.ImageField(
        upload_to="images/", blank=True)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.slug == None:
            slug = slugify(self.title)

            has_slug = Project.objects.filter(slug=slug).exists()
            count = 1
            while has_slug:
                count += 1
                slug = slugify(self.title) + '-' + str(count)
                has_slug = Project.objects.filter(slug=slug).exists()
            self.slug = slug

        super().save(*args, **kwargs)

    # delete item from db and image from media folder
    def delete(self, *args, **kwargs):
        self.image.delete()
        super().delete(*args, **kwargs)
