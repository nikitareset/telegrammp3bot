{\rtf1\ansi\ansicpg1252\cocoartf2580
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;\f1\fnil\fcharset0 AppleColorEmoji;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww14200\viewh14040\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import telebot\
from flask import Flask\
import threading\
import random\
import os\
\
TOKEN = os.environ.get('BOT_TOKEN')\
CHANNEL_ID = os.environ.get('CHANNEL_ID')\
\
bot = telebot.TeleBot(TOKEN)\
app = Flask(__name__)\
\
@app.route('/')\
def home():\
    return "\uc0\u1041 \u1086 \u1090  \u1088 \u1072 \u1073 \u1086 \u1090 \u1072 \u1077 \u1090 !"\
\
REPLIES = [\
    "\uc0\u1043 \u1086 \u1090 \u1086 \u1074 \u1086 , \u1089 \u1087 \u1072 \u1089 \u1080 \u1073 \u1086  \u1073 \u1088 \u1086 !",\
    "\uc0\u1055 \u1088 \u1080 \u1085 \u1103 \u1083 , \u1073 \u1088 \u1072 \u1090 !",\
    "\uc0\u1047 \u1072 \u1082 \u1072 \u1079  \u1074  \u1086 \u1073 \u1088 \u1072 \u1073 \u1086 \u1090 \u1082 \u1077  
\f1 \uc0\u55357 \u56384 
\f0 ",\
    "\uc0\u1057 \u1086 \u1093 \u1088 \u1072 \u1085 \u1080 \u1083  \u1074  \u1085 \u1077 \u1081 \u1088 \u1086 \u1072 \u1088 \u1093 \u1080 \u1074  
\f1 \uc0\u55358 \u56800 
\f0 ",\
    "\uc0\u1054 \u1090 \u1083 \u1080 \u1095 \u1085 \u1099 \u1081  \u1074 \u1099 \u1073 \u1086 \u1088 !",\
    "\uc0\u1054 \u1073 \u1103 \u1079 \u1072 \u1090 \u1077 \u1083 \u1100 \u1085 \u1086  \u1076 \u1086 \u1073 \u1072 \u1074 \u1083 \u1102  \u1085 \u1072  \u1092 \u1083 \u1077 \u1096 \u1082 \u1091 !",\
    "\uc0\u1061 \u1086 \u1088 \u1086 \u1096 \u1080 \u1081  \u1090 \u1088 \u1077 \u1082 , \u1079 \u1072 \u1087 \u1086 \u1084 \u1085 \u1080 \u1083 !",\
    "\uc0\u1054 \u1082 \u1077 \u1081 , \u1082 \u1080 \u1076 \u1072 \u1081  \u1077 \u1097 \u1105  \u1077 \u1089 \u1083 \u1080  \u1077 \u1089 \u1090 \u1100 !",\
    "\uc0\u1040 \u1088 \u1090 \u1105 \u1084  \u1073 \u1091 \u1076 \u1077 \u1090  \u1076 \u1086 \u1074 \u1086 \u1083 \u1077 \u1085  
\f1 \uc0\u55357 \u56846 
\f0 ",\
    "\uc0\u1057 \u1091 \u1087 \u1077 \u1088 , \u1091  \u1084 \u1077 \u1085 \u1103  \u1082 \u1072 \u1082  \u1088 \u1072 \u1079  \u1091 \u1078 \u1077  \u1086 \u1085  \u1077 \u1089 \u1090 \u1100 !",\
    "\uc0\u1044 \u1086 \u1073 \u1072 \u1074 \u1080 \u1083  \u1074  \u1087 \u1083 \u1077 \u1081 \u1083 \u1080 \u1089 \u1090 !"\
]\
\
@bot.message_handler(content_types=['text', 'photo', 'video', 'document', 'audio', 'voice'])\
def handle_all(message):\
    try:\
        content_type = message.content_type\
        if content_type == 'text':\
            bot.send_message(CHANNEL_ID, f"\uc0\u1057 \u1086 \u1086 \u1073 \u1097 \u1077 \u1085 \u1080 \u1077  \u1086 \u1090  @\{message.chat.username or '\u1087 \u1086 \u1083 \u1100 \u1079 \u1086 \u1074 \u1072 \u1090 \u1077 \u1083 \u1100 '\}:\\n\{message.text\}")\
        elif content_type == 'photo':\
            file_id = message.photo[-1].file_id\
            caption = message.caption or ''\
            bot.send_photo(CHANNEL_ID, file_id, caption=f"@\{message.chat.username or '\uc0\u1087 \u1086 \u1083 \u1100 \u1079 \u1086 \u1074 \u1072 \u1090 \u1077 \u1083 \u1100 '\}: \{caption\}")\
        elif content_type == 'document':\
            bot.send_document(CHANNEL_ID, message.document.file_id, caption=f"\uc0\u1044 \u1086 \u1082 \u1091 \u1084 \u1077 \u1085 \u1090  \u1086 \u1090  @\{message.chat.username or '\u1087 \u1086 \u1083 \u1100 \u1079 \u1086 \u1074 \u1072 \u1090 \u1077 \u1083 \u1100 '\}")\
        elif content_type == 'video':\
            bot.send_video(CHANNEL_ID, message.video.file_id, caption=f"\uc0\u1042 \u1080 \u1076 \u1077 \u1086  \u1086 \u1090  @\{message.chat.username or '\u1087 \u1086 \u1083 \u1100 \u1079 \u1086 \u1074 \u1072 \u1090 \u1077 \u1083 \u1100 '\}")\
        elif content_type == 'audio':\
            bot.send_audio(CHANNEL_ID, message.audio.file_id, caption=f"\uc0\u1040 \u1091 \u1076 \u1080 \u1086  \u1086 \u1090  @\{message.chat.username or '\u1087 \u1086 \u1083 \u1100 \u1079 \u1086 \u1074 \u1072 \u1090 \u1077 \u1083 \u1100 '\}")\
        elif content_type == 'voice':\
            bot.send_voice(CHANNEL_ID, message.voice.file_id, caption=f"\uc0\u1043 \u1086 \u1083 \u1086 \u1089 \u1086 \u1074 \u1086 \u1077  \u1086 \u1090  @\{message.chat.username or '\u1087 \u1086 \u1083 \u1100 \u1079 \u1086 \u1074 \u1072 \u1090 \u1077 \u1083 \u1100 '\}")\
        bot.reply_to(message, random.choice(REPLIES))\
    except Exception as e:\
        print(f"\uc0\u1054 \u1096 \u1080 \u1073 \u1082 \u1072 : \{e\}")\
\
def run_bot():\
    bot.polling()\
\
def run_web():\
    app.run(host='0.0.0.0', port=8080)\
\
threading.Thread(target=run_bot).start()\
threading.Thread(target=run_web).start()\
}