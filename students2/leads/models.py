from django.db import models

class Registers(models.Model):
	st_name = models.CharField(max_length=250)
	st_mobile = models.CharField(max_length=250)
	st_email = models.CharField(max_length=150)
	st_course = models.CharField(max_length=2500)
	st_sourse = models.CharField(max_length=250)
	st_lead_status = models.CharField(max_length=250)
	st_demo_date = models.CharField(max_length=150)
	st_counsler = models.CharField(max_length=2500)
	st_remarks = models.CharField(max_length=2500)
	def __str__(self):
		return self.st_name+ "--"+self.st_course

class Joinings(models.Model):
	course = models.CharField(max_length=250)
	name = models.CharField(max_length=250)
	complection_date = models.CharField(max_length=150)
	date_join = models.CharField(max_length=2500)
	course_fee = models.CharField(max_length=250)
	instructor = models.CharField(max_length=250)
	aadhar_number = models.CharField(max_length=150)
	mobile = models.CharField(max_length=2500)
	email = models.CharField(max_length=2500)
	remarks = models.CharField(max_length=2500)
	Status = models.CharField(max_length=2500)
	def __str__(self):
		return self.name+ "--"+self.course
class Course_names(models.Model):
	course = models.CharField(max_length=250)
	name = models.CharField(max_length=250)
	def __str__(self):
		return self.course
