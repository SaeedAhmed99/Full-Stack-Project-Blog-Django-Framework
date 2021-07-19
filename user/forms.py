from django import forms
from django.contrib.auth.models import User
from user.models import pofile


class CreateUser(forms.Form):
    username = forms.CharField(max_length = 50, label = 'اسم المستخدم', help_text = 'اسم المستخد يجب الا يحتوي على مسافات')
    email = forms.EmailField(label = 'البريد الالكتروني')
    first_name = forms.CharField(label = 'الاسم الاول')
    last_name = forms.CharField(label = 'الاسم الاخير')
    password = forms.CharField(label = 'كلمة المرور', min_length = 8, widget = forms.PasswordInput(),
        help_text = 'يجب الا تقل كلمة المرور عن 8 خانات')
    passwordconfirm = forms.CharField(label = 'تاكيد كلمة المرور', min_length = 8, widget = forms.PasswordInput())


    def clean_password2(self):
        if self.cleaned_data['password'] != self.cleaned_data['passwordconfirm']:
            raise forms.ValidationError('كلمة المرور غير متطابقة')
        return self.cleaned_data['passwordconfirm']

    def clean_username(self):
        if User.objects.filter(username=self.cleaned_data['username']).exists(): 
            raise forms.ValidationError('يوجد مستخدم مسجل بهذا الاسم.')
        return self.cleaned_data['username']

class log_in_form(forms.ModelForm):
    username = forms.CharField(label = 'اسم المستخدم')
    password = forms.CharField(label = 'كلمة المرور', widget = forms.PasswordInput())
    class Meta:
        model = User    
        fields = ('username', 'password')

class user_update(forms.ModelForm):
    first_name = forms.CharField(label = 'الاسم الاول')
    last_name = forms.CharField(label = 'الاسم الاخير')
    email = forms.EmailField(label = 'البريد الالكتروني')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class image_update(forms.ModelForm):
    
    class Meta:
        model = pofile
        fields = ('image',)
