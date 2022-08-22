import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import os
import smtplib
import wikipedia
master="Samya"
print("Getting Cathy Ready")
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

# this function will pronouced the string passed to it
def speak(text):
	engine.say(text)
	engine.runAndWait()
# wishing the master
def wishMe():
	hour= int(datetime.datetime.now().hour)
	
	if hour >=0 and hour<12:
		speak("Good Morning "+ master)
	elif hour >=12 and hour<18:
		speak("Good Afternoon "+ master)
	else :
		speak("Good Evening "+master)
	speak("How can I help?")
# takes command from the master
def takeCommand():
	r= sr.Recognizer()
	with sr.Microphone() as source :
		print('...')
		audio= r.listen(source)
	
	try:
		print("Recognizing....")
		query=r.recognize_google(audio, language='en-in')
		print(query)
		
	except Exception as e:
		speak("Say that again please")
		
	return query

		
	


speak("Hi, I'm Cathy'")
wishMe()

query= takeCommand()

if 'wikipedia' in query.lower() : 
	speak('searching Wikipedia')
	query=query.replace("wikipedia", "")
	results= wikipedia.summary(query, sentences=2)
	speak(results)
elif 'open youtube' in query.lower():
	webbrowser.open ('youtube.com')
elif 'play videos of' in query.lower() or 'search youtube for' in query.lower():
	
	
	args=query.split()
	str=args[3]
	for i in range(4,len(args)):
		str= str+"+"+args[i]
	webbrowser.open('www.youtube.com/results?search_query='+str)
elif 'who is' in query.lower() :
	speak('searching Wikipedia')
	if 'who is' in query.lower():
		query=query.replace("who is", "")
		results=wikipedia.summary(query, sentences=2, auto_suggest=False)
		speak(results)
elif 'what is' in query.lower() :
		query=query.replace("what is", "")

		results=wikipedia.summary(query, sentences=2, auto_suggest=False)
		speak(results)
elif 'the time' in query.lower():
	hour= int(datetime.datetime.now().hour)
	minute= int(datetime.datetime.now().minute)
	if hour >=12 :
		hour=hour-12
		if hour==0:
			hour=12
		strTime="The time is "+str(hour)+":"+str(minute)+"pm"
		speak(strTime)
	else :
		strTime="The time is "+str(hour)+":"+str(minute)+"am"
		speak(strTime)
else:
	speak("Sorry, I don't know that")
	




