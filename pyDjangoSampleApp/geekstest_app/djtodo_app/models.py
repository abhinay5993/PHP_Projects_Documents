from django.db import models
from model_utils import Choices
from django.utils.translation import gettext_lazy as _

# Create your models here.

class MyTodoAppBootStrapModel(models.Model):
    # id = models.BigAutoField(primary_key=True)
    STATUS_CHOICE = Choices(
        (1, "pending", _("pending")),
        (2, "completed", _("completed")),
    )
    id = models.BigAutoField(primary_key=True)
    title = models.TextField()
    status = models.IntegerField(default=STATUS_CHOICE.pending)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Meta:
      db_table = "djtodo_apptable"