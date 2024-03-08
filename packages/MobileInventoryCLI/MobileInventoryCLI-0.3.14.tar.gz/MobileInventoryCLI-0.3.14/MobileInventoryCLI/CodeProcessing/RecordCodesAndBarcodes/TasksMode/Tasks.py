from MobileInventoryCLI.CodeProcessing.RecordCodesAndBarcodes.DB.db import *
import MobileInventoryCLI.CodeProcessing.RecordCodesAndBarcodes.Unified.Unified as unified

import random
from colored import Style,Fore
import json

class TasksMode:
    def getTotalwithBreakDownForScan(self):
        while True:
            color1=Fore.red
            color2=Fore.yellow
            color3=Fore.cyan
            color4=Fore.green_yellow

            scanned=input("barcode|code: ")
            if scanned in self.options['1']['cmds']:
                self.options['1']['exec']()
            elif scanned in self.options['2']['cmds']:
                return
            else:
                with Session(self.engine) as session:
                    result=session.query(Entry).filter(or_(Entry.Barcode==scanned,Entry.Code==scanned)).first()
                    if result:
                        total=0
                        for f in self.valid_fields:
                            if f not in self.special:
                                if getattr(result,f) not in [None,'']:
                                    total+=float(getattr(result,f))
                        print(result)
                        print(f"{color1}Amount Needed Total is {Style.reset}{color2}{Style.bold}{total}{Style.reset}!")
                        
                    else:
                        print(f"{Fore.red}{Style.bold}No such Barcode|Code:{scanned}{Style.reset}")

            

    def display_field(self,fieldname):
        color1=Fore.red
        color2=Fore.yellow
        color3=Fore.cyan
        color4=Fore.green_yellow
        m=f"Item Num |Name|Barcode|Code|{fieldname}"
        hr='-'*len(m)
        print(f"{m}\n{hr}")
        if fieldname in self.valid_fields:
            with Session(self.engine) as session:
                results=session.query(Entry).filter(Entry.InList==True).all()
                if len(results) < 1:
                    print(f"{Fore.red}{Style.bold}Nothing is in List!{Style.reset}")
                for num,result in enumerate(results):
                    print(f"{Fore.red}{num}{Style.reset} -> {color1}{result.Name}{Style.reset}|{color2}{result.Barcode}{Style.reset}|{color3}{result.Code}{Style.reset}|{color4}{getattr(result,fieldname)}{Style.reset}")
        print(f"{m}\n{hr}")

    def setFieldInList(self,fieldname):
        while True:
            if fieldname not in self.special or fieldname in ['Facings']:
                m=f"Item Num |Name|Barcode|Code|{fieldname}"
                hr='-'*len(m)
                print(f"{m}\n{hr}")
                if fieldname in self.valid_fields:
                    with Session(self.engine) as session:
                        code=''
                        while True:
                            code=input("barcode|code: ")
                            if code in self.options['1']['cmds']:
                                self.options['1']['exec']()
                            elif code in self.options['2']['cmds']:
                                return
                            else:
                                break
                        value=0
                        while True:
                            value=input("amount|+amount|-amount: ")
                            if value in self.options['1']['cmds']:
                                self.options['1']['exec']()
                            elif value in self.options['2']['cmds']:
                                return
                            else:
                                try:
                                    color1=Fore.red
                                    color2=Fore.yellow
                                    color3=Fore.cyan
                                    color4=Fore.green_yellow 
                                    if value.startswith("-") or value.startswith("+"):
                                        value=float(eval(value))
                                        result=session.query(Entry).filter(or_(Entry.Barcode==code,Entry.Code==code)).first()
                                        if result:
                                            setattr(result,fieldname,getattr(result,fieldname)+float(value))
                                            result.InList=True
                                            session.commit()
                                            session.flush()
                                            session.refresh(result)
                                            print(f"{Fore.red}0{Style.reset} -> {color1}{result.Name}{Style.reset}|{color2}{result.Barcode}{Style.reset}|{color3}{result.Code}{Style.reset}|{color4}{getattr(result,fieldname)}{Style.reset}")
                                            print(f"{m}\n{hr}")

                                        else:
                                            n=Entry(Barcode=code,Code='',Name=code,InList=True,Note="New Item")
                                            setattr(n,fieldname,value)
                                            session.add(n)
                                            session.commit()
                                            session.flush()
                                            session.refresh(n)
                                            result=n
                                            print(f"{Fore.red}0{Style.reset} -> {color1}{result.Name}{Style.reset}|{color2}{result.Barcode}{Style.reset}|{color3}{result.Code}{Style.reset}|{color4}{getattr(result,fieldname)}{Style.reset}")

                                            print(f"{m}\n{hr}")
                                    else:
                                        value=float(eval(value))
                                        result=session.query(Entry).filter(or_(Entry.Barcode==code,Entry.Code==code)).first()
                                        if result:
                                            setattr(result,fieldname,value)
                                            result.InList=True
                                            session.commit()
                                            session.flush()
                                            session.refresh(result)
                                            print(f"{Fore.red}0{Style.reset} -> {color1}{result.Name}{Style.reset}|{color2}{result.Barcode}{Style.reset}|{color3}{result.Code}{Style.reset}|{color4}{getattr(result,fieldname)}{Style.reset}")

                                            print(f"{m}\n{hr}")

                                        else:
                                            n=Entry(Barcode=code,Code='',Name=code,InList=True,Note="New Item")
                                            setattr(n,fieldname,value)
                                            session.add(n)
                                            session.commit()
                                            session.flush()
                                            session.refresh(n)
                                            result=n
                                            print(f"{Fore.red}0{Style.reset} -> {color1}{result.Name}{Style.reset}|{color2}{result.Barcode}{Style.reset}|{color3}{result.Code}{Style.reset}|{color4}{getattr(result,fieldname)}{Style.reset}")

                                            print(f"{m}\n{hr}")

                                            #raise Exception(result)
                                    break
                                except Exception as e:
                                    print(e)
            else:
                #code for tags,caseId[br,6w,ld],
                self.processSpecial(fieldname)
                break
    helpText_barcodes=f"""
    1. Enter the EntryId into the prompt
    2. if an entry is found you will be prompted for a code to be saved
    """
    def setBarcodes(self,fieldname):
         while True:
            try:
                cmd=input("Do What[help/q/b/$EntryId]?: ")
                if cmd.lower() in ['help',]:
                    print(self.helpText_barcodes)
                elif cmd.lower() in ['q','quit']:
                    exit("user quit!")
                elif cmd.lower() in ['b','back']:
                    return
                else:
                    with Session(self.engine) as session:
                        r=session.query(Entry).filter(Entry.EntryId==int(cmd)).first()
                        if r:
                            code=input(f"{fieldname} : ")
                            if code.lower() in ['help',]:
                                print(self.helpText_barcodes)
                            elif code.lower() in ['q','quit']:
                                exit("user quit!")
                            elif code.lower() in ['b','back']:
                                return
                            else:
                                setattr(r,fieldname,code)
                                session.commit()
                                session.flush()
                                session.refresh(r)
                                print(r)
            except Exception as e:
                print(e)



    def processSpecial(self,fieldname):
        if fieldname.lower() == "tags":
            self.editTags()
        elif 'Barcode' in fieldname:
            self.setBarcodes(fieldname)
        else:
            print("SpecialOPS Fields! {fieldname} Not Implemented Yet!")
            self.editCaseIds()


    helpText_caseIds=f'''
{Fore.green_yellow}$WHERE,$EntryId,exec()|$ID{Style.reset}
#[ld,6w,br,all],$EntryId,generate - create a synthetic id for case and save item to and save qrcode png of $case_id in $WHERE
#[ld,6w,br,all],$EntryId,$case_id - set case id for item in $WHERE
#[ld,6w,br,all],$EntryId - display item case id in $WHERE
[ld,6w,br,all],s|search,$case_id - display items associated with $case_id in $WHERE
#[ld,6w,br,all],$EntryId,clr_csid - set $case_id to '' in $WHERE
where:
 ld is for Load
 6w is 6-Wheeler or U-Boat
 br is BackRoom
 
 all will apply to all of the above fields
    '''
    def editCaseIds(self):
         while True:
            cmd=input("Do What[help]?: ")
            if cmd.lower() in ['help',]:
                print(self.helpText_caseIds)
            elif cmd.lower() in ['q','quit']:
                exit("user quit!")
            elif cmd.lower() in ['b','back']:
                return
            else:
                print(cmd)
                split_cmd=cmd.split(",")
                if len(split_cmd)==3:
                    mode=split_cmd[0]
                    eid=split_cmd[1]
                    ex=split_cmd[2]
                    if eid.lower() in ['s','search']:
                        #search
                        with Session(self.engine) as session:
                            results=[]
                            if split_cmd[0].lower() == '6w':
                                results=session.query(Entry).filter(Entry.CaseID_6W==ex).all()
                            elif split_cmd[0].lower() == 'ld':
                                results=session.query(Entry).filter(Entry.CaseID_LD==ex).all()
                            elif split_cmd[0].lower() == 'br':
                                results=session.query(Entry).filter(Entry.CaseID_BR==ex).all()
                            elif split_cmd[0].lower() == 'all':
                                results=session.query(Entry).filter(or_(Entry.CaseID_BR==ex,Entry.CaseID_LD==ex,Entry.CaseID_6W==ex)).all()
                            if len(results) < 1:
                                print(f"{Fore.dark_goldenrod}No Items to display!{Style.reset}")
                            for num,r in enumerate(results):
                                print(f"{Fore.red}{num}{Style.reset} -> {r}")
                    else:
                        with Session(self.engine) as session:
                            query=session.query(Entry).filter(Entry.EntryId==int(eid)).first()
                            if query:
                                if ex.lower() in ['clr_csid',]:
                                    if split_cmd[0].lower() == '6w':
                                        query.CaseID_6W=''
                                    elif split_cmd[0].lower() == 'ld':
                                        query.CaseID_LD=''
                                    elif split_cmd[0].lower() == 'br':
                                        query.CaseID_BR=''
                                    elif split_cmd[0].lower() == 'all':
                                        query.CaseID_6W=''
                                        query.CaseID_LD=''
                                        query.CaseID_BR=''
                                elif ex.lower() in ['generate','gen','g']:
                                    if split_cmd[0].lower() == '6w':
                                        query.CaseID_6W=query.synthetic_field_str()
                                    elif split_cmd[0].lower() == 'ld':
                                        query.CaseID_LD=query.synthetic_field_str()
                                    elif split_cmd[0].lower() == 'br':
                                        query.CaseID_BR=query.synthetic_field_str()
                                    elif split_cmd[0].lower() == 'all':
                                        query.CaseID_6W=query.synthetic_field_str()
                                        query.CaseID_LD=query.synthetic_field_str()
                                        query.CaseID_BR=query.synthetic_field_str()
                                else:
                                    if split_cmd[0].lower() == '6w':
                                        query.CaseID_6W=ex
                                    elif split_cmd[0].lower() == 'ld':
                                        query.CaseID_LD=ex
                                    elif split_cmd[0].lower() == 'br':
                                        query.CaseID_BR=ex
                                    elif split_cmd[0].lower() == 'all':
                                        query.CaseID_6W=ex
                                        query.CaseID_LD=ex
                                        query.CaseID_BR=ex
                                session.commit()
                                session.flush()
                                session.refresh(query)
                                print(f"""
    Name: {query.Name}
    Barcode: {query.Barcode}
    Code: {query.Code}
    EntryId: {query.EntryId}
    CaseId 6W: {query.CaseID_6W}
    CaseId LD: {query.CaseID_LD}
    CaseId BR: {query.CaseID_BR}
    """)
                elif len(split_cmd)==2:
                    with Session(self.engine) as session:
                        query=session.query(Entry).filter(Entry.EntryId==int(split_cmd[1]))
                        r=query.first()
                        if r:
                            if split_cmd[0].lower() == '6w':
                                print(r.CaseID_6W)
                            elif split_cmd[0].lower() == 'ld':
                                print(r.CaseID_LD)
                            elif split_cmd[0].lower() == 'br':
                                print(r.CaseID_BR)
                                #self.CaseID_BR=CaseID_BR
                                #self.CaseID_LD=CaseID_LD
                                #self.CaseID_6W=CaseID_6W
                        else:
                            print(f"{Fore.dark_goldenrod}No Such Item!{Style.reset}")
                else:
                    print(self.helpText_caseIds)


    helpText_tags=f'''
    {Fore.green_yellow}$mode[=|R,+,-],$TAG_TEXT,$fieldname,$id|$code|$barcode|$fieldData_to_id{Style.reset}
    {Fore.cyan}=|R{Style.reset} -> {Fore.yellow}{Style.bold}set Tag to $TAG_TEXT{Style.reset}
    {Fore.cyan}+{Style.reset} -> {Fore.yellow}{Style.bold}add $TAG_TEXT to Tag{Style.reset}
    {Fore.cyan}-{Style.reset} -> {Fore.yellow}{Style.bold}remove $TAG_TEXT from Tag{Style.reset}
    '''
    def editTags(self):
        while True:
            cmd=input("Do What[help]?: ")
            if cmd.lower() in ['help',]:
                print(self.helpText_tags)
            elif cmd.lower() in ['q','quit']:
                exit("user quit!")
            elif cmd.lower() in ['b','back']:
                return
            else:
                split_cmd=cmd.split(",")
                if len(split_cmd) == 4:
                    #$mode,$search_fieldname,$EntryId,$tag
                    mode=split_cmd[0]
                    tag=[split_cmd[1],] 
                    search_fieldname=split_cmd[2]
                    eid=int(split_cmd[3])
                    with Session(self.engine) as session:
                        result=session.query(Entry).filter(Entry.__dict__.get(search_fieldname)==eid).all()
                        for num,r in enumerate(result):
                            if r.Tags == '':
                                 r.Tags=json.dumps(list(tag))
                                 
                            if mode in ['=','r','R']:
                                r.Tags=json.dumps(list(tag))
                            elif mode == '+':
                                try:
                                    old=json.loads(r.Tags)
                                    old.append(tag[0])
                                    r.Tags=json.dumps(old)
                                except Exception as e:
                                    print(e)
                            elif mode == '-':
                                try:
                                    old=json.loads(r.Tags)
                                    i=old.index(tag[0])
                                    old.pop(i)
                                    r.Tags=json.dumps(old)
                                except Exception as e:
                                    print(e)
                                

                            
                            session.commit()
                            session.flush()
                            session.refresh(r)
                            print(r)
                else:
                    print(self.helpText_tags)


    def setName(self):
        with Session(self.engine) as session:
            code=''
            while True:
                code=input("barcode|code: ")
                if code in self.options['1']['cmds']:
                    self.options['1']['exec']()
                elif code in self.options['2']['cmds']:
                    return
                else:
                    break
            value=0
            while True:
                value=input("Name: ")
                if value in self.options['1']['cmds']:
                    self.options['1']['exec']()
                elif value in self.options['2']['cmds']:
                    return
                else:
                    result=session.query(Entry).filter(or_(Entry.Barcode==code,Entry.Code==code)).first()
                    if result:
                        result.Name=value
                        session.commit()
                        session.flush()
                        session.refresh(result)
                        print(result)
                    else:
                        print(f"{Fore.red}{Style.bold}No Such Item Identified by '{code}'{Style.reset}")
                    break
                            

    def __init__(self,engine,parent):
        self.engine=engine
        self.parent=parent
        self.special=['Tags','ALT_Barcode','DUP_Barcode','CaseID_6W','CaseID_BR','CaseID_LD','Facings']
        self.valid_fields=['Shelf',
        'BackRoom',
        'Display_1',
        'Display_2',
        'Display_3',
        'Display_4',
        'Display_5',
        'Display_6',
        'ALT_Barcode',
        'DUP_Barcode',
        'CaseID_BR',
        'CaseID_LD',
        'CaseID_6W',
        'Tags',
        'Facings',
        'SBX_WTR_DSPLY',
        'SBX_CHP_DSPLY',
        'SBX_WTR_KLR',
        'FLRL_CHP_DSPLY',
        'FLRL_WTR_DSPLY',
        'WD_DSPLY',
        'CHKSTND_SPLY',
        ]
        '''
        ALT_Barcode=Column(String)
        DUP_Barcode=Column(String)
        CaseID_BR=Column(String)
        CaseID_LD=Column(String)
        CaseID_6W=Column(String)
        Tags=Column(String)
        Facings=Column(Integer)
        SBX_WTR_DSPLY=Column(Integer)
        SBX_CHP_DSPLY=Column(Integer)
        SBX_WTR_KLR=Column(Integer)
        FLRL_CHP_DSPLY=Column(Integer)
        FLRL_WTR_DSPLY=Column(Integer)
        WD_DSPLY=WD_DSPLY=Column(Integer)
        CHKSTND_SPLY=CHKSTND_SPLY=Column(Integer)
        '''
        #self.display_field("Shelf")
        self.options={
                '1':{
                    'cmds':['q','quit','#1'],
                    'desc':"quit program",
                    'exec':lambda: exit("user quit!"),
                    },
                '2':{
                    'cmds':['b','back','#2'],
                    'desc':'go back menu if any',
                    'exec':None
                    },
                }
        #autogenerate duplicate functionality for all valid fields for display
        count=3
        for entry in self.valid_fields:
            self.options[entry]={
                    'cmds':["#"+str(count),f"ls {entry}"],
                    'desc':f'list needed @ {entry}',
                    'exec':lambda self=self,entry=entry: self.display_field(f"{entry}"),
                    }
            count+=1
        #setoptions
        #self.setFieldInList("Shelf")
        for entry in self.valid_fields:
            self.options[entry+"_set"]={
                    'cmds':["#"+str(count),f"set {entry}"],
                    'desc':f'set needed @ {entry}',
                    'exec':lambda self=self,entry=entry: self.setFieldInList(f"{entry}"),
                    }
            count+=1
        self.options["lu"]={
                    'cmds':["#"+str(count),f"lookup","lu","check","ck"],
                    'desc':f'get total for valid fields',
                    'exec':lambda self=self,entry=entry: self.getTotalwithBreakDownForScan(),
                    }
        count+=1
        self.options["setName"]={
                    'cmds':["#"+str(count),f"setName","sn"],
                    'desc':f'set name for item by barcode!',
                    'exec':lambda self=self,entry=entry: self.setName(),
                    }
        count+=1


        while True:
            command=input(f"{Style.bold}{Fore.green}do what[??/?]:{Style.reset} ")
            if self.parent != None and self.parent.Unified(command):
                print("ran an external command!")
            elif command == "??":
                for num,option in enumerate(self.options):
                    color=Fore.dark_goldenrod
                    color1=Fore.cyan
                    if (num%2)==0:
                        color=Fore.green_yellow
                        color1=Fore.magenta
                    print(f"{color}{self.options[option]['cmds']}{Style.reset} - {color1}{self.options[option]['desc']}{Style.reset}")
            else:
                for option in self.options:
                    if self.options[option]['exec'] != None and command.lower() in self.options[option]['cmds']:
                        self.options[option]['exec']()
                    elif self.options[option]['exec'] == None and command.lower() in self.options[option]['cmds']:
                        return
               



if __name__ == "__main__":
    TasksMode(parent=None,engine=ENGINE)
