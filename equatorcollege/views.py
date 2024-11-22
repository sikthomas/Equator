from django.shortcuts import render,redirect,get_object_or_404
from .forms import UserRegistrationForm,StudentInformationForm,StudentApprovalForm,UnitRegistrationForm
from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth import login, authenticate,logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import StudentInformation,Department,CourseLevel,CourseName,StudentApproval,UnitRegistration
from django.db.models import Max
from django.utils.timezone import now
from django.contrib.auth.decorators import login_required

def index(request):
    logged_in_user = request.user
    student_count = StudentInformation.objects.count()
    approval_count = StudentApproval.objects.count()

    ict_students = StudentInformation.objects.filter( department_id__department_code='SCI').count()
    business = StudentInformation.objects.filter( department_id__department_code='SBM').count()
    social_scinces = StudentInformation.objects.filter( department_id__department_code='SHS').count()

    try:
        myacademic_info = StudentInformation.objects.get(student_id=logged_in_user)
    except StudentInformation.DoesNotExist:
        myacademic_info = None

    if logged_in_user.is_superuser and logged_in_user.is_staff:
        return render(request, 'admindashboard/index.html', {'student_count': student_count,'approval_count': approval_count,'ict_students':ict_students,'business':business,'social_scinces':social_scinces})
    elif logged_in_user.is_superuser and not logged_in_user.is_staff:
        return render(request, 'registrar/index.html', {'student_count': student_count,'approval_count': approval_count,'ict_students':ict_students,'business':business,'social_scinces':social_scinces})
    elif not logged_in_user.is_superuser and logged_in_user.is_staff:
        return render(request, 'studentadmindashboard/index.html', {'student_count': student_count,'approval_count': approval_count,'ict_students':ict_students,'business':business,'social_scinces':social_scinces})
    else:
        return render(request, 'student/index.html', {'myacademic_info':myacademic_info})
    
def ict_list(request ):
    logged_in_user=request.user
    ict_students_list = StudentInformation.objects.filter( department_id__department_code='SCI')
    
    if logged_in_user.is_superuser and logged_in_user.is_staff:
        return render(request, 'admindashboard/ictlist.html', {'ict_students_list':ict_students_list})
    elif logged_in_user.is_superuser and not logged_in_user.is_staff:
         return render(request, 'registrar/ictlist.html', {'ict_students_list':ict_students_list})
    else:
        return render(request, 'studentadmindashboard/ictlist.html', {'ict_students_list':ict_students_list})

def bcom_list(request ):
    logged_in_user=request.user
    business_list = StudentInformation.objects.filter( department_id__department_code='SBM')

    if logged_in_user.is_superuser and logged_in_user.is_staff:
        return render(request, 'admindashboard/business.html', {'business_list':business_list})
    elif logged_in_user.is_superuser and not logged_in_user.is_staff:
         return render(request, 'registrar/business.html', {'business_list':business_list})
    else:
        return render(request, 'studentadmindashboard/business.html', {'business_list':business_list})
    
def shs_list(request ):
    logged_in_user=request.user
    social_scinces_list = StudentInformation.objects.filter( department_id__department_code='SHS')

    if logged_in_user.is_superuser and logged_in_user.is_staff:
        return render(request, 'admindashboard/shs.html', {'social_scinces_list':social_scinces_list})
    elif logged_in_user.is_superuser and not logged_in_user.is_staff:
         return render(request, 'registrar/shs.html', {'social_scinces_list':social_scinces_list})
    else:
        return render(request, 'studentadmindashboard/shs.html', {'social_scinces_list':social_scinces_list})


def signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user=user)
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'sharedfiles/signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    
    return render(request, 'sharedfiles/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def assign_role(request):
    userinfo = User.objects.all()
    
    if request.method == 'POST':
        user_id = request.POST.get('userid')
        role = request.POST.get('role')
        
        if user_id and role:
            user = get_object_or_404(User, pk=user_id)
            
            if role == 'admin':
                user.is_superuser = True
                user.is_staff = True
            elif role == 'registrar':
                user.is_superuser = True
                user.is_staff = False
            elif role == 'studentadmin':
                user.is_superuser = False
                user.is_staff = True
            elif role == 'student':
                user.is_superuser = False
                user.is_staff = False
            user.save()
            return redirect('index')  # Redirect to success page after saving
        else:
            print("User ID or role not provided.")  # Print errors for debugging
    
    return render(request, 'admindashboard/assign_role.html', {'userinfo': userinfo})


@login_required
def admission(request):
    user = request.user
    students = User.objects.all() 
    departments = Department.objects.all()
    courselevels = CourseLevel.objects.all()
    coursenames = CourseName.objects.all()

    if request.method == 'POST':
        form = StudentInformationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            if not user.is_superuser and user.is_staff:
                return redirect('studentadmin')
            if user.is_superuser and not user.is_staff:
                return redirect('registrar')
            else:
                return redirect('index')  # assuming 'admindashboard:index' is the correct URL pattern
    else:
        form = StudentInformationForm()
    if not user.is_superuser and user.is_staff:
        return render(request, 'studentadmindashboard/admission.html', {'students': students, 'departments': departments, 'courselevels': courselevels, 'coursenames': coursenames, 'form': form})
    elif user.is_superuser and not user.is_staff:
        return render(request, 'registrar/admission.html', {'students': students, 'departments': departments, 'courselevels': courselevels, 'coursenames': coursenames, 'form': form})
    else:
        return render(request, 'admindashboard/admission.html', {'students': students, 'departments': departments, 'courselevels': courselevels, 'coursenames': coursenames, 'form': form})

@login_required
def admissionlist(request):
    user = request.user
    students = StudentInformation.objects.all()
    approved_students = StudentInformation.objects.all()
    if not user.is_superuser and user.is_staff:
        return render(request, 'studentadmindashboard/admissionlist.html', {'students': students,'approved_students':approved_students})
    elif user.is_superuser and user.is_staff:
        return render(request, 'admindashboard/admissionlist.html', {'students': students,'approved_students':approved_students})
    else:
        return render(request, 'registrar/admissionlist.html', {'students': students,'approved_students':approved_students})

@login_required
def studentdetails(request, pk):
    user = request.user
    students = StudentInformation.objects.get(pk=pk)

    if user.is_superuser and user.is_staff:
        return render(request, 'admindashboard/studentdetails.html', {'students': students})
    if user.is_superuser and not user.is_staff:
        return render(request, 'registrar/studentdetails.html', {'students': students})
    else:
        return render(request, 'studentadmindashboard/studentdetails.html', {'students': students})

@login_required
def update_student_information(request, pk):
    user = request.user
    student_info = get_object_or_404(StudentInformation, pk=pk)
    if request.method == "POST":
        form = StudentInformationForm(request.POST, instance=student_info)
        if form.is_valid():
            form.save()
            if user.is_superuser and user.is_staff:
                return redirect('index')  # Redirect to your desired page after saving
            elif user.is_superuser and not user.is_staff:
                return redirect('registrar')  # Redirect to your desired page after saving
            else:
                return redirect('studentadmin')  # Redirect to your desired page after saving
            
    else:
        form = StudentInformationForm(instance=student_info)
        if user.is_superuser and user.is_staff:
            return render(request, 'admindashboard/update_student_information.html', {'form': form})
        elif user.is_superuser and user.is_staff:
            return render(request, 'registrar/update_student_information.html', {'form': form})
        else:
            return render(request, 'studentadmindashboard/update_student_information.html', {'form': form})


@login_required
def approve_student(request, pk):
    user = request.user
    student_info = get_object_or_404(StudentInformation, pk=pk)
    if request.method == 'POST':
        form = StudentApprovalForm(request.POST)
        if form.is_valid():
            student_info.is_approved = True
            student_info.approved_by = request.user
            student_info.save()

            approve_student = form.save(commit=False)
            approve_student.student = student_info
            approve_student.approved_by = request.user
            approve_student.approval_date = now()

            department_code = student_info.department_id.department_code
            course_level_code = student_info.course_level_id.course_level_code
            year = now().year

            # Determine the prefix based on course level
            if course_level_code.lower() == 'dip':
                prefix = f"{department_code.upper()}/D"
            elif course_level_code.lower() == 'cert':
                prefix = f"{department_code.upper()}/C"
            elif course_level_code.lower() == 'art':
                prefix = f"{department_code.upper()}/A"
            elif course_level_code.lower() == 'cp':
                prefix = f"{department_code.upper()}/CP"
            elif course_level_code.lower() == 'p':
                prefix = f"{department_code.upper()}/P"
            else:
                prefix = f"{department_code.upper()}/O"

            # Get the last assigned number for the given prefix and increment it
            last_admission = StudentApproval.objects.filter(assign_admission__startswith=prefix).aggregate(
                Max('assign_admission'))
            if last_admission['assign_admission__max']:
                last_number = int(last_admission['assign_admission__max'].split('/')[1][1:])
                new_number = last_number + 1
            else:
                new_number = 1

            # Format the new admission number
            assign_admission = f"{prefix}{new_number:03d}/{year}"

            approve_student.assign_admission = assign_admission
            approve_student.save()

            if user.is_superuser and user.is_staff:
                return redirect('index')  # Redirect to a success page or another appropriate page
            else:
                return redirect('registrar') 

        else:
            # Handle form validation errors if needed
            print(form.errors)  # Output form errors to console for debugging
    else:
        form = StudentApprovalForm()
        if user.is_superuser and user.is_staff:
            return render(request, 'admindashboard/approvestudent.html', {'form': form, 'student_info': student_info})
        else:
            return render(request, 'registrar/approvestudent.html', {'form': form, 'student_info': student_info})

@login_required
def approvedlist(request):
    user = request.user
    approved_students = StudentApproval.objects.all()
    if not user.is_superuser and user.is_staff:
        return render(request, 'studentadmindashboard/approvedlist.html', {'approved_students': approved_students})
    elif user.is_superuser and not user.is_staff:
        return render(request, 'registrar/approvedlist.html', {'approved_students': approved_students})
    else:
        return render(request, 'admindashboard/approvedlist.html', {'approved_students': approved_students})

    
@login_required
def approvedlist_addunits(request):
    user = request.user
    approved_students = StudentApproval.objects.all()
    if user.is_superuser and not user.is_staff:
        return render(request, 'registrar/approvedlist_addunits.html', {'approved_students': approved_students})
    else:
        return render(request, 'admindashboard/approvedlist_addunits.html', {'approved_students': approved_students})

@login_required
def approved_student_details(request,pk):
    user = request.user
    students = StudentApproval.objects.get(pk=pk)
    if user.is_superuser and user.is_staff:
        return render(request, 'admindashboard/approved_student_details.html', {'students': students})
    elif user.is_superuser and not user.is_staff:
        return render(request, 'registrar/approved_student_details.html', {'students': students})
    else:
        return render(request, 'studentadmindashboard/approved_student_details.html', {'students': students})

@login_required
def delete_student(request, pk):
    user = request.user
    student =StudentInformation.objects.get(pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('index')  
    if user.is_superuser and user.is_staff:
        return render(request, 'admindashboard/delete_student.html', {'student': student})
    else:
        return render(request, 'registrar/delete_student.html', {'student': student})
    
@login_required
def register_units(request, pk):
    logged_in_user = request.user
    student = get_object_or_404(StudentApproval, id=pk)
    
    if request.method == 'POST':
        form = UnitRegistrationForm(request.POST, student=student)  # Pass student to form
        if form.is_valid():
            # Save the selected units for this student
            unit_registration = form.save(student=student, user=request.user, commit=True)

            # Update the 'is_unit_registered' field to True on the StudentApproval model
            student.is_unit_registered = True
            student.save()  # Save the changes to StudentApproval

            # Redirect to the appropriate page based on the user's role
            if logged_in_user.is_superuser and logged_in_user.is_staff:
                return redirect('index') 
            else:
                return redirect('registrar:index')
    else:
        form = UnitRegistrationForm(student=student) 
    if logged_in_user.is_superuser and logged_in_user.is_staff:
        return render(request, 'admindashboard/register_units.html', {'form': form, 'student': student})
    else:
        return render(request, 'registrar/register_units.html', {'form': form, 'student': student})

@login_required
def view_units(request, pk):
    logged_in_user = request.user
    units = UnitRegistration.objects.filter(approved_student__student__pk=pk)

    if logged_in_user.is_superuser and logged_in_user.is_staff:
        return render(request, 'admindashboard/view_units.html', {'units': units})
    elif logged_in_user.is_superuser and not logged_in_user.is_staff:
        return render(request, 'registrar/view_units.html', {'units': units})
    elif not logged_in_user.is_superuser and logged_in_user.is_staff:
        return render(request, 'studentadmindashboard/view_units.html', {'units': units})
    else:
        return render(request, 'student/view_units.html', {'units': units})
    


@login_required
def view_myunits(request):
    logged_in_user = request.user

    # Fetch the StudentInformation instance for the logged-in user
    try:
        student_info = StudentInformation.objects.get(student_id=logged_in_user)
    except StudentInformation.DoesNotExist:
        student_info = None
        units = None

    # If student info exists, filter by it to get the registered units
    if student_info:
        units = UnitRegistration.objects.filter(approved_student__student=student_info)
        return render(request, 'student/view_units.html', {'units': units})
    else:
         return render(request, 'student/no_unit.html')