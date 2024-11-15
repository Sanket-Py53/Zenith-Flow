from django import forms

class FileUploadForm(forms.Form):
    FILE_TYPE_CHOICES = [
        ('CSV', 'CSV'),  #actual value stored in the database
        ('Excel','Excel'),   #display text shown in the form
    ]
    clientname = forms.CharField(max_length=30, label="Client Name")
    filetype = forms.ChoiceField(choices= FILE_TYPE_CHOICES, label='File Type')
    uploaddate = forms.DateField(widget=forms.SelectDateWidget,label='Enter Date')
    file = forms.FileField(label='Upload File')