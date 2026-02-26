from django.core.management.base import BaseCommand
from faker import Faker
from studentorg.models import College, Program, Organization, Student, OrgMember

class Command(BaseCommand):
    help = 'Create initial data for the application'

    def handle(self, *args, **kwargs):
        self.create_colleges()
        self.create_programs()
        self.create_organization(10)
        self.create_students(50)
        self.create_membership(10)

    def create_colleges(self):
        colleges = ['College of Engineering', 'College of Arts and Sciences', 'College of Business']
        for name in colleges:
            College.objects.get_or_create(college_name=name)
        self.stdout.write(self.style.SUCCESS('Colleges created successfully.'))

    def create_programs(self):
        college = College.objects.first()
        programs = ['BS Information Technology', 'BS Computer Science', 'BS Civil Engineering']
        for name in programs:
            Program.objects.get_or_create(prog_name=name, college=college)
        self.stdout.write(self.style.SUCCESS('Programs created successfully.'))

    def create_organization(self, count):
        fake = Faker()
        for _ in range(count):
            Organization.objects.create(
                name=fake.company(),
                college=College.objects.order_by('?').first(),
                description=fake.sentence()
            )
        self.stdout.write(self.style.SUCCESS('Initial data for organization created successfully.'))

    def create_students(self, count):
        fake = Faker('en_PH')
        for _ in range(count):
            # We pick a random program from the ones we just created
            random_program = Program.objects.order_by('?').first()
            Student.objects.create(
                student_id=f"{fake.random_int(2020, 2024)}-{fake.random_int(1,8)}-{fake.random_number(digits=4)}",
                lastname=fake.last_name(),
                firstname=fake.first_name(),
                middlename=fake.last_name(),
                program=random_program
            )
        self.stdout.write(self.style.SUCCESS('Initial data for students created successfully.'))

    def create_membership(self, count):
        fake = Faker()
        for _ in range(count):
            OrgMember.objects.create(
                student=Student.objects.order_by('?').first(),
                organization=Organization.objects.order_by('?').first(),
                date_joined=fake.date_between(start_date="-2y", end_date="today")
            )
        self.stdout.write(self.style.SUCCESS('Initial data for student organization created successfully.'))
