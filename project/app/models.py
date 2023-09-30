from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
LESSON_CHOICES = (
    ("1", "MEDİKAL BİYOLOJİ (MEDICAL BIOLOGY)"),
    ("2", "MEDİKAL BİYOLKİMYA (MEDICAL BIOCHEMISTRY)"),
    ("3", "BİOFİZİK (BIOPHYSICS)"),
    ("4", "FİZYOLOJİ (PHYSIOLOGY)"),
    ("5", "GENETİK (MEDICAL GENETICS)"),
    ("6", "HİSTOLOJİ (HİSTOLOGY)"),
    ("7", "ANATOMİ (ANATOMY)"),
    ("8", "MİKROBİYOLOJİ (MICROBIOLOGY)"),
    ("9", "İMMUNOLOJİ (IMMUNOLOGY)"),
    ("10", "PATOLOJİ (PATHOLOGY)"),
    ("11", "BİOİSTATİSTİK (BIOSTATISTICS)"),
    ("12", "ÇOCUK CERRAHİ (PED SURGERY)"),
    ("13", "FARMAKOLOJİ (PHARMACOLOGY)"),
    ("14", "DAHİLİYE (INTERNAL MEDICINE)"),
    ("15", "PLASTİK CERRAHİ (PLASTİC SURGERY)"),
    ("16", "ÜROLOJİ (UROLOGY)"),
    ("17", "RADYOLOJİ (RADIOLOGY)"),
    ("18", "KADIN DOĞUM (OBSTETRICS and GYNECOLOGY)"),
    ("19", "PEDİATRİ (PEDIATRICS)"),
    ("20", "GENEL CERRAHİ (GENERAL SURGERY)"),
    ("21", "ORTOPEDİ (ORTHOPEDICS)"),
    ("22", "DERMATOLOJİ (DERMATOLOGY)"),
    ("23", "ANESTEZİ (ANESTHETICS)"),
    ("24", "NÖROLOJİ (NEUROLOGY)"),
    ("25", "BEYİN SİNİR CERRAHİ (NEUROSURGERY)"),
    ("26", "KARDİYOLOJİ (CARDIO)"),
    ("27", "ENFEKSİYON HASTALIKLARI (INFECTIOUS DISEASES)"),
    ("28", "HALK SAĞLIĞI (PUBLIC HEALTH)"),
    ("29", "KALP DAMAR CERRAHİ (CARDIAC SURGERY)"),
    ("30", "ACİL TIP (EMERGENCY MEDICINE)"),
    ("31", "GÖĞÜS HASTALIKLARI (THORACIC MEDICINE)"),
    ("32", "FİZİKSEL TIP REHABİLİTASYON (PHYSIOTHERAPY)"),
    ("33", "PSİKİYATRİ (PSYCHIATRY)"),
    ("34", "KULAK BURUN BOĞAZ (ENT)"),
    ("35", "GÖZ HASTALIKLARI (EYE)"),
    ("36", "ADLİ TIP (FORENSIC MED)"),
    ("37", "HEMATOLOJİ (HEMATOLOGY)"),
    ("38", "ENDOKRONOLOJİ (ENDOCRINOLOGY)"),
    
)

COPY_OR_NOTE = ( 
    ("copy", "Çıkmış"),
    ("note", "Ders Notu")
)

LESSON_YEAR = (
    ("1", "1. sınıf dersi"),
    ("2", "2. sınıf dersi"),
    ("3", "3. sınıf dersi"),
    ("staj", "Staj"),
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
    class_year = models.CharField(max_length = 20,choices = LESSON_YEAR, default = 'none')
    #1 2 3 ARTI STAJ SEÇİLSİN CHOİCE FİELD
    lesson_year = models.SmallIntegerField()
    academician = models.ForeignKey(Academician, on_delete= models.PROTECT)
    description = models.TextField()
    
    def __str__(self):
        return self.name
        
        

