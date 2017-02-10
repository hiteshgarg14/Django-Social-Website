from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


"""
With this basic model, we can only store actions such as User X did something. We
need an extra ForeignKey field in order to save actions that involve a target object,
such as User X bookmarked image Y or User X is now following user Y. As you
already know, a normal ForeignKey can only point to one other model. Instead,
we need a way for the action's target object to be an instance of any existing model.
This is where the Django contenttypes framework comes on the scene.
"""
class Action(models.Model):
    user = models.ForeignKey(User, related_name='actions', db_index=True)
    verb = models.CharField(max_length=225)
    """
    In generic relations ContentType objects play the role of pointing to the model used
    for the relationship.
    """
    target_ct = models.ForeignKey(ContentType, blank=True, null=True,related_name='target_obj')
    # limit_choices_to
    target_id = models.PositiveIntegerField(null=True,blank=True,db_index=True )
    target = GenericForeignKey('target_ct', 'target_id')
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ('-created',)
