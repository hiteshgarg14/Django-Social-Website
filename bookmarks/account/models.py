from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

"""
In order to keep your code generic, use the get_user_model() method
to retrieve the user model and the AUTH_USER_MODEL setting to refer to
it when defining model's relations to the user model, instead of referring
to the auth User model directly.
"""

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)


class Contact(models.Model):
    user_from = models.ForeignKey(User,related_name='rel_from_set')
    user_to = models.ForeignKey(User, related_name='rel_to_set')
    # This will improve query performance when ordering QuerySets by this field.
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return '{} follows {}'.format(self.user_from, self.user_to)


User.add_to_class('following', models.ManyToManyField('self',
                                                      through=Contact,
                                                      related_name='followers',
                                                      symmetrical=False))
"""
user.followers.all() and user.following.all()

When you use an intermediate model for many-to-many
relationships some of the related manager's methods are disabled,
such as add(), create() or remove(). You need to create or
delete instances of the intermediate model instead.
"""
