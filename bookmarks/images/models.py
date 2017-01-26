from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.utils.text import slugify

class Image(models.Model):
    """
    This is a ForeignKey field because it specifies a one-to-many relationship:
    A user can post multiple images, but each image is posted by a single user.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='images_created')
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, blank=True)
    url = models.URLField()
    image = models.ImageField(upload_to='images/%Y/%m/%d')
    description = models.TextField()
    created = models.DateField(auto_now_add=True, db_index=True)

    """
    We will need a many-to-many relationship in this case, because a user might
    like multiple images and each image can be liked by multiple users.
    ----------------------------------------------------------------------------
    As with ForeignKey fields, the related_name attribute of ManyToManyField
    allows us to name the relationship from the related object back to this one.
    ManyToManyField fields provide a many-to-many manager that allows us to
    retrieve related objects such as image.users_like.all() or from a user object
    such as user.images_liked.all().
    """
    users_likes = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                         related_name='images_liked',
                                         blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            super(Image, self).save(*args, **kwargs)


    def __str__(self):
        return self.title
