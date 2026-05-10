from rest_framework import serializers
from studentorg.models import College, Student, Program

# Keep this one!
class CollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = College
        fields = '__all__'

# Add this one
class StudentSerializer(serializers.ModelSerializer):
    program_name = serializers.CharField(source='program.prog_name', read_only=True)

    class Meta:
        model = Student
        fields = ['id', 'student_id', 'lastname', 'firstname', 'middlename', 'program', 'program_name']
        read_only_fields = ['program_name']
        
# And add this one
class ProgramSerializer(serializers.ModelSerializer):
    # This 'student_set' pulls all students linked to this program
    students = StudentSerializer(many=True, read_only=True, source='student_set')

    class Meta:
        model = Program
        fields = ['id', 'prog_name', 'college', 'students']
