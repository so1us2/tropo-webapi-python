import sys
sys.path = ['..'] + sys.path
from itty import *
from tropo import Tropo, Session, Result, Transcription

@post('/index')
def index(request):

    t = Tropo()
    VOICE = 'Grace' 
    
    transcriptionobj = Transcription(id = "tropo-12123", url = "http://192.168.26.88:8080/FileUpload/uploadFile", language = "English").json

    t.record(transcription = transcriptionobj, name='voicemail.wav', say='Your call is important. Please leave a short message after the tone: ', url = 'http://192.168.26.88:8080/FileUpload/uploadFile', beep = True, formamt = 'audio/wav', sensitivity = 5.3) 

    return t.RenderJson()
	
run_itty(server='wsgiref', host='192.168.26.1', port=8888)
