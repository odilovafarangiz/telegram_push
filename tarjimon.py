from deep_translator import GoogleTranslator
def tarjima_uz(matn):
    t=GoogleTranslator(source='auto',\
      target='uz').translate(text=matn)
    return  t
def tarjima_en(matn):
    t=GoogleTranslator(source='auto',\
      target='en').translate(text=matn)
    return  t