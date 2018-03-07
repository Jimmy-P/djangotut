from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Comment, Post


#class MyRegistrationForm(UserCreationForm):
#    email = forms.EmailField(required=True)
#    
#    class Meta:
#        model = User
#        fields = ('username', 'email', 'password1', 'password2')
#        
#    def save(self, commit=True):
#        user = super(MyRegistrationForm, self).save(commit=False)
#        user.email = self.cleaned_data['email']
#        # user.set_password(self.cleaned_data['password1'])
#        
#        if commit:
#            user.save()
#            
#        return user
#    
#    
#
#class ContactForm1(forms.Form):
#    subject = forms.CharField(max_length=100)
#    
#class ContactForm2(forms.Form):
#    sender = forms.EmailField()
#
#class ContactForm3(forms.Form):
#    message = forms.CharField(widget=forms.Textarea)

class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)#('name', 'email', 'body')

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','body',)
