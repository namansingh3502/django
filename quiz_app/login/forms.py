from django import forms

class UserPass( forms.Form ):
	CHOICES = (('creator', 'Creator'),('participant', 'Participant'))
	
	username = forms.CharField( label='Username')
	password = forms.CharField( widget=forms.PasswordInput, label='Password')
	user_type = forms.ChoiceField( label = 'I am' , choices = CHOICES )

class NewUser( forms.Form ):
	CHOICES = (('creator', 'Creator'),('participant', 'Participant'))
    
	name = forms.CharField( label = 'Name')
	username = forms.CharField( label = 'Username')
	password = forms.CharField( widget = forms.PasswordInput, label = 'Password')
	user_type = forms.ChoiceField( label = 'I am' , choices = CHOICES )
