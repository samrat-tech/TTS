import pyttsx3
import abbreviations

class main_engine(object):

    def text_to_speech(self):
        
        """
        Function to convert text to speech
        :param text: text
        :param gender: gender
        :return: None
        """
              
        voice_dict = {'Male': 0, 'Female': 1}
        code = voice_dict[self.gender]

        engine = pyttsx3.init()
        
        
        cleaner_engine=abbreviations.abbreviation(self.text)
        cleaned_text= cleaner_engine.english_cleaners()
        
        

        # Setting up voice rate
        engine.setProperty('rate', 120)

        # Setting up volume level  between 0 and 1
        engine.setProperty('volume', 0.8)

        # Change voices: 0 for male and 1 for female
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[code].id)

        engine.say(cleaned_text)
        engine.runAndWait()
    
    def __init__(self,text,gender):
        self.text=text
        self.gender=gender
        
# p1=main_engine('text LOL text','Male')
# p1.text_to_speech()


