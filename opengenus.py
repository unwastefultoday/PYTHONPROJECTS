#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install moviepy')


# In[2]:


'!pip install wand'


# In[3]:


'''def audio_to_video(audio_file_name, output_name):    
    from moviepy.editor import AudioFileClip, TextClip, CompositeVideoClip
    audio = AudioFileClip(audio_file_name)
    text = TextClip("Your Text", fontsize=30, color='white', bg_color='black').set_duration(audio.duration)
    result = CompositeVideoClip([text.set_pos('center')]).set_audio(audio)
    result.write_videofile(output_name+".mp4", codec='libx264', audio_codec='aac')'''


# In[4]:


def url_to_audio(input_urls_file):
    from gtts import gTTS
    import requests
    from bs4 import BeautifulSoup
    import re
    from sumy.parsers.plaintext import PlaintextParser
    from sumy.nlp.tokenizers import Tokenizer
    from sumy.summarizers.text_rank import TextRankSummarizer
    import os
    with open(input_urls_file) as file_in:
        urls = []
        for line in file_in:
            urls.append(line.strip())
    # Make HTTP request to the URL
    for url in urls:
        if len(urls)==0:
            print("No URLS in input.txt")
            break
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'lxml')
        for elem in soup(['script','a', 'style', 'table', 'iframe', 'aside','pre','ins','li','ul','google-auto-placed ap_container','L-Affiliate-Tagged']):
             elem.extract()
        text = soup.get_text()
        text = ''.join(text).strip()
        topic_name = soup.find('h1',class_='post-full-title')


        parser = PlaintextParser.from_string(text, Tokenizer("english"))
        summarizer = TextRankSummarizer()
        summary = summarizer(parser.document, 10)
        text_summary = ""
        for sentence in summary:
            text_summary += str(sentence)


        intro_text = f'Today we will learn about {topic_name.text} '
        outro_text=f'\nThis was all about {topic_name} . For code files and additional information, please visit www.iq.opengenus.org/'
        text_summary = intro_text+'\n'+text_summary+'\n'+outro_text
        with open(topic_name.get_text()+'.txt', 'a') as f:
            for word in text_summary:
                try:
                    f.write(word)
                except:
                    f.write('error'+"\n")

        name=topic_name.get_text()+" .mp3"
        language = 'en'
        speech = gTTS(text=text_summary, lang=language, slow=False)
        speech.save(name)
        '''audio_data = BytesIO()
        speech.save(audio_data)'''
        os.system("mpg321 hello.mp3")
        print("successfully converted from URL to audio!")
        '''vid = input("Do you wish to connvert the audio file to a video? Enter yes or no: ")
        if vid.lower()=="yes":
            audio_to_video(name,topic_name.get_text())
        else:
            print("Thank You!")'''


# In[5]:


'''input_urls_file="C:\\Users\\Ambarish Deb\\Desktop\\project\\input.txt"
url_to_audio(input_urls_file)'''


# In[6]:


def url_to_text(input_urls_file):
    import requests
    from bs4 import BeautifulSoup
    with open(input_urls_file) as file_in:
        urls = []
        for line in file_in:
            urls.append(line.strip())
    # Make HTTP request to the URL
    for url in urls:
        if len(urls)==0:
            print("No URLS in input.txt")
            break
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'lxml')
        for elem in soup(['script','a', 'style', 'table', 'iframe', 'aside','pre','ins','li','ul','google-auto-placed ap_container','L-Affiliate-Tagged']):
             elem.extract()
        text = soup.get_text()
        text = ''.join(text).strip()
        topic_name = soup.find('h1',class_='post-full-title')
        with open(topic_name.get_text()+" .txt", "w", encoding="utf-8") as text_file:
             text_file.write(text)
    
    print("successfully converted from URL to text file!")


# In[7]:


'''input_urls_file="C:\\Users\\Ambarish Deb\\Desktop\\project\\input.txt"
url_to_text(input_urls_file)'''


# In[8]:


def url_to_text_summary(input_urls_file):
    import requests
    from bs4 import BeautifulSoup
    from sumy.parsers.plaintext import PlaintextParser
    from sumy.nlp.tokenizers import Tokenizer
    from sumy.summarizers.text_rank import TextRankSummarizer
    with open(input_urls_file) as file_in:
        urls = []
        for line in file_in:
            urls.append(line.strip())
    # Make HTTP request to the URL
    for url in urls:
        if len(urls)==0:
            print("No URLS in input.txt")
            break
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'lxml')
        for elem in soup(['script','a', 'style', 'table', 'iframe', 'aside','pre','ins','li','ul','google-auto-placed ap_container','L-Affiliate-Tagged']):
             elem.extract()
        text = soup.get_text()
        text = ''.join(text).strip()
        topic_name = soup.find('h1',class_='post-full-title')
        parser = PlaintextParser.from_string(text, Tokenizer("english"))
        summarizer = TextRankSummarizer()
        summary = summarizer(parser.document, 10)
        text_summary = ""
        for sentence in summary:
            text_summary += str(sentence)
        with open(topic_name.get_text()+" summarised .txt", "w", encoding="utf-8") as text_file:
             text_file.write(text_summary)
    print("successfully converted from URL to summarised text file!")


# In[9]:


'''input_urls_file="C:\\Users\\Ambarish Deb\\Desktop\\project\\input.txt"
url_to_text_summary(input_urls_file)'''


# In[10]:


def text_to_summary(input_text):
    from sumy.parsers.plaintext import PlaintextParser
    from sumy.nlp.tokenizers import Tokenizer
    from sumy.summarizers.text_rank import TextRankSummarizer
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = TextRankSummarizer()
    summary = summarizer(parser.document, 10)
    text_summary = ""
    for sentence in summary:
        text_summary += str(sentence)
    with open("summarised .txt", "a", encoding="utf-8") as text_file:
        text_file.write(text_summary)


# In[12]:


def text_to_audio(input_text):
    from gtts import gTTS
    language = 'en'
    speech = gTTS(text=input_text, lang=language, slow=False)
    speech.save(name)
    os.system("mpg321 hello.mp3")
    print("successfully converted from text to audio!")
    


# In[20]:


import argparse


parser = argparse.ArgumentParser(description='Data Conversion from command line')

parser.add_argument('-f')
parser.add_argument('--from', dest='input_type', required=True,
                    help='Specify the input type: "url" or "text"')
parser.add_argument('--to', dest='output_type', required=True,
                    help='Specify the output type: "audio" or "summary"')
parser.add_argument('--input', dest='input_data', required=True,
                    help='Specify the input data: URL or text content')
'''parser.add_argument('--output', dest='output_file', 
                    help='Specify the output file path for audio or summary')'''


args = parser.parse_args()


input_type = args.input_type.lower()
output_type = args.output_type.lower()
input_data = args.input_data
'output_file = args.output_file'


if input_type == 'url' and output_type == 'audio':
    url_to_audio(input_data)
elif input_type == 'url' and output_type == 'text':
    url_to_text(input_data)
elif input_type == 'text' and output_type == 'audio':
    convert_text_to_audio(input_data)
elif input_type == 'text' and output_type == 'summary':
    text_to_summary(input_data)
elif input_type == 'text' and output_type == 'audio':
    text_to_audio(input_data)
else:
    print('please enter proper arguements')


# In[19]:


get_ipython().run_line_magic('tb', '')


# In[ ]:




