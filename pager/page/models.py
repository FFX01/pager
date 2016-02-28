from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from mptt.models import MPTTModel, TreeForeignKey

# Status choices determine whether or not a user can access a given 'Page' instance.
PAGE_STATUS_CHOICES = (
    ('published', 'published'),
    ('draft', 'draft'),
    ('staged', 'staged')
)


class Page(MPTTModel):
    """
    Base page model. Includes data to define a standard static HTML page.
    """
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
    # Allows for a Page instance to have a 'parent-child' relationship with
    # another Page instance. A Page instance's children can be accessed by
    # calling Page.children. Similarly, a child Page instance can access it's
    # parent via Page.parent. This is a many to one relationship.
    #
    # See https://django-mptt.github.io/django-mptt/models.html#mpttmodel-instance-methods
    # for more methods.
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
        """
        Override save method to automatically generate a slug of the page title.
        :param args:
        :param kwargs:
        :return: Uses super to pass this model instance back to the original
        save method.

        See https://rhettinger.wordpress.com/2011/05/26/super-considered-super/
        for more information.
        """
        if not self.slug:
            self.slug = slugify(self.title)
        super(Page, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
