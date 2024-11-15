from django.shortcuts import render
from .forms import FileUploadForm
from django.conf import settings
import boto3


# Create your views here.
def File_Upload_View(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Check if a file was uploaded
            if 'file' not in request.FILES or not request.FILES['file']:
                form.add_error('file','A File Must Be Uploaded !!!')
            else:
                file = request.FILES['file']
                # To ensure only one file is uploaded
                if len(request.FILES)>1:
                    form.add_error('file','Only One File Can Be Uplaoded !!!')
                else:
                    #Validate File Type
                    allowed_extensions = ['csv','xlsx','xls']
                    file_extension = file.name.split('.')[-1].lower()
                    if file_extension not in allowed_extensions:
                        form.add_error('file', 'Only CSV or Excel files are allowed !!!')

                    else:
                        s3 = boto3.client('s3', aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                                          aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
                                          region_name=settings.AWS_S3_REGION_NAME)
                        # Upload the file to S3
                        s3.upload_fileobj(file, settings.AWS_STORAGE_BUCKET_NAME, file.name)
                        # File is valid; proceed and return success
                        print("File Submitted Sucessfully !!!")
                        print(form.cleaned_data)
                        return render(request, 'file_upload/client_file.html',{'form':form, 'success':True})

        # If the form is not valid or errors occur
        return render(request,'file_upload/client_file.html', {'form': form})

    else:
        form = FileUploadForm()
        # For GET requests, render the form
        return render(request, 'file_upload/client_file.html', {'form': form})
