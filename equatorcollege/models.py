from django.db import models
from django.contrib.auth.models import User

class Usertype(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    role = models.CharField(max_length=20)  # Adjust max_length as needed

    def __str__(self):
        return f"{self.userid.username} - {self.role}"


class Department(models.Model):
    department_code=models.CharField(max_length=10)
    department_name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.department_name


class CourseLevel(models.Model):
    course_level_code=models.CharField(max_length=10)
    courselevel_name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.courselevel_name

class CourseName(models.Model):
    course_name = models.CharField(max_length=50)

    def __str__(self):
        return self.course_name

class StudentInformation(models.Model):
    student_id = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=50)
    birthday = models.DateField()
    marital_status = models.CharField(max_length=50)
    mobile_no = models.PositiveIntegerField()
    religion = models.CharField(max_length=50)
    county = models.CharField(max_length=50)
    subcounty = models.CharField(max_length=50)
    permanent_address = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=20)
    town = models.CharField(max_length=50)
    kin_relationship = models.CharField(max_length=50)
    kin_firstname = models.CharField(max_length=50)
    kin_lastname = models.CharField(max_length=50)
    kin_address = models.CharField(max_length=255)
    kin_town = models.CharField(max_length=50)
    kin_contact = models.IntegerField()
    kin_email = models.EmailField()
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE)
    course_level_id = models.ForeignKey(CourseLevel, on_delete=models.CASCADE)
    course_name_id = models.ForeignKey(CourseName, on_delete=models.CASCADE)
    learning_mode = models.CharField(max_length=30)
    preferred_semester = models.CharField(max_length=50)
    schools_attended = models.TextField(max_length=255)
    financing = models.CharField(max_length=50)
    preferred_campus = models.CharField(max_length=50)
    need_accommodation = models.CharField(max_length=50)
    registered_at = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)
    approved_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='approvals')
    uploadcertificates=models.FileField(upload_to='mediafiles',blank=True,null=True)

    def __str__(self):
        return f'{self.student.username} - {self.course_name}'

class StudentApproval(models.Model):
    student = models.OneToOneField(StudentInformation, on_delete=models.CASCADE)
    assign_admission = models.CharField(max_length=30, blank=True)
    approve = models.CharField(max_length=30)
    comment=models.CharField(max_length=100,blank=True,unique=False)
    approved_by = models.ForeignKey(User, on_delete=models.CASCADE)
    approval_date = models.DateTimeField(auto_now_add=True)
    is_unit_registered = models.BooleanField(default=False)
    is_mark_added = models.BooleanField(default=False)
    
    def __str__(self):
        return f'Approval for {self.student.student.username}'


class UnitRegistration(models.Model):
    approved_student = models.ForeignKey(StudentApproval, on_delete=models.CASCADE)
    term=models.IntegerField(blank=True)
    unit_code=models.CharField(max_length=20)
    unit_name=models.CharField(max_length=50)
    registration_date = models.DateTimeField(auto_now_add=True)
    registered_by = models.ForeignKey(User, on_delete=models.CASCADE)
    is_mark_added = models.BooleanField(default=False)


