from . import models

def get_school(id):
    schools=models.School.objects.get(pk=id)
    
    return schools