#Copyright (c) 2021 NEEL18

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

#LICENSE   = NEEL GitHub
#__author__= NEEL KANANI
#__email___= neelkanani9999@gmail.com
#__Year____= 2021
#Version___= 1.1.0

import datetime
import requests
import wikipedia
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import googletrans
from googletrans import Translator
#import simplejson as json
#from Crypto import return_cryptoPrices
#from newsapi import NewsApiClient
#import PyCurrency_Converter 
#from forex_python.converter import CurrencyRates
#from currency_converter import CurrencyConverter

app = Flask(__name__)



@app.route("/")
def hello():
    return "Status Online"

@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '')
    #print(incoming_msg)
    resp = MessagingResponse()
    msg = resp.message()
    responded = False

    if 'about' in incoming_msg or 'About' in incoming_msg:
        text = f'🎯Created and Developed by *NEEL KANANI*📌\n*✉️© 2021 NEEL KANANI.  All rights reserved.*📝 '
        msg.body(text)
        responded = True

    
    if 'start' in incoming_msg or 'Start' in incoming_msg:
        text = f'🤖 _Hello I Am a Bit BOT, how Can I Help You?_\n\n*Company\'s official number and website :*\n\n📞 : +917041622101\n📱 : \n\n*For any query Contact on below no :*\n\n📞 : +917041622101 (NEEL KANANI )\n\n*For feedback, mail us on below mail id :*\n📧 neel.kanani111145@marwadiuniversity.ac.in (NEEL KANANI)\n--------------------------------------------------------------------\n\n🚀 *Features*\n\n✅ _Covid-19 info_\n✅ \n✅ \n✅ _Google Search_ \n✅ \n✅ _wiki Search_\n✅ _weather Information_\n✅ _Quote_\n✅ _Translator_\n\n--------------------------------------------------------------------\n\n🎯 *Upcoming features* 🎯\n\n✅ _Stackoverflow query finder_\n✅ _Voice based query_\n✅ _Torrent link to Google drive link or normal link_\n✅ _Device based location in longitude and latitude_\n✅ _Instagram video Downloader_\n✅ _stocking instagram profile_\n✅ _News_\n\n--------------------------------------------------------------------\n\n_To Display Command Type_ *Menu*\n\n_To help for Command Type_ *Help or help*' 
        msg.body(text)
        responded = True

    if 'info-covid' in incoming_msg or 'Info-covid' in incoming_msg:
        import requests as r, json
        req = r.get('https://coronavirus-19-api.herokuapp.com/countries/india')
        res = r.get('https://coronavirus-19-api.herokuapp.com/countries/Russia')
        reu = r.get('https://coronavirus-19-api.herokuapp.com/countries/USA')
        reqq = r.get('https://coronavirus-19-api.herokuapp.com/countries/world')
        jss = reqq.json()
        js= req.json()
        jsr = res.json()
        jsu = reu.json()
        text = f'*Info Coronavirus India 🇮🇳*\n\n*Positive* : {js["cases"]} \n*Recovred* : {js["recovered"]} \n*Died* : {js["deaths"]} \n*Today cases* : {js["todayCases"]} \n*Today died* : {js["todayDeaths"]} \n*critical* : {js["critical"]} \n*casesPerOneMillion* : {js["casesPerOneMillion"]} \n*deathsPerOneMillion* : {js["deathsPerOneMillion"]} \n*totalTests* : {js["totalTests"]} \n*TestsPerMillion*: {js["testsPerOneMillion"]}\n\n\n*Info Coronavirus USA 🇺🇸*\n\n*Positive* : {jsu["cases"]} \n*Recovred* : {jsu["recovered"]} \n*Died* : {jsu["deaths"]} \n*Today cases* : {jsu["todayCases"]} \n*Today died* : {jsu["todayDeaths"]} \n*critical* : {jsu["critical"]} \n*casesPerOneMillion* : {jsu["casesPerOneMillion"]} \n*deathsPerOneMillion* : {jsu["deathsPerOneMillion"]} \n*totalTests* : {jsu["totalTests"]} \n*TestsPerMillion*: {jsu["testsPerOneMillion"]} \n\n\n*Info Coronavirus Russia 🇷🇺*\n\n*Positive* : {jsr["cases"]} \n*Recovred* : {jsr["recovered"]} \n*Died* : {jsr["deaths"]} \n*Today cases* : {jsr["todayCases"]} \n*Today died* : {jsr["todayDeaths"]} \n*critical* : {jsr["critical"]} \n*casesPerOneMillion* : {jsr["casesPerOneMillion"]} \n*deathsPerOneMillion* : {jsr["deathsPerOneMillion"]} \n*totalTests* : {jsr["totalTests"]} \n*TestsPerMillion*: {jsr["testsPerOneMillion"]} \n\n\n*Global* \n\n*Positive* : {jss["cases"]} \n*Recovered* : {jss["recovered"]} \n*Died* : {jss["deaths"]}'
        msg.body(text)
        responded = True
       

    if "/CR-IN-US" in incoming_msg:
        import requests
        par = incoming_msg[9:]
        c = CurrencyConverter(decimal=True)
        result = c.convert(par, 'INR' , 'USD')
        msg.body(result)
        responded = True

    if 'Menu' in incoming_msg or 'menu' in incoming_msg:
        text = f'⌨️ *List Of Command :*  \n\n🔥 *info-covid* (Information of COVID-19) \n\n🔥 *Schedule* _Display Schedule_\n\n🔥 *YT* _<url>_ : Youtube Downloader\n\n🔥 *Quote* : Generate Quote\n\n🔥 *wiki* : Information form wikipedia\n\n🔥 *FL* _<url>_ : Download Big Size Fb Videos\n\n🔥 *GL* _<query>_ : Google Search\n\n🔥 *weather _<city name>_* : weather Information \n\n🔥 *Advice :* Sends life related advice\n\n🔥 *Translator :* Translates one language to other language \n\n🔥 *help* : How to use the command'
        msg.body(text)
        responded = True
    
    if 'GL' in incoming_msg or 'gl' in incoming_msg or 'Gl' in incoming_msg:
        from googlesearch import search
        query = incoming_msg[2:]
        for i in search(query, tld="com", num=10, stop=10, pause=2):
            text = f'\n\n============Results============\n\n *Result* : '+i
            msg.body(text)
            responded = True

    if 'quote' in incoming_msg or 'Quote' in incoming_msg:
        # return a quote
        import requests
        r = requests.get('https://api.quotable.io/random')
        if r.status_code == 200:
            data = r.json()
            quote = f'{data["content"]} ({data["author"]})'
        else:
            quote = 'I could not retrieve a quote at this time, sorry.'
        msg.body(quote)
        responded = True

    if 'weather' in incoming_msg or 'Weather' in incoming_msg:
        import requests
        def return_weather(place):
            words = place.split(" ")
            r = data = requests.get(
                'http://api.openweathermap.org/data/2.5/weather?q=' + words[1] + '&APPID=0216d3975efcbccb926efbaf5d521b86')
            weatherDetails = r.json()
            temp = weatherDetails["main"]["temp"]
            weatherDescription = weatherDetails["weather"][0]["description"]
            msg = "It is {temp} degrees with {desc}".format(temp=temp,desc=weatherDescription)
            return msg
        data = return_weather(incoming_msg)
        msg.body(data)
        responded = True

    if 'advice' in incoming_msg or 'Advice' in incoming_msg:
        import requests
        def return_advice():
            r = requests.get('https://api.adviceslip.com/advice')
            if r.status_code == 200:
                data = r.json();
                advice = data["slip"]["advice"]
            return advice
        data = return_advice()
        msg.body(data)
        responded = True

    if 'TR en-gu' in incoming_msg:
        par = incoming_msg[8:]
        translator = Translator()
        result = translator.translate(par, src='en', dest='gu')
        msg.body(result.text)
        responded = True

    if 'TR gu-en' in incoming_msg:
        par = incoming_msg[8:]
        translator = Translator()
        result = translator.translate(par, src='gu', dest='en')
        msg.body(result.text)
        responded = True

    if 'TR en-mr' in incoming_msg:
        par = incoming_msg[8:]
        translator = Translator()
        result = translator.translate(par, src='en', dest='mr')
        msg.body(result.text)
        responded = True

    if 'TR mr-en' in incoming_msg:
        par = incoming_msg[8:]
        translator = Translator()
        result = translator.translate(par, src='mr', dest='en')
        msg.body(result.text)
        responded = True

    if 'TR en-hi' in incoming_msg:
        par = incoming_msg[8:]
        translator = Translator()
        result = translator.translate(par, src='en', dest='hi')
        msg.body(result.text)
        responded = True

    if 'TR hi-en' in incoming_msg:
        par = incoming_msg[8:]
        translator = Translator()
        result = translator.translate(par, src='hi', dest='en')
        msg.body(result.text)
        responded = True

    if 'TR en-kn' in incoming_msg:
        par = incoming_msg[8:]
        translator = Translator()
        result = translator.translate(par, src='en', dest='kn')
        msg.body(result.text)
        responded = True

    if 'TR kn-en' in incoming_msg:
        par = incoming_msg[8:]
        translator = Translator()
        result = translator.translate(par, src='kn', dest='en')
        msg.body(result.text)
        responded = True

    if 'TR en-bn' in incoming_msg:
        par = incoming_msg[8:]
        translator = Translator()
        result = translator.translate(par, src='en', dest='bn')
        msg.body(result.text)
        responded = True

    if 'TR bn-en' in incoming_msg:
        par = incoming_msg[8:]
        translator = Translator()
        result = translator.translate(par, src='bn', dest='en')
        msg.body(result.text)
        responded = True

    if 'TR en-ta' in incoming_msg:
        par = incoming_msg[8:]
        translator = Translator()
        result = translator.translate(par, src='en', dest='ta')
        msg.body(result.text)
        responded = True

    if 'TR ta-en' in incoming_msg:
        par = incoming_msg[8:]
        translator = Translator()
        result = translator.translate(par, src='ta', dest='en')
        msg.body(result.text)
        responded = True

    if 'TR en-te' in incoming_msg:
        par = incoming_msg[8:]
        translator = Translator()
        result = translator.translate(par, src='en', dest='te')
        msg.body(result.text)
        responded = True

    if 'TR te-en' in incoming_msg:
        par = incoming_msg[8:]
        translator = Translator()
        result = translator.translate(par, src='te', dest='en')
        msg.body(result.text)
        responded = True

    if 'TR en-ml' in incoming_msg:
        par = incoming_msg[8:]
        translator = Translator()
        result = translator.translate(par, src='en', dest='ml')
        msg.body(result.text)
        responded = True

    if 'TR ml-en' in incoming_msg:
        par = incoming_msg[8:]
        translator = Translator()
        result = translator.translate(par, src='ml', dest='en')
        msg.body(result.text)
        responded = True

    if 'TR en-pa' in incoming_msg:
        par = incoming_msg[8:]
        translator = Translator()
        result = translator.translate(par, src='en', dest='pa')
        msg.body(result.text)
        responded = True

    if 'TR pa-en' in incoming_msg:
        par = incoming_msg[8:]
        translator = Translator()
        result = translator.translate(par, src='pa', dest='en')
        msg.body(result.text)
        responded = True

    if 'TR en-ur' in incoming_msg:
        par = incoming_msg[8:]
        translator = Translator()
        result = translator.translate(par, src='en', dest='ur')
        msg.body(result.text)
        responded = True

    if 'TR ur-en' in incoming_msg:
        par = incoming_msg[8:]
        translator = Translator()
        result = translator.translate(par, src='ur', dest='en')
        msg.body(result.text)
        responded = True

    if 'TR ur-gu' in incoming_msg:
        par = incoming_msg[8:]
        translator = Translator()
        result = translator.translate(par, src='ur', dest='gu')
        msg.body(result.text)
        responded = True

    if 'TR gu-ur' in incoming_msg:
        par = incoming_msg[8:]
        translator = Translator()
        result = translator.translate(par, src='gu', dest='ur')
        msg.body(result.text)
        responded = True

    if 'TR ur-hi' in incoming_msg:
        par = incoming_msg[8:]
        translator = Translator()
        result = translator.translate(par, src='ur', dest='hi')
        msg.body(result.text)
        responded = True

    if 'TR hi-ur' in incoming_msg:
        par = incoming_msg[8:]
        translator = Translator()
        result = translator.translate(par, src='hi', dest='ur')
        msg.body(result.text)
        responded = True

    if 'TR ur-mr' in incoming_msg:
        par = incoming_msg[8:]
        translator = Translator()
        result = translator.translate(par, src='ur', dest='mr')
        msg.body(result.text)
        responded = True

    if 'TR mr-ur' in incoming_msg:
        par = incoming_msg[8:]
        translator = Translator()
        result = translator.translate(par, src='mr', dest='ur')
        msg.body(result.text)
        responded = True

    if 'TR ur-kn' in incoming_msg:
        par = incoming_msg[8:]
        translator = Translator()
        result = translator.translate(par, src='ur', dest='kn')
        msg.body(result.text)
        responded = True

    if 'TR kn-ur' in incoming_msg:
        par = incoming_msg[8:]
        translator = Translator()
        result = translator.translate(par, src='kn', dest='ur')
        msg.body(result.text)
        responded = True

    if 'TR ur-bn' in incoming_msg:
        par = incoming_msg[8:]
        translator = Translator()
        result = translator.translate(par, src='ur', dest='bn')
        msg.body(result.text)
        responded = True

    if 'TR bn-ur' in incoming_msg:
        par = incoming_msg[8:]
        translator = Translator()
        result = translator.translate(par, src='bn', dest='ur')
        msg.body(result.text)
        responded = True

    if 'TR ur-ta' in incoming_msg:
        par = incoming_msg[8:]
        translator = Translator()
        result = translator.translate(par, src='ur', dest='ta')
        msg.body(result.text)
        responded = True

    if 'TR ta-ur' in incoming_msg:
        par = incoming_msg[8:]
        translator = Translator()
        result = translator.translate(par, src='ta', dest='ur')
        msg.body(result.text)
        responded = True

    if 'TR ur-te' in incoming_msg:
        par = incoming_msg[8:]
        translator = Translator()
        result = translator.translate(par, src='ur', dest='te')
        msg.body(result.text)
        responded = True

    if 'TR te-ur' in incoming_msg:
        par = incoming_msg[8:]
        translator = Translator()
        result = translator.translate(par, src='te', dest='ur')
        msg.body(result.text)
        responded = True

    if 'TR ur-ml' in incoming_msg:
        par = incoming_msg[8:]
        translator = Translator()
        result = translator.translate(par, src='ur', dest='ml')
        msg.body(result.text)
        responded = True

    if 'TR ml-ur' in incoming_msg:
        par = incoming_msg[8:]
        translator = Translator()
        result = translator.translate(par, src='ml', dest='ur')
        msg.body(result.text)
        responded = True

    if 'TR ur-pa' in incoming_msg:
        par = incoming_msg[8:]
        translator = Translator()
        result = translator.translate(par, src='ur', dest='pa')
        msg.body(result.text)
        responded = True

    if 'TR pa-ur' in incoming_msg:
        par = incoming_msg[8:]
        translator = Translator()
        result = translator.translate(par, src='pa', dest='ur')
        msg.body(result.text)
        responded = True

    if 'wiki' in incoming_msg:
        query = incoming_msg[4:]
        incoming_msg = incoming_msg.replace("wiki", "")
        result = wikipedia.summary(incoming_msg, sentences=3)
        text = f'\n\n This is according to wikipedia\n\n=============*Result*==============\n\n '+result
        msg.body(text)
        responded = True

    if 'Time' in incoming_msg or 'time' in incoming_msg:
        strTime=datetime.datetime.now().strftime("%H:%M:%S")
        text = f'\n\n Current time \n '+ strTime
        msg.body(text)
        responded = True

    if 'FB' in incoming_msg or 'fb' in incoming_msg or 'Fb' in incoming_msg:
        import requests as r
        import re
        par = incoming_msg[2:]
        html = r.get(par)
        video_url = re.search('sd_src:"(.+?)"', html.text).group(1)
        reqq = r.get('http://tinyurl.com/api-create.php?url='+video_url)
        msg.body('*Video Converted Successfully here is your link...*\n\nLINK : '+reqq.text)
        responded = True

        
   # if '/TTS' in incoming_msg:
      #  par = incoming_msg[5:]
       # msg.media('https://api.farzain.com/tts.php?id='+par+'&apikey=JsaChFteVJakyjBa0M5syf64z&')
       # responded = True

    if 'YT' in incoming_msg or 'yt' in incoming_msg or 'Yt' in incoming_msg:
        import pafy
        import requests as r
        par = incoming_msg[2:]
        audio = pafy.new(par)
        gen = audio.getbestaudio(preftype='m4a')
        genn = audio.getbestvideo(preftype='mp4')
        req = r.get('http://tinyurl.com/api-create.php?url='+gen.url)
        popo = r.get('http://tinyurl.com/api-create.php?url='+genn.url)
        msg.body('_=========================_\n\n     _Video Converted Successfully_\n\n_=========================_\n\n''*'+gen.title+'*''\n\n*Link Download Music* :' +req.text+'\n\n*Link Download Video* :' +popo.text)
        responded = True
        
    if 'Schedule' in incoming_msg or 'schedule' in incoming_msg:
       msg.media('https://user-images.githubusercontent.com/74760068/111062692-72dbbf00-84d0-11eb-9f46-2b88854c78a0.png')
       responded = True

    if 'help' in incoming_msg or 'Help' in incoming_msg:
       text = f'💻 *Help For Facebook*\n\nFB _link video_ Ecample :\n\nFB https://fb.watch/2uY9On1xkw/ \n\n💻 *Help For Google Search* \n\n GL <Query> Example :  \n\nGL GUJARAT \n\n💻 *Help for YouTube video Download*\n\n YT <video link> Example :  \n\nYT https://youtu.be/Ci0WbaUH3no\n\n💻 *Help for translator*\n\n TR-en-gu <sentence> Example :  \n\nTR-en-gu How are you? \n\nfor translator we have only indian languages included so far the list is below:\n\n-------------------------------------------------------------------- \n\nTR-gu-en <Translate Gujarati to English>\nTR-en-mr <Translate English to Marathi>\nTR-mr-en <Translate Marathi to English>\nTR-en-hi <Translate English to Hindi>\nTR-hi-en <Translate Hindi to English>\nTR-en-kn <Translate English to Kannad>\nTR-kn-en <Translate Kannad to English>\nTR-en-bn <Translate English to Bengali>\nTR-bn-en <Translate Bengali to English>\nTR-en-ta <Translate English to Tamil>\nTR-ta-en <Translate Tamil to English>\nTR-en-te <Translate English to Telugu>\nTR-te-en <Translate Telugu to English>\nTR-te-en <Translate Telugu to English>\nTR-en-ml <Translate English to Malayalam>\nTR-ml-en <Translate Malayalam to English>\nTR-en-pa <Translate English to Punjabi>\nTR-pa-en <Translate Punjabi to English>\nTR-pa-en <Translate Punjabi to English>\nTR-ur-en <Translate Urdu to English>'
       msg.body(text)
       responded = True
    
    if responded == False:
        msg.body('Sorry for inconvinience, I Am just BOT didn\'t recognized that command, please send start to go to the menu')

    return str(resp)

if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
