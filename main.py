import binascii
import nfc
import threading
import os
import requests
import sys

class TagTool():
    def __init__(self):
        self.cl = nfc.ContactlessFrontend("usb")
        pass
    
    def on_connect(self, tag):

        self.idm = binascii.hexlify(tag._nfcid)
        print("IDm : " + str(self.idm))
        self.send_spread_sheet()

        return True

    def send_spread_sheet(self):
        url = "https://script.google.com/macros/s/AKfycbyGIsWY6NaG7T57WHzycbUb16ZR8WIaN1oqaTFrd5Nv-hFMTS4fCqxaAhjeAV_hqoDhdw/exec"
        response = requests.get(url + '?id=' + str(self.idm))
        print(response)

    def if_del(self):
        self.cl.close()


    def run(self):
        while True:
            self.cl.connect(rdwr={'on-connect' : self.on_connect})
            
def terminate(callbacks):
    while True:
        n = input()
        if n == "e":
            for callback in callbacks:
                callback
            print("Terminate")
            sys.exit()


def main():
    tt = TagTool()
    tt_th = threading.Thread(target=tt.run)
    tt_th.setDaemon(True)
    tt_th.start()
    terminate(callbacks = [tt.if_del])

if __name__ == "__main__":
    main()