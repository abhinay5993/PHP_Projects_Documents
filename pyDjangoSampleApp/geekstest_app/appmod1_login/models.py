from django.db import models
from model_utils import Choices
from django.utils.translation import gettext_lazy as _

# Create your models here.


class PersonModel(models.Model):
    # id = models.BigAutoField(primary_key=True)
    GENDER = Choices(
        (1, "male", _("male")),
        (2, "female", _("female")),
        (3, "others", _("others")),
    )
    fname = models.CharField(max_length=50)
    lstName = models.CharField(max_length=50)
    emailVal = models.EmailField()
    genderVal = models.IntegerField(choices=GENDER, default=GENDER.male)
    ageVal = models.IntegerField(default=0, null=True)

# class Meta:
#       db_table = "testTableCustTableName"