# exec(open(r"D:\Python\company_proj\app1\db_shell.py").read())

from app1.models import Company
from django.contrib.auth.models import User

# User.objects.create_user(username='Kiran', password='Python@123')
# User.objects.create_user(username="Mihir", password="Python@123")
# print(User.objects.all())

# c1 = Company(name="Cipla", address="rasayani", no_of_employees=12000, est_date="7/1/2023", is_govt_registered=True)
# c2 = Company(name="Dr. Reddy's", address="Hyderabad", no_of_employees=25000, est_date="12/12/2022", is_govt_registered=True)
# c1.save()
# c2.save()
# print(Company.objects.all())

# Company.objects.using("SECOND_DB").create(name="Wipro", address="Pune", no_of_employees=25000, est_date="12/12/2022", is_govt_registered=True)
print(Company.objects.using("SECOND_DB").all())