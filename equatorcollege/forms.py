from django import forms
from django.contrib.auth.models import User
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from . models import StudentInformation,StudentApproval,UnitRegistration,Usertype

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='First Name')
    last_name = forms.CharField(max_length=30, required=True, help_text='Last Name')
    email = forms.EmailField(max_length=254, help_text='Enter a valid email address')
    

    class Meta:

        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
        
class UsertypeForm(forms.ModelForm):
    class Meta:
        model = Usertype
        fields = ['userid', 'role']


class StudentInformationForm(forms.ModelForm):
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
    MARITAL_STATUS_CHOICES = (
        ('single', 'Single'),
        ('married', 'Married'),
    )
    RELIGION_CHOICES = (
        ('christian', 'Christian'),
        ('muslim', 'Muslim'),
    )
    COUNTY_CHOICES = (
        ('Baringo', 'Baringo'),
        ('Bomet', 'Bomet'),
        ('Bungoma', 'Bungoma'),
        ('Busia', 'Busia'),
        ('Elgeyo Marakwet', 'Elgeyo Marakwet'),
        ('Embu', 'Embu'),
        ('Garissa', 'Garissa'),
        ('Homa Bay', 'Homa Bay'),
    )
    KIN_RELATIONSHIP_CHOICES = (
        ('Father', 'Father'),
        ('Mother', 'Mother'),
        ('Guardian', 'Guardian'),
    )
    LEARNING_MODE_CHOICES = (
        ('Full time', 'Full time'),
        ('Part time', 'Part time'),
        ('Distance', 'Distance learning'),
        ('Weekend', 'Weekend'),
    )
    PREFERRED_SEMESTER_CHOICES = (
        ('Jan/april', 'Jan/April'),
        ('May/aug', 'May/Aug'),
        ('Sept/Dec', 'Sept/Dec'),
        ('schoolbased', 'School based'),
    )
    FINANCING_STUDIES_CHOICES = (
        ('self', 'Self'),
        ('Parent', 'Parent'),
        ('Guardian', 'Guardian'),
        ('Helb', 'Helb'),
        ('sponsorship', 'Sponsorship'),
        ('equator foundation', 'Equator Foundation'),
    )
    PREFERRED_CAMPUS_CHOICES = (
        ('Utawala Campus', 'Utawala Campus'),
        ('Umoja Campus', 'Umoja Campus'),
        ('Guardian', 'Guardian'),
        ('Kisumu Campus', 'Kisumu Campus'),
        ('Rodi Campus', 'Rodi Campus'),
    )
    ACCOMMODATION_CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )

    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    marital_status = forms.ChoiceField(choices=MARITAL_STATUS_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    religion = forms.ChoiceField(choices=RELIGION_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    county = forms.ChoiceField(choices=COUNTY_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    kin_relationship = forms.ChoiceField(choices=KIN_RELATIONSHIP_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    learning_mode = forms.ChoiceField(choices=LEARNING_MODE_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    preferred_semester = forms.ChoiceField(choices=PREFERRED_SEMESTER_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    financing = forms.ChoiceField(choices=FINANCING_STUDIES_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    preferred_campus = forms.ChoiceField(choices=PREFERRED_CAMPUS_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    need_accommodation = forms.ChoiceField(choices=ACCOMMODATION_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = StudentInformation
        fields = [
            'student_id',
            'gender',
            'birthday',
            'marital_status',
            'mobile_no',
            'religion',
            'county',
            'subcounty',
            'permanent_address',
            'postal_code',
            'town',
            'kin_relationship',
            'kin_firstname',
            'kin_lastname',
            'kin_address',
            'kin_town',
            'kin_contact',
            'kin_email',
            'department_id',
            'course_level_id',
            'course_name_id',
            'learning_mode',
            'preferred_semester',
            'schools_attended',
            'financing',
            'preferred_campus',
            'need_accommodation',
            'uploadcertificates',
        ]
        widgets = {
            'student_id': forms.Select(attrs={'class': 'form-control'}),
            'birthday': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'marital_status': forms.Select(attrs={'class': 'form-control'}),
            'mobile_no': forms.NumberInput(attrs={'class': 'form-control'}),
            'religion': forms.Select(attrs={'class': 'form-control'}),
            'subcounty': forms.TextInput(attrs={'class': 'form-control'}),
            'permanent_address': forms.TextInput(attrs={'class': 'form-control'}),
            'postal_code': forms.TextInput(attrs={'class': 'form-control'}),
            'town': forms.TextInput(attrs={'class': 'form-control'}),
            'kin_firstname': forms.TextInput(attrs={'class': 'form-control'}),
            'kin_lastname': forms.TextInput(attrs={'class': 'form-control'}),
            'kin_address': forms.TextInput(attrs={'class': 'form-control'}),
            'kin_town': forms.TextInput(attrs={'class': 'form-control'}),
            'kin_contact': forms.NumberInput(attrs={'class': 'form-control'}),
            'kin_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'department_id': forms.Select(attrs={'class': 'form-control'}),
            'course_level_id': forms.Select(attrs={'class': 'form-control'}),
            'course_name_id': forms.Select(attrs={'class': 'form-control'}),
            'learning_mode': forms.Select(attrs={'class': 'form-control'}),
            'preferred_semester': forms.Select(attrs={'class': 'form-control'}),
            'schools_attended': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'uploadcertificates': forms.FileInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Customizing labels if needed
        self.fields['student_id'].label = 'Select Student'
        self.fields['gender'].label = 'Select Gender'
        # Add more custom labels as needed

    def clean_mobile_no(self):
        mobile_no = self.cleaned_data['mobile_no']
        # Validate mobile number if needed
        return mobile_no
    


APPROVE_CHOICES = [
    ('', 'Select'),
    ('approved', 'Approve'),
    ('declined', 'Decline'),
]

class StudentApprovalForm(forms.ModelForm):
    class Meta:
        model = StudentApproval
        fields = ['approve', 'comment']
        widgets = {
            'approve': forms.Select(choices=APPROVE_CHOICES, attrs={'class': 'form-control'}),
            'comment': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(StudentApprovalForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            if not isinstance(self.fields[field].widget, forms.CheckboxInput):
                self.fields[field].widget.attrs['class'] = 'form-control'


TERM_CHOICES = [
    (1, 'Term 1'),
    (2, 'Term 2'),
]

ICT_CHOICES = [
    ('SAD', 'SAD'),
    ('CA1', 'Computer Application 1'),
    ('CA2', 'Computer Application 2'),
    ('BE', 'Basic Electronics'),
]

BUSINESS_CHOICES = [
    ('accounting', 'Accounting'),
    ('business managemeny', 'Business Management'),
]

PACKAGES_CHOICES = [
    ('introduction', 'Introduction'),
    ('word', 'Ms Word'),
    ('excel', 'Ms Excel'),
    ('publisher', 'Ms Publisher'),
    ('powerpoint', 'Ms Powerpoint'),
    ('access', 'Ms Access'),
    ('internet and emails', 'Internet and Emails'),
]

PROGRAMMING_CHOICES = [
    ('c++', 'C++'),
]

class UnitRegistrationForm(forms.ModelForm):
    # Add the term field to the form as a dropdown (ChoiceField)
    term = forms.ChoiceField(
        choices=TERM_CHOICES,
        label="Select Term",
        widget=forms.Select(),  # This renders it as a dropdown
        required=True,  # By default, it's required
    )
    
    units = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        label="Select Units",
    )

    class Meta:
        model = UnitRegistration
        fields = ['term', 'units']  # Include 'term' in the fields

    def __init__(self, *args, **kwargs):
        # Pop the student object from kwargs and pass it to the form
        student = kwargs.pop('student', None)  
        super().__init__(*args, **kwargs)

        if student:
            admission_number = student.assign_admission.strip()  # Clean the admission number
            print(f"Debug: Admission Number: {admission_number}")  # Debugging output

            admission_prefix1 = admission_number[:5]
            admission_prefix2 = admission_number[:6]
            
            # Initialize the term field as required
            self.fields['term'].required = True

            if admission_prefix1 == 'SCI/D':
                print("Debug: Setting ICT_CHOICES")  # Debugging output
                self.fields['units'].choices = ICT_CHOICES
            elif admission_prefix2 == 'SCI/CP':
                print("Debug: Setting PACKAGES_CHOICES")  # Debugging output
                self.fields['units'].choices = PACKAGES_CHOICES
                # Make term field optional (not required)
                self.fields['term'].required = False
            elif admission_prefix1 == 'SCI/C':
                print("Debug: Setting BUSINESS_CHOICES for SCI/C")  # Debugging output
                self.fields['units'].choices = BUSINESS_CHOICES
            elif admission_prefix1.startswith('SCI/P'):
                print("Debug: Setting PROGRAMMING_CHOICES")  # Debugging output
                self.fields['units'].choices = PROGRAMMING_CHOICES
                # Make term field optional (not required)
                self.fields['term'].required = False
            else:
                print("Debug: Setting GENERAL BUSINESS_CHOICES")  # Debugging output
                self.fields['units'].choices = BUSINESS_CHOICES

    def save(self, student, user, commit=True):
        units = self.cleaned_data['units']
        # For each selected unit, create a UnitRegistration record
        for unit_code in units:
            unit_name = dict(self.fields['units'].choices).get(unit_code)
            unit_registration = UnitRegistration(
                approved_student=student,
                unit_code=unit_code,
                unit_name=unit_name,
                registered_by=user,
                term=self.cleaned_data['term'] if self.cleaned_data.get('term') else None,  # Save the term if it's selected
            )
            if commit:
                unit_registration.save()
        return unit_registration
    
ASSESSMENT_CHOICES = (
    ('CAT 1', 'CAT 1'),
    ('CAT 2', 'CAT 2'),
    ('Main Exam', 'Main Exam'),
)
