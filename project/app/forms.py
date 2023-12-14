from django import forms
from django.core import validators
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordChangeForm
from django.contrib.auth.models import User
from app.models import Academician, Lesson
from django_select2.forms import ModelChoiceIterator,ModelSelect2Widget

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


"""def checkUni(value):
    at_index = value.find("@")
    if at_index != -1 and at_index < len(value) - 18 and value[at_index:].find("stu.istinye.edu.tr") != -1 :
        print("okay")
    else:
        raise forms.ValidationError("Üniversite mailiniz uygun değildir")"""
        

class RegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Customize labels
        self.fields['username'].label = 'Kullanıcı adı'
        self.fields['password1'].label = 'Şifre'
        self.fields['password2'].label = 'Şifre tekrar'

        # Customize help text
        self.fields['username'].help_text = ""
        self.fields['password1'].help_text = """
            <ul>
                <li>Şifreniz diğer kişisel bilgilerinizle çok benzer olamaz.</li>
                <li>Şifreniz en az 8 karakter içermelidir.</li>
                <li>Parolanız yaygın olarak kullanılan bir parola olamaz.</li>
                <li>Parolanız tamamen sayısal olamaz.</li>
            </ul>
        """
        self.fields['password2'].help_text = ""
        self.fields['email'].help_text = "Sadece üniversite mailinizle kayıt olabilirsiniz. Üniversiteniz sistemde kayıtlı değilse siteye kayıt olamazsınız. Üniversite eklemesi yapmak için bize ulaşın."

    #email = forms.EmailField(required=True,validators=[checkUni])
    class Meta:
        model = User
        fields = ["username", "email", "password1","password2"]


class CustomLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Customize labels
        self.fields['username'].label = 'Kullanıcı Adı'
        self.fields['password'].label = 'Şifre'

class CustomPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Customize labels
        self.fields['old_password'].label = 'Eski Şifre'
        self.fields['new_password1'].label = 'Yeni Şifre'      
        self.fields['new_password2'].label = 'Yeni Şifre Tekrar'
        

        #Customize help text
        self.fields['new_password1'].help_text = """
            <ul>
                <li>Şifreniz diğer kişisel bilgilerinizle çok benzer olamaz.</li>
                <li>Şifreniz en az 8 karakter içermelidir.</li>
                <li>Parolanız yaygın olarak kullanılan bir parola olamaz.</li>
                <li>Parolanız tamamen sayısal olamaz.</li>
            </ul>
        """

class AcademicianForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Customize labels
        self.fields['name'].label = 'Hoca Adı'
        self.fields['copy'].label = 'Çıkmış sorar mı?'      
        self.fields['attendance'].label = 'Yoklama alır mı?'
        self.fields['note'].label = 'Sözlü notu bol mu?'
        self.fields['lecture'].label = 'Ders anlatımı'
        self.fields['description'].label = 'Açıklama'      


    class Meta:
        model = Academician
        fields = ["name", "copy", "attendance", "note", "lecture", "description"]

class SearchAcademicianForm(forms.Form):
    search_query = forms.ModelChoiceField(
        queryset=Academician.objects.all(),
        required=False,
        empty_label=None
    )


class LessonForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Customize labels
        self.fields['title'].label = 'Ders Notu Başlığı'
        self.fields['name'].label = 'Ders'
        self.fields['copy_or_note'].label = 'Çıkmış mı? Ders Notu mu?'    
        # self.fields['link'].label = 'Ders Notu Linki'    
        self.fields['class_year'].label = 'Kaçıncı Sınıf Dersi?'
        self.fields['lesson_year'].label = 'Ders Yılı'
        self.fields['academician'].label = 'Dersin Hocası'
        self.fields['description'].label = 'Ders Notu Açıklaması'  
        
    class Meta:
        model = Lesson
        fields = ["title", "name","copy_or_note", "class_year","lesson_year", "academician",  "description"]



class SearchLessonForm(forms.Form):
    search_query_lesson = forms.ChoiceField(
        choices=LESSON_CHOICES, 
        required=False,      
    )
    search_query_copy_or_note = forms.ChoiceField(
        choices=COPY_OR_NOTE,  
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['search_query_lesson'].choices = [('any', 'Any')] + self.get_lesson_choices()
        

    def get_lesson_choices(self):
        lesson_names = Lesson.objects.values_list('name', flat=True).distinct()
        return [(choice[0], choice[1]) for choice in LESSON_CHOICES if choice[0] in lesson_names]
    
class tempform:
    pass