from django import forms

class TweetForm(forms.Form):
	name = forms.CharField(max_length=32,required=False)
	tweet = forms.CharField(max_length=32,label='Tweet')
