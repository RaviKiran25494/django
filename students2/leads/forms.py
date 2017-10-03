from django import forms

class RegistrationForm(forms.Form):
    name=forms.CharField(min_length=2,max_length=45)
    mobile = forms.CharField(max_length=250)
    email = forms.CharField(max_length=250)
    course = forms.CharField(max_length=2500)
    sourse = forms.CharField(max_length=250)
    lead_status = forms.CharField(max_length=250)
    demo_date = forms.CharField(max_length=150)
    counsler = forms.CharField(max_length=2500)
    remarks = forms.CharField(max_length=2500)

# class MyModelForm(forms.ModelForm):
# 	def _init(self, *args, **kwargs):
# 		super(MyModelForm, self).init_(*args, **kwargs)
# 		self.fields['name'].widget.attrs['class']= 'form-control'
# 		self.fields['phone'].widget.attrs[ 'class']='form-control' 
# 		class Meta: model = MyModel