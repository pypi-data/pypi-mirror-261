import pandas as pd
import csv
from datetime import datetime
from pathlib import Path
from colored import Fore,Style,Back
from barcode import Code39,UPCA,EAN8,EAN13
import barcode,qrcode,os,sys,argparse
from datetime import datetime,timedelta
import zipfile,tarfile
import base64,json
from ast import literal_eval
import sqlalchemy
from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base as dbase
from sqlalchemy.ext.automap import automap_base
from pathlib import Path
import upcean

print("fores")
from MobileInventoryCLI.CodeProcessing.RecordCodesAndBarcodes.ExtractPkg.ExtractPkg2 import *
from MobileInventoryCLI.CodeProcessing.RecordCodesAndBarcodes.Lookup.Lookup import *
from MobileInventoryCLI.CodeProcessing.RecordCodesAndBarcodes.DayLog.DayLogger import *
from MobileInventoryCLI.CodeProcessing.RecordCodesAndBarcodes.DB.db import *
from MobileInventoryCLI.CodeProcessing.RecordCodesAndBarcodes.ConvertCode.ConvertCode import *
from MobileInventoryCLI.CodeProcessing.RecordCodesAndBarcodes.setCode.setCode import *
from MobileInventoryCLI.CodeProcessing.RecordCodesAndBarcodes.Locator.Locator import *
from MobileInventoryCLI.CodeProcessing.RecordCodesAndBarcodes.ListMode2.ListMode2 import *
from MobileInventoryCLI.CodeProcessing.RecordCodesAndBarcodes.TasksMode.Tasks import *
from MobileInventoryCLI.CodeProcessing.RecordCodesAndBarcodes.ExportList.ExportListCurrent import *


import MobileInventoryCLI.CodeProcessing.RecordCodesAndBarcodes.possibleCode as pc

class TouchStampC:
    def __init__(self,engine,parent):
        try:
            self.engine=engine
            self.parent=parent
            print("TouchStamp Locator for Fast Note Logging!")
            self.helpTxt=f"""
            + | +,Note,Barcode|Code - create a new touchstamp entry, '+' on its own will
                                              prompt for details; otherwise use details as describe
            e | e,Note,TouchStampId - edit a touchstamp entry, 'e' on its own will
                                              prompt for details; otherwise use details as describe
            - | -,TouchStampId - remove an entry by prompt ('-' on its own), or by TouchStampId
            l - list all
            l,$TouchStampId - list touch stamp id
            l,Note|TouchStampId,$searchable - search for in fields
            q|quit - quit program
            b|back - go back a menu
            """
            while True:
                cmd=input("do what? ")
                if cmd.lower() in ['q','quit']:
                    exit("user quit!")
                elif cmd.lower() in ['b','back']:
                    return
                elif cmd.lower() in ['?','help']:
                    print(self.helpTxt)
                elif cmd.split(",")[0].lower() in ['+']:
                    cmdline=cmd.split(",")
                    ct=len(cmdline)

                    if ct > 1 and ct == 3:
                        barcode=None
                        with Session(self.engine) as session:
                            bcd=session.query(Entry).filter(or_(Entry.Barcode==cmdline[2],Entry.Code==cmdline[2])).first()
                            print(bcd)
                            if bcd:
                                ts=TouchStamp(Note=cmdline[1],EntryId=bcd.EntryId)
                            else:
                                ts=TouchStamp(Note=cmdline[1],EntryId=None)
                            session.add(ts)
                            session.commit()
                            session.refresh(ts)
                            print(ts)
                    else:
                        code=input("Barcode|Code|q|quit|b|back: ")
                        if code.lower() in ['q','quit']:
                            exit("user quit")
                        elif code.lower() in ['b','back']:
                            return
                        else:
                            note=input("note|q|quit|b|back: ")
                            if note.lower() in ['q','quit']:
                                exit("user quit")
                            elif note.lower() in ['b','back']:
                                return
                            with Session(self.engine) as session:
                                bcd=session.query(Entry).filter(or_(Entry.Barcode==code,Entry.Code==code)).first()
                                print(bcd)

                                if bcd:
                                    ts=TouchStamp(Note=note,EntryId=bcd.EntryId)
                                else:
                                    ts=TouchStamp(Note=note,EntryId=None)
                                session.add(ts)
                                session.commit()
                                session.refresh(ts)
                                print(ts)
                elif cmd.split(",")[0].lower() in ['-']:
                    cmdline=cmd.split(",")
                    ct=len(cmdline)

                    if ct > 1 and ct == 2:
                        barcode=None
                        with Session(self.engine) as session:
                            r=session.query(TouchStamp).filter(TouchStamp.TouchStampId==int(cmdline[1])).delete()
                            session.commit()
                            print(f"deleted {r}")
                    else:
                        code=input("TouchStampId|q|quit|b|back: ")
                        if code.lower() in ['q','quit']:
                            exit("user quit")
                        elif code.lower() in ['b','back']:
                            return
                        else:
                            with Session(self.engine) as session:
                                bcd=session.query(TouchStamp).filter(TouchStamp.TouchStampId==int(code)).delete()
                                session.commit()
                                print(bcd)          
                elif cmd.split(",")[0].lower() in ['e']:
                    cmdline=cmd.split(",")
                    ct=len(cmdline)

                    if ct > 1 and ct == 3:
                        with Session(self.engine) as session:
                            tsid=int(cmdline[2])
                            ts=session.query(TouchStamp).filter(TouchStamp.TouchStampId==tsid).first()
                            if ts:
                                note=input("Note: ")
                                if note.startswith("+"):
                                    ts.Note+=note
                                elif note.endswith("+"):
                                    ts.Note=note+ts.Note
                                elif note.startswith("-"):
                                    ts.Note.replace(note,' '*len(note))
                                else:
                                    ts.Note=note
                                print(ts)
                            else:
                                print(f"No Such TouchStampId!")
                            session.commit()
                    else:
                        with Session(self.engine) as session:
                            tsid=int(input("TouchStampId: "))
                            ts=session.query(TouchStamp).filter(TouchStamp.TouchStampId==tsid).first()
                            if ts:
                                note=input("Note: ")
                                if note.startswith("+"):
                                    ts.Note+=note
                                elif note.endswith("+"):
                                    ts.Note=note+ts.Note
                                elif note.startswith("-"):
                                    ts.Note.replace(note,' '*len(note))
                                else:
                                    ts.Note=note
                                print(ts)
                            else:
                                print(f"No Such TouchStampId!")
                            session.commit()
                elif cmd.split(",")[0].lower() in ['l']:
                    cmdline=cmd.split(",")
                    ct=len(cmdline)
                    if ct == 1:
                        with Session(self.engine) as session:
                            results=session.query(TouchStamp).all()
                            ct=len(results)
                            for num,i in enumerate(results):
                                print(f"{num}/{ct} -> {i}")
                    elif ct > 1 and ct == 2:
                       with Session(self.engine) as session:
                            results=session.query(TouchStamp).filter(TouchStamp.TouchStampId==int(cmdline[1])).all()
                            ct=len(results)
                            for num,i in enumerate(results):
                                print(f"{num}/{ct} -> {i}")
                    elif ct > 1 and ct == 3:
                        field=cmdline[1]
                        if field not in ['Timestamp',]:
                            if field == 'Note':
                                with Session(self.engine) as session:
                                    results=session.query(TouchStamp).filter(TouchStamp.Note.icontains(cmdline[2].lower())).all()
                                    ct=len(results)
                                    for num,i in enumerate(results):
                                        print(f"{num}/{ct} -> {i}")
                                    print(f"Total Results {ct}")
                            elif field == "TouchStampId":
                                with Session(self.engine) as session:
                                    results=session.query(TouchStamp).filter(TouchStamp.TouchStampId==int(cmdline[2])).all()
                                    ct=len(results)
                                    for num,i in enumerate(results):
                                        print(f"{num}/{ct} -> {i}")
                                    print(f"Total Results {ct}") 
                            else:
                                print("Unsupported Field to Search!")
                        #list items by searching field
                    else:
                        print(self.helpTxt)
                        #prompt for field to search
                        #print relevant touchstamps
                
        except Exception as e:
            print(e)
        except Exception as e:
            print(e)