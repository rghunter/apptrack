from __future__ import unicode_literals

from django.db import models
from django.forms import ModelForm
from django.conf import settings
import uuid

class Scholarship(models.Model):
    name = models.CharField(max_length=50)
    def __unicode__(self):
       return self.name

class Application(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    scholarship = models.ForeignKey(Scholarship, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dob = models.DateField(verbose_name="Date of Birth")
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=50)
    daytime_phone = models.CharField(max_length=50)
    mobile_phone = models.CharField(max_length=50, blank=True)
    email = models.EmailField()
    school_name = models.CharField(verbose_name="Current school or school last attended", max_length=50, blank=True)
    school_address = models.CharField(verbose_name="Current or last school's full address", max_length=50, blank=True)
    grade = models.CharField(max_length=50, blank=True, verbose_name="Current grade or year if still in school")
    previous_bts = models.TextField(verbose_name="If you have been awarded a BTS scholarship previously, please indicate which scholarship and year.")
    how_heard = models.TextField(verbose_name="How did you hear about the BTS scholarships; e.g., guidance counsellor, scuba instructor, BTS website, etc.?")
    certifications_earned = models.CharField(max_length=50, blank=True)
    certification_agency = models.CharField(max_length=50, blank=True)
    number_of_logged_dives = models.PositiveIntegerField(blank=True, null=True)
    use_of_money = models.TextField(verbose_name="DESCRIBE HOW YOU PLAN TO USE THE SCHOLARSHIP FUNDS AND HOW THIS SCHOLARSHIP WILL HELP YOU TO ACHIEVE YOUR GOALS" )
    extra_curriculars = models.TextField(verbose_name="IDENTIFY YOUR EXTRACURRICULAR ACTIVITIES (E.G., SCHOOL RELATED, COMMUNITY RELATED, CLUBS, OTHER.) Be sure to include marine specific activities that you have been involved in, and indicate leadership roles you may have had. Provide dates and/or number of hours of activities.")
    awards = models.TextField(verbose_name="IDENTIFY ANY AWARDS, HONORS OR ACADEMIC ACHIEVEMENTS. Include dates and appropriate information about these awards, etc.")
    work_experience = models.TextField(verbose_name="IDENTIFY ANY INTERNSHIPS/VOLUNTEER/WORK EXPERIENCES YOU HAVE PARTICIPATED IN. Include specific details about these experiences, e.g., dates of the experience, length of time, the work/responsibilities involved, etc.")
    essay = models.TextField(verbose_name="ESSAY: BE SURE TO TELL US ABOUT YOUR INTEREST IN AND PASSION FOR THE OCEANS, THE MARINE LIFE AND ITS PROTECTION AND YOUR MARINE/MARITIME CAREER GOALS.  (Please limit to 500 words.)")
    dive_medic = models.TextField(verbose_name="IF YOU ARE APPLYING FOR THE DIVER MEDIC TECHNICIAN SCHOLARSHIP, ALSO COMPOSE A SHORT ESSAY ON \"WHY I WANT TO BE A DIVER MEDIC\". (Please limit your essay to 250 words.)", blank=True)

    def __unicode__(self):
        return "{}: {} {}".format(self.scholarship.name, self.first_name, self.last_name)


class ApplicationForm(ModelForm):
    class Meta:
        model = Application
        fields = '__all__'

class RecommendationLetter(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=50)
    daytime_phone = models.CharField(max_length=50)
    mobile_phone = models.CharField(max_length=50, blank=True)
    relationship = models.CharField(max_length=200)
    letter = models.TextField()

class RecommendationLetterForm(ModelForm):
    class Meta:
        model = RecommendationLetter
        exclude = ['application']

