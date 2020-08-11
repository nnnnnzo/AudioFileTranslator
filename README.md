# AudioFileTranslator
AFT is a python nano framework based on the googletrans and speech_recognition modules. AFT transcribe and translate an audio file to another language. The code is easy to understand and edit, the demo version translate a French dialogue to an English Text (AFT_One.py).

*AFT work by installing the two required python modules:
</br>`$ pip install googletrans`
</br>`$ pip install SpeechRecognition`

## Table of Contents

- [AFT Engine (Python Module)](#AFT-Engine)
- [AFT One (PreConfigured AudioTranslator)](#AFT-One)
- [License](#license)


## AFT Engine
"AFT_Engine.py" is the python module from AFT. It's made to be used inside another script without taking space.</br> </br>
[![AFTE BADGE](https://img.shields.io/badge/Download-AFT%20Engine-blue)](https://github.com/nnnzo/AudioFileTranslator/releases/tag/1.1)
### Installation
To use AFT Engine, it's required to move "AFT_Engine.py" in the same directory of your own python script.
### Importation and usage
To import and use AFT Engine use the following code.</br>
```python
from AFT_Engine import *
print(AFTcore("audio.wav", "fr-FR", "fr", "ja"))
```
or (if you don't want to print the translated audio)</br>
```python
from AFT_Engine import *
AFTcore("audio.wav", "fr-FR", "fr", "ja"))
```
##### /!\ AFT Engine only return the translated text, nothing more.
#### As you noticed the AFTcore function of the Engine need 4 arguments: </br> 
```python
("AudioFilePath", "SourceLanguageCode-SourceCountryCode", "SourceLanguageCode", "DestinationLanguageCode")
```
</br>[Language Code List >>](https://cloud.google.com/translate/docs/languages "Language Code List")</br>
#### The Repo contains a demo folder to help you use AFT Engine.

</br>

## AFT One 
"AFT_One.py" is a more user friendly version for people who only want a Translator and not a python module. </br> </br>
[![AFTO BADGE](https://img.shields.io/badge/Download-AFT%20One-yellow)](https://github.com/nnnzo/AudioFileTranslator/releases/tag/1.0)
</br>
![AFT Base ScreenShot](https://raw.githubusercontent.com/nnnzo/Ressources/master/img/Capture%20d%E2%80%99e%CC%81cran%202020-08-02%20a%CC%80%2012.28.09.png)

PS: The audio used in the screenshot is not really appropriate, it is made to learn the pronunciation of French words; hence the errors towards the end of the translation.

## License

The AFT framework (wich contains AFT Engine and AFT One) is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Tips

This Github account is verified by the brave creator program, please consider making a BAT tips !
![BAT logo](https://gemini.com/images/currencies/buy_basicattentiontoken_bat.svg) 
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
