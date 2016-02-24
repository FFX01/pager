from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from mptt.models import MPTTModel, TreeForeignKey


PAGE_STATUS_CHOICES = (
    ('published', 'published'),
    ('draft', 'draft'),
    ('staged', 'staged')
)


class Page(MPTTModel):
    title = models.CharField(
        max_length=150,
        blank=False
    )
    slug = models.SlugField(
        max_length=200,
        blank=True
    )
    meta_description = models.CharField(
        max_length=120,
        blank=True
    )
    author = models.ForeignKey(
        User,
        related_name='pages',
        blank=False
    )
    created = models.DateTimeField(
        auto_now_add=True,
        blank=True
    )
    status = models.CharField(
        choices=PAGE_STATUS_CHOICES,
        max_length=20,
        blank=False
    )
    parent = TreeForeignKey(
        'self',
        blank=True,
        null=True,
        related_name='children'
    )
    content = models.TextField(
        blank=True
    )

    class Meta:
        verbose_name = 'Page'
        verbose_name_plural = 'Pages'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Page, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
