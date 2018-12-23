# IMPORT

from django.db import models
# from django.utils import timezone
import datetime


# Create your models here.


class GenericError(Exception):
	def __init__(self, message):
		# Call the base class constructor with the parameters it needs
		super().__init__(message)


class Project(models.Model):
	title = models.CharField(max_length=255)
	start_project = models.DateTimeField('start project')
	end_project = models.DateTimeField('end project')
	'''if start_project > end_project:
		raise GenericError("Project start date can not be longer than Project end date!")'''

	@classmethod
	def create(cls, title, start_project, end_project):
		proj = cls(title = title, start_project = start_project, end_project = end_project)
		proj.save()
		return proj

	def create_calendar_plan(self, plan_title, plan_type, month):
		CalendarPlan.create(plan_title = plan_title, plan_type = plan_type, month = month, project_id = self.id)
	def get_project_uid(self):
		return self.id
	def get_project_title(self) -> str:
		return self.title
	def get_project_start(self) -> datetime:
		return self.start_project
	def get_project_end(self) -> datetime:
		return self.end_project
	def get_project_plans(self) -> list:
		return self.calendarplan_set.all()


class CalendarPlan(models.Model):
	plan_title = models.CharField(max_length=255, unique=True)
	plan_type = models.CharField(max_length=255, unique=True)
	month = models.CharField(max_length=32, unique=True)
	project = models.ForeignKey(Project, on_delete=models.CASCADE)
	'''if plan_type is None:
		raise GenericError("Incorrect plan type!")
	if plan_title is None:
		raise GenericError("Incorrect plan title!")'''

	@classmethod
	def create(cls, plan_title, plan_type,month, project_id):
		calendar_plan = cls(plan_title = plan_title, plan_type = plan_type, month = month, project_id = project_id)
		calendar_plan.save()
		return calendar_plan

	def create_task(self, title, start_date, end_date, progress):
		Task.create(title = title, start_date = start_date, end_date = end_date, progress = progress, calendar_plan_id = self.id)
	def get_plan_uid(self):
		return self.id
	def get_calendar_plan_title(self) -> str:
		return self.plan_title
	def get_calendar_plan_type(self) -> str:
		return self.plan_type
	def get_calendar_plan_month(self) -> str:
		return self.month
	def get_calendar_plan_tasks(self) -> list:
		return self.task_set.all()


class Task(models.Model):
	pass

class Task(models.Model):
	title = models.CharField(max_length=255)
	start_date = models.DateTimeField()
	end_date = models.DateTimeField()
	progress = models.IntegerField()
	calendar_plan = models.ForeignKey(CalendarPlan, on_delete = models.CASCADE)
	'''if progress > 100 or progress < 0:
		raise GenericError("Incorrect task progress!")
	if start_date > end_date:
		raise GenericError("Incorrect task date!")
	if title is None:
		raise GenericError("Incorrect task title!")'''

	@classmethod
	def create(cls, title, start_date, end_date, progress, calendar_plan_id):
		task = cls(title = title, start_date = start_date, end_date = end_date, progress = progress, calendar_plan_id = calendar_plan_id)
		task.save()
		return task

	def get_task_uid(self):
		return self.id
	def get_task_title(self) -> str:
		return self.title
	def get_task_start_date(self) -> datetime.datetime:
		return self.start_date
	def get_task_end_date(self) -> datetime.datetime:
		return self.end_date
	def get_task_progress(self) -> int:
		return self.progress
	def set_start_date(self, start_date: datetime):
		self.update(start_date = start_date)
		#'''if self.start_date > self.end_date:
		#	raise GenericError("Task start date can not be longer than Task end date!")'''
	def set_end_date(self, end_date: datetime):
		self.update(end_date = end_date)
		#'''if self.end_date < self.start_date:
		#	raise GenericError("Task end date cannot be less than Task start date!")'''
	def set_progress(self, progress: int):
		if 0 < progress < 100:
			self.update(progress = progress)
		else:
			raise GenericError("Incorrect task progress!")