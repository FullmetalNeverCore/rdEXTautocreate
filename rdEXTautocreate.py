import ujson
from dataclasses import dataclass
import os 
import wave
import contextlib


@dataclass 
class XData: 
        x : dict

@dataclass 
class DataToChnage:
    filename : str
    opt : str 
    val : str
    name_station : str
    fm : str

class MData():

    def __init__(self,fn) -> None:
        self.init_file = open(f'./{fn}.json','r+')  
        self.xd = XData({'0'})

    def overwriter(self,option,val):
        self.xd.x = ujson.load(self.init_file)
        self.init_file.seek(0)
        self.xd.x[str(option)] = str(val) if type(val) == str else float(val)

    def dumper(self):
        ujson.dump(self.xd.x,self.init_file,indent=4)
        self.init_file.truncate()
        print("DUMPED")
        
    def song_writer(self): 
        print("Preparing to dump wav names.")
        timecodes = []
        list_names = [x for x in os.listdir('./') if '.wav' in x]
        final_lines = {}
        for x in list_names:
            with contextlib.closing(wave.open(x,'r')) as f:
                frames = f.getnframes()
                rate = f.getframerate()
                duration = frames / float(rate)
            final_lines[f'{main.dtc.name_station}\\{x}'] = int(duration)
        self.xd.x = final_lines


class Main:
    dtc = DataToChnage('1','1','1','1','1')
    cor_opt = ['displayName','fm','metadata','songInfo']

    def start():
        print(main.dtc.filename)
        main.dtc.name_station = input("Input name of station: ")
        main.dtc.fm = input("Input name of fm: ")
        print(f"{main.dtc.filename} {main.dtc.opt} {main.dtc.val} {main.dtc.name_station}")
        main.writer()
    
    def writer():
            md = MData(f'metadata')
            md.overwriter(f'displayName',f'{main.dtc.name_station}')
            md.overwriter(f'fm',float(main.dtc.fm))
            md.dumper()
            md = MData(f'songInfos')
            md.song_writer()
            md.dumper()



            

if __name__ == "__main__":
    global main 
    main = Main
    main.start()
