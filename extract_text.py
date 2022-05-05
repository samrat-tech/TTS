import PyPDF2
import docx

class upload(object):

    def upload_txt(self):
        file = open(self.path)
        text = file.read().replace("\n", " ")
        return text
        file.close()
        

    def upload_pdf(self):
        # creating a pdf file object
        file = open(self.path, 'rb')

        # creating a pdf reader object
        pdfReader = PyPDF2.PdfFileReader(file)

        # creating a page object
        pageObj = pdfReader.getPage(0)

        # extracting text from page
        text = pageObj.extractText()
        # text_to_speech(text, gender)
        return text
        file.close()


    def upload_docx(self):
        doc = docx.Document(self.path)
        all_paras = doc.paragraphs
        for para in all_paras:
            # text_to_speech(para.text, gender)
            return para.text
    
    def __init__(self,path):
        self.path=path
        
        


# path="G:/class/n.txt"
# p1=upload(path,"male")
# p1.upload_txt()