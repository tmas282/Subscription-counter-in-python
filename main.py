import PySimpleGUI as sg
import threading
import requests
import time
def api_all(id,window):
        while True:
                #request subs
                api_sub = "https://www.googleapis.com/youtube/v3/channels?part=statistics&id={}&key=AIzaSyCfwPAY-oTL1NGg5oIv5fu4rKWO-ujgSks".format(id)
                rs = requests.get(api_sub) #request subs
                subs = int(rs.json()["items"][0]["statistics"]["subscriberCount"])
                window["-subs-"].Update("{} inscritos".format(subs))
                
                # request nome
                api_nome = "https://www.googleapis.com/youtube/v3/channels?part=snippet&id={}&key=AIzaSyCfwPAY-oTL1NGg5oIv5fu4rKWO-ujgSks".format(id)
                rn = requests.get(api_nome) # request nome
                nome = str(rn.json()["items"][0]["snippet"]["title"])
                window["-channel-"].Update("{}".format(nome))
                for i in range(15):
                        time.sleep(1)
                        print("Update time:",i)
def run():
    subs=0
    sg.theme("dark grey 9")
    layout=[[sg.Text("CONTADOR DE SUBS",text_color="red",size=(20, 0),font=("Algerian", 30))],
            [sg.Text("'Canal'",key="-channel-",size=(20,0), font=("Agency FB", 20))],
            [sg.Text("'Inscritos'",key="-subs-",size=(20,0), font=("Agency FB", 20))],
            [sg.Text("Insira o seu channel id: ",text_color="yellow", font=("Calibri", 10))],
            [sg.Input("",key="channel_id")],
            [sg.Button("Começar")]]
    window = sg.Window("Contador Subs", layout)
    subscriber_up_thread = None #subscriber update thread
    while True:
        event, values = window.read()
        id=values["channel_id"]
        if subscriber_up_thread != None:
                subscriber_up_thread = threading.Thread(target=api_all, args=(id, window)).join()
                subscriber_up_thread = threading.Thread(target=api_all, args=(id, window)).start()
        elif subscriber_up_thread == None:
            subscriber_up_thread = threading.Thread(target=api_all, args=(id, window)).start()
run()
    