import speech_recognition as sr

r = sr.Recognizer()
with sr.AudioFile('./Rei Do gado.wav') as fonte:
    audio = r.record(fonte)
try:
    texto = r.recognize_google(audio, language='pt-br')
    print(f'Google Speech Recognition acha que você disse: \n"{texto}"')
except sr.UnknownValueError:
    print('Google Speech Recognition não entendeu seu áudio')
except sr.RequestError as e:
    print(f'Não foi possível se conectar à API da Google. Erro: {str(e)}')
