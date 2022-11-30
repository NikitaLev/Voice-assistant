# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import vosk
import queue
from fuzzywuzzy import fuzz
import datetime
import webbrowser
import random
from pywinauto.application import Application
import config
import speaker
from num2t4ru import num2text
from text_to_num import text2num
import word_worker as word
import test_listen
import threading


def va_respond(voice: str):
    if voice.startswith(config.VA_ALIAS):
        cmd = recognize_cmd(filter_cmd(voice))
        if cmd['cmd'] not in config.VA_CMD_LIST.keys():
            speaker.va_speak("Что?")
        else:
            execute_cmd(cmd['cmd'])


def recognize_cmd(cmd: str):
    rc = {'cmd': '', 'percent': 0}
    for c, v in config.VA_CMD_LIST.items():
        for x in v:
            vrt = fuzz.ratio(cmd, x)
            if vrt > rc['percent']:
                rc['cmd'] = c
                rc['percent'] = vrt

    return rc


def filter_cmd(raw_voice: str):
    cmd = raw_voice
    print(cmd)
    for x in config.VA_ALIAS:
        cmd = cmd.replace(x, "").strip()

    for x in config.VA_TBR:
        cmd = cmd.replace(x, "").strip()

    return cmd


def execute_cmd(cmd: str):
    if cmd == 'help':
        # help
        text = "Я умею: ..."
        text += "произносить время ..."
        text += "рассказывать анекдоты ..."
        text += "и открывать браузер"
        speaker.va_speak(text)
        pass
    elif cmd == 'ctime':
        # current time
        now = datetime.datetime.now()
        text = "Сейч+ас " + num2text(now.hour) + " " + num2text(now.minute)
        speaker.va_speak(text)
    elif cmd == 'joke':
        jokes = ['Как смеются программисты? ... ехе ехе ехе',
                 'ЭсКьюЭль запрос заходит в бар, подходит к двум столам и спрашивает .. «м+ожно присоединиться?»',
                 'Программист это машина для преобразования кофе в код']
        speaker.va_speak(random.choice(jokes))
    elif cmd == 'open_browser':
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open("http://python.org")

    elif cmd == 'what_we_say_to_god':
        txt = 'не сегодня, господин'
        speaker.va_speak(txt)

    elif cmd == 'heeelp':
        txt = 'памагитииииии'
        speaker.va_speak(txt)

    elif cmd == 'test':
        txt = ['я тебе что, . собака?']
        speaker.va_speak(random.choice(txt))
    elif cmd == 'dota_start':
        txt = ['трезвость, ....   там куда мы направляемся, она нам не понадобится',
               'покой нам только снится, анал, орал и чечевица']
        speaker.va_speak(random.choice(txt))
        path = 'E:\\steam\\steamapps\\common\\dota 2 beta\\game\\bin\\win64\\'
        # app = Application().start("C:/Users/Mikita.Leventsyeu/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Steam/Steam %s")
        app = Application(backend='uia').start(path + 'dota2.exe')
    elif cmd == 'EpicGamesStore':
        txt = 'трезвость, ....   там куда мы направляемся, она нам не понадобится'
        speaker.va_speak(random.choice(txt))
        path = 'E:\\epic\\Epic Games\\Launcher\\Portal\\Binaries\\Win32\\'
        # app = Application().start("C:/Users/Mikita.Leventsyeu/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Steam/Steam %s")
        app = Application(backend='uia').start(path + 'EpicGamesLauncher.exe')
    elif cmd == 'Fortnite':
        txt = 'трезвость, ....   там куда мы направляемся, она нам не понадобится'
        speaker.va_speak(random.choice(txt))
        path = 'E:\\epic\\Fortnite\\FortniteGame\\Binaries\\Win64\\'
        # app = Application().start("C:/Users/Mikita.Leventsyeu/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Steam/Steam %s")
        app = Application(backend='uia').start(path + 'FortniteLauncher.exe')
    elif cmd == 'steam_start':
        txt = ['запускаю стим, господин',
               'самое время для отдыха, господин']
        speaker.va_speak(random.choice(txt))
        path = 'E:\\steam\\'
        app = Application(backend='uia').start(path + 'steam.exe')
    elif cmd == 'notepad':
        txt = ['если вам что-то нужно написать, пишите сами, я пока этого не умею']
        speaker.va_speak(random.choice(txt))
        app = Application(backend='uia').start('notepad.exe')


# app = Application().start("notepad.exe")
# app.UntitledNotepad.Edit.type_keys("йцукен гшщ зх!", with_spaces = True)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    """word.start_print()

    word.set_standart_text()
    word.string_writer("text text text text text text")

    word.set_header_text(1)
    word.string_writer("Heading 1")

    word.set_standart_text()
    word.string_writer("text text text")

    word.bage_break()

    word.set_header_text(1)
    word.string_writer("Heading 2")

    word.set_standart_text()
    word.string_writer("text text text text text text")
    word.save_file()
 """

    params = {"callback": va_respond}

    task_listen = threading.Thread(name="listen_step_1", target=test_listen.va_listen, kwargs=params)
    task_listen.start()
    # test_listen.va_listen(va_respond)

# else:
#    print(rec.PartialResult())
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

