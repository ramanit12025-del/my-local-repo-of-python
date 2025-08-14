import pyttsx3

# Initialize Text-to-Speech engine
engine = pyttsx3.init()

# Optional: Adjust speaking rate
engine.setProperty('rate', 170)  # Words per minute

# Optional: Adjust volume (0.0 to 1.0)
engine.setProperty('volume', 1.0)

# Speak first three lines
engine.say("Hello, how are you?")
engine.say("How can I help you?")
engine.say("Anything you need related to product information?")

# Change to female voice (voices[1]) or check available voices
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Usually female
engine.say("Thanks for coming.")

# Run speech
engine.runAndWait()
