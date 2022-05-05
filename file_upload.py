import file_validation
import os
from werkzeug.utils import secure_filename
import extract_text


class upload(object):
    def file_upload(self):
        p1=file_validation.file_extension_validator(self.file.filename)       
        if self.file and p1.allowed_file():
            self.filename=secure_filename(self.file.filename)
            self.file.save(os.path.join('D:/TTS-Final-code/text_upload',self.filename))
            self.path= "D:/TTS-Final-code/text_upload"+"/"+self.filename
            self.extension=self.filename.rsplit('.', 1)[1].lower() 
            text=extract_text.upload(self.path)
            if self.extension == "txt":
                a=text.upload_txt()
                return a
                
            elif self.extension == "pdf":
                a= text.upload_pdf()
                return a
                
            elif self.extension == "docx":
                a=text.upload_docx()
                return a


    def alert(self):
        alert=file_validation.file_extension_validator(self.file.filename)
        alert_true= alert.allowed_file()
        if alert_true == True:
            return False
        else:
            return True
   
    
    def __init__(self,file):
        self.file=file



