from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
LESSON_CHOICES = (
    ("1", "MEDICAL BIOLOGY"),
    ("2", "MEDICAL BIOCHEMISTRY"),
    ("3", "BIOPHYSICS"),
    ("4", "PHYSIOLOGY"),
    ("5", "MEDICAL GENETICS"),
    ("6", "HİSTOLOGY"),
    ("7", "ANATOMY"),
    ("8", "MICRO"),
    ("9", "IMMUN"),
    ("10", "PATHOLOGY"),
    ("11", "BIOIST"),
    ("12", "PED"),
    ("13", "PHARMACOLOGY"),
    ("14", "INTERNAL MEDICINE"),
    ("15", "ANATOMY"),
    ("16", "UROLOGY"),
    ("17", "RADIOLOGY"),
    ("18", "OBSTETRICS and GYNECOLOGY"),
    ("19", "CHILD HEALTH"),
    ("20", "GENERAL SURGERY"),
    ("21", "ORTHOPEDICS"),
    ("22", "DERMATOLOGY"),
    ("23", "MED. GENETICS"),
    ("24", "NEUROLOGY"),
    ("25", "NEUROSURGERY"),
    ("26", "CARDIO"),
    ("27", "INFECTIOUS DIS"),
    ("28", "PUBLIC HEALTH"),
    ("29", "BASIC STATISTICS"),
)

COPY_OR_NOTE = ( 
    ("copy", "Çıkmış"),
    ("note", "Ders Notu")
)

class Academician(models.Model):
    name = models.CharField(max_length=264)
    copy = models.SmallIntegerField(validators=[MaxValueValidator(5),MinValueValidator(1)])
    attendance = models.SmallIntegerField(validators=[MaxValueValidator(5),MinValueValidator(1)])
    note = models.SmallIntegerField(validators=[MaxValueValidator(5),MinValueValidator(1)])
    lecture = models.SmallIntegerField(validators=[MaxValueValidator(5),MinValueValidator(1)])
    description = models.TextField()
    

    def __str__(self):
        return self.name 
    

class Lesson(models.Model):
    title = models.CharField(max_length=264)
    name = models.CharField(max_length = 20,choices = LESSON_CHOICES, default = '1')
    copy_or_note = models.CharField(max_length = 20,choices = COPY_OR_NOTE, default = 'copy')
    # link = models.URLField()
    class_year = models.SmallIntegerField(validators=[MaxValueValidator(5),MinValueValidator(1)])
    lesson_year = models.SmallIntegerField()
    academician = models.ForeignKey(Academician, on_delete= models.PROTECT)
    description = models.TextField()
    
    def __str__(self):
        return self.name
        
        

