class file_extension_validator(object):

    def __init__(self,filename):
        self.filename=filename
        self.allowed_extensions={'txt', 'pdf', 'docx'}
     
    

    def allowed_file(self):
        return '.' in self.filename and \
            self.filename.rsplit('.', 1)[1].lower() in self.allowed_extensions


# p1=file_extension_validator('a.txt')
# print(p1.allowed_file())
# return True/false