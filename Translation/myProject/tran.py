from google_trans_new import google_translator
translator=google_translator()

value=translator.translate('hello',lang_src='en',lang_tgt='it')
print(value)




