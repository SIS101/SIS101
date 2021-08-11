from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.urls import reverse
from . import models, forms

# Create your views here.
@login_required
def index(request):
    template="dashboard/schools/index.html"
    context={}
    l_user=get_object_or_404(User, pk=request.user.id)
    context["l_user"]=l_user
    
    if l_user.has_perm("schools.view_school"):
            
        schools = models.School.objects.all()
        context["schools"]=schools

        return render(request, template, context)
    else:
    
        messages.warning(request, "Access denied.")
        return HttpResponseRedirect(reverse("portal:dashboard"))


@login_required
def add_school(request):
    l_user=get_object_or_404(User, pk=request.user.id)
    
    if l_user.has_perm("schools.add_school"):
        
        template="dashboard/schools/add-school.html"
        context={}

        form = forms.SchoolForm()
        context["form"]=form

        if request.method == "POST":
            pform = forms.SchoolForm(request.POST)
            if pform.is_valid():
                pform.save()
                messages.success(request, "School successfully added!")
            else:
                messages.error(request, "Failed to add school.")
                context["form"]=pform

        return render(request, template, context)
        
    else:
    
        messages.warning(request, "Access denied.")
        return HttpResponseRedirect(reverse("schools:index"))

@login_required
def view_school(request, school_id):
    l_user=get_object_or_404(User, pk=request.user.id)
    
    if l_user.has_perm("schools.view_school"):
        
        template="dashboard/schools/view-school.html"
        context={}

        school = models.School.objects.get(pk=school_id)
        programmes = models.Programme.objects.filter(school=school)
        context["school"]=school
        context["programmes"]=programmes

        return render(request, template, context)
        
    else:
    
        messages.warning(request, "Access denied.")
        return HttpResponseRedirect(reverse("schools:index"))

@login_required
def add_programme(request, school_id):
    l_user=get_object_or_404(User, pk=request.user.id)
    
    if l_user.has_perm("schools.add_programme"):
        template="dashboard/schools/add-programme.html"
        context={}

        school = models.School.objects.get(pk=school_id)
        context["school"]=school
        form = forms.ProgrammeForm({"school": school_id})
        context["form"]=form

        if request.method == "POST":
            pform = forms.ProgrammeForm(request.POST)
            if pform.is_valid():
                pform.save()
                messages.success(request, "Programme successfully added!")
            else:
                messages.error(request, "Failed to add programme.")
                context["form"]=pform

        return render(request, template, context)

    else:
        messages.warning(request, "Access denied.")
        return HttpResponseRedirect(reverse("schools:view-school", args=[school_id]))

@login_required
def view_programme(request, programme_id):
    l_user=get_object_or_404(User, pk=request.user.id)
    
    if l_user.has_perm("schools.view_programme"):
        template="dashboard/schools/view-programme.html"
        context={}

        programme = models.Programme.objects.get(pk=programme_id)
        context["programme"]=programme
        courses=models.Course.objects.filter(programme=programme)
        context["courses"]=courses

        return render(request, template, context)    
        
    else:
        messages.warning(request, "Access denied.")
        return HttpResponseRedirect(reverse("schools:index"))

@login_required
def add_course(request, programme_id):
    l_user=get_object_or_404(User, pk=request.user.id)
    
    if l_user.has_perm("shools.add_course"):
        template="dashboard/schools/add-course.html"
        context={}

        form = forms.CourseForm({"programme":programme_id})
        context["form"]=form
        programme = models.Programme.objects.get(pk=programme_id)
        context["programme"]=programme

        if request.method == "POST":
            pform = forms.CourseForm(request.POST)
            if pform.is_valid():
                pform.save()
                messages.success(request, "Course successfully added!")
            else:
                messages.error(request, "Failed to add Course.")
                context["form"]=pform

        return render(request, template, context)
    
    else:
        messages.warning(request, "Access denied.")
        return HttpResponseRedirect(reverse("schools:view-programme", args=[programme_id]))

@login_required
def edit_course(request, programme_id, course_id):
    l_user = get_object_or_404(User, pk=request.user.id)
    if l_user.has_perm("schools.vew_course"):
        template="dashboard/schools/edit-course.html"
        context={"l_user":l_user}

        course = models.Course.objects.get(pk=course_id)
        form = forms.CourseForm(instance=course)
        context["form"]=form
        programme = models.Programme.objects.get(pk=programme_id)
        context["programme"]=programme

        if request.method == "POST":
            if request.user.has_perm("schools.change_course"):
                pform = forms.CourseForm(request.POST, instance=course)
                if pform.is_valid():
                    pform.save()
                    messages.success(request, "Course successfully updated!")
                    return HttpResponseRedirect(reverse("schools:edit-course", kwargs={"programme_id":programme_id, "course_id":course_id}))
                else:
                    messages.error(request, "Failed to update Course.")
                    context["form"]=pform
            else:
                messages.error(request, "Insufficient privilages.")

    else:
        messages.warning(request, "Access denied.")
        return HttpResponseRedirect(reverse("schools:view-programme", kwargs={"programme_id":programme_id}))

    return render(request, template, context)

@login_required
def delete_object(request, object_type, object_id):
    l_user = get_object_or_404(User, pk=request.user.id)
    if l_user.has_perms(["schools.delete_school","schools.delete_programme","schools.delete_course"]):
        if object_type == "school":
            models.School.objects.get(pk=object_id).delete()
            messages.success(request, "Deleted!")
            return HttpResponseRedirect(reverse("schools:index"))
        elif object_type == "programme":
            obj = models.Programme.objects.get(pk=object_id)
            bid = obj.school.pk
            obj.delete()
            messages.success(request, "Deleted!")
            return HttpResponseRedirect(reverse("schools:view-school", kwargs={"school_id": bid}))
        elif object_type == "course":
            obj = models.Course.objects.get(pk=object_id)
            bid = obj.programme.pk
            obj.delete()
            messages.success(request, "Deleted!")
            return HttpResponseRedirect(reverse("schools:view-programme", kwargs={"programme_id": bid}))
        else:
            messages.error(request, "Could not delete object")
            return HttpResponseRedirect(reverse("schools:index"))
    else:
        messages.warning(request, "Access denied.")
        return HttpResponseRedirect(reverse("schools:index"))