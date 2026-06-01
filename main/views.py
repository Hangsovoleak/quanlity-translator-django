from django.shortcuts import render
from translate import Translator

def home(request):
    context = {}
    if request.method == "POST":
        text = request.POST.get("translate", "")
        language = request.POST.get("language", "fr")
        
        if language == "en":
            # If translating English to English, just return the text as-is
            translation = text 
        else:
            # Explicitly set from_lang='en' alongside your target language
            translator = Translator(from_lang="en", to_lang=language)
            translation = translator.translate(text)
        
        context = {
            "original_text": text,
            "translated_text": translation,
            "selected_language": language,
        }
        
    return render(request, 'main/index.html', context)