#import sounddevice as sd
#import wavio



import streamlit as st
#from audiorecorder import audiorecorder





def record(duration, fs):
  #  sd.default.samplerate = fs
  #  sd.default.channels = 1
    
    
   # st.title("Audio Recorder")
   # audio1 = audiorecorder("Click to record", "Recording...")
    st.write(audio1)
    if len(audio1) > 0:
    	st.audio(audio1)
    	st.write("آواز دوبارہ ریکارڈ کرنے کے لیے' ریکارڈ کیجیے' کا بٹن دبایں۔")
    	wav_file = open("/home/amad/streamlit/voice recording (AADIL)/temp/sample1.wav", "wb")
    	wav_file.write(audio1.tobytes())





   # myrecording = sd.rec(int(duration * fs))
   # sd.wait(duration)
   # return myrecording
    return audio1
def save_record(path_myrecording, myrecording, fs):

  #  wavio.write(path_myrecording, myrecording, fs, sampwidth=2)
    

    
	
  
    print("myrecording")
    	
    
    
    return None
def read_audio(file):
    with open(file, "rb") as audio_file:
        audio_bytes = audio_file.read()
    return audio_bytes
