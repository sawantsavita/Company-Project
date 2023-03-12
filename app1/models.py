from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=255, null=True)
    no_of_employees = models.IntegerField(null=True)
    est_date = models.DateField(auto_now=True, null=True)
    is_govt_registered = models.BooleanField(default=True, null=True)
    is_active = models.BooleanField(default=False)
    
    class Meta:
        db_table = 'company'
        
    def __str__(self):
        return self.name
    
    def show_details(self):
        return f"""
Name = {self.name}
Address = {self.address}
No of employees = {self.no_of_employees}
Established Date = {self.est_date}
Is Govt. Recognised = {self.is_govt_registered}    
"""