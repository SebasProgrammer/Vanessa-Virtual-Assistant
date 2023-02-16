def Answer(r, source):
    print('Listening wpp...')
    audio = r.listen(source)
    try:
        record = r.recognize_google(audio, language="es-PE")
        record = record.lower()
        print(record)
        return r, source, record
    except Exception:
        return r, source, ' '

def AnswerSeconds(r, source, type=1, seconds = 2):
    print('Listening...')
    if type == 1:
        audio = r.listen(source)
    else:
        audio = r.record(source, duration=seconds)
    try:
        record = r.recognize_google(audio, language="es-PE")
        record = record.lower()
        print(record)
        return r,  source, record
    except Exception:
        return r, source, ' '
