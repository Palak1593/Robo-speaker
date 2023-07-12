
import pyttsx3

# To achieve real-time speech output as you type, you can use the pyttsx3 library instead of gtts. 
# The pyttsx3 library provides a text-to-speech functionality with the ability to speak the text immediately
# without the need to save it to a file.

if __name__=='__main__':

  print("Welcome to robo speaker")
  engine=pyttsx3.init()           #This line initializes the text-to-speech engine using pyttsx3.init(). 
                                #   It creates an instance of the engine that will be used to convert text to speech.
  while True:
      x=input("Enter what you want to pronounce : ")
      
      if x=='q':
        break
    
      engine.say(x)        #This line uses the engine object to convert the text x to speech.
                           #   The engine.say() function is called with the text as the parameter.
      
      engine.runAndWait()   #This line instructs the engine to run the speech synthesis and
                            # wait for it to complete before continuing to the next iteration of the loop. 
                            # It ensures that the speech is spoken before moving on to the next input.