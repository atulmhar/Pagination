from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=255,d)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    position = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    hire_date = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    # address = models.TextField(..=True, null=True)
    
    class Meta:
        db_table = 'user'  # Match the exact table name in lowercase
        managed = False  # Prevent Django from managing the table

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
