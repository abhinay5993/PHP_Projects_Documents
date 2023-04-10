from django.db import models

# Create your models here.
class PersonModel(models.Model):
    # id = models.BigAutoField(primary_key=True)
    GENDER = [
        ("M", "Male"),
        ("F", "Female"),
        ("O", "Others"),
    ]
    fname = models.CharField(max_length=50)
    lstName = models.CharField(max_length=50)
    ageVal = models.IntegerField(default=0, null=True)
    emailVal = models.EmailField()
    genderVal = models.CharField(max_length=1, choices=GENDER)
      
# class Meta:
#       db_table = "testTableCustTableName"