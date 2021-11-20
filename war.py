# EDIT :Fareel
from function import *
from Naked.toolshed.shell import execute_js 
import ast, time, random, json, codecs, re, subprocess
#=========================================================
login = codecs.open("token.json","r","utf-8")
Login = json.load(login)
appNya0="ANDROIDLITE\t2.16.0\tAndroid OS\t7.1.2"
appNya1="ANDROIDLITE\t2.17.0\tAndroid OS\t6.0.1"
appNya2="ANDROIDLITE\t2.16.0\tAndroid OS\t8.0.0"
appNya3="ANDROIDLITE\t2.17.0\tAndroid OS\t6.0.1"
appNya4="ANDROIDLITE\t2.17.0\tAndroid OS\t10"
appNya5="ANDROIDLITE\t2.17.0\tAndroid OS\t8.0.0"
appNya6="ANDROIDLITE\t2.16.0\tAndroid OS\t11"
appNya7="ANDROIDLITE\t2.17.0\tAndroid OS\t7.1.2"
appNya8="ANDROIDLITE\t2.16.0\tAndroid OS\t11"
appNya9="ANDROIDLITE\t2.17.0\tAndroid OS\t6.0.1"
appNya10="ANDROIDLITE\t2.17.0\tAndroid OS\t7.1.2"
appNya11="ANDROIDLITE\t2.17.0\tAndroid OS\t9.0"
#=========================================================
cl = Farel(myToken=str(Login["CL"]), myApp=appNya0)
aa = Farel(myToken=str(Login["AA"]), myApp=appNya1)
bb = Farel(myToken=str(Login["BB"]), myApp=appNya2)
cc = Farel(myToken=str(Login["CC"]), myApp=appNya3)
dd = Farel(myToken=str(Login["DD"]), myApp=appNya4)
ee = Farel(myToken=str(Login["EE"]), myApp=appNya5)
ff = Farel(myToken=str(Login["FF"]), myApp=appNya6)
gg = Farel(myToken=str(Login["GG"]), myApp=appNya7)
hh = Farel(myToken=str(Login["HH"]), myApp=appNya8)
ii = Farel(myToken=str(Login["II"]), myApp=appNya9)
jj = Farel(myToken=str(Login["JJ"]), myApp=appNya10)
kk = Farel(myToken=str(Login["KK"]), myApp=appNya11)
print("LOGIN SUSKSES")
#=========================================================>>
mid = cl.getProfile().mid;Amid = aa.getProfile().mid;Bmid = bb.getProfile().mid;Cmid = cc.getProfile().mid;Dmid = dd.getProfile().mid;Emid = ee.getProfile().mid;Fmid = ff.getProfile().mid;Gmid = gg.getProfile().mid;Hmid = hh.getProfile().mid;Imid = ii.getProfile().mid;Jmid = jj.getProfile().mid;Kmid = kk.getProfile().mid
tiktik = codecs.open("FarelWar.json","r","utf-8")
FarelBot = json.load(tiktik)
Bacok =[aa,bb,cc,dd,ee,ff,gg,hh,ii,jj,kk]
def backup():
    try:
        backup = FarelBot
        f = codecs.open('FarelWar.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        print(error)
        return False
FarelBot['list']['bot'] = [];FarelBot['list']['bot'].append(mid);FarelBot['list']['bot'].append(Amid);FarelBot['list']['bot'].append(Bmid);FarelBot['list']['bot'].append(Cmid);FarelBot['list']['bot'].append(Dmid);FarelBot['list']['bot'].append(Emid);FarelBot['list']['bot'].append(Fmid);FarelBot['list']['bot'].append(Gmid);FarelBot['list']['bot'].append(Hmid);FarelBot['list']['bot'].append(Imid);FarelBot['list']['bot'].append(Jmid);FarelBot['list']['bot'].append(Kmid);backup()
#=========================================================
settings = {
    "selfbot": True,
}
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def restartBot():
    python = sys.executable
    os.execl(python, python, *sys.argv)
#=========================================================
helpM ="""
╔⚜️ Fareel Bots ⚜️
║🔰ping
║🔰help
║🔰speed
║🔰/blc
║🔰cban
║🔰onpro
║🔰offpro
║🔰onjoin
║🔰offjoin
║🔰listpro
║🔰rchat
║🔰.cek
║🔰botn1: [1/9]
║🔰.myname
║🔰mypic
║🔰allpic
║🔰allme:
║🔰in [asis]
║🔰sepak  [kiick]
║🔰/out [asis]
║🔰/by [induk]
║🔰/groups
║🔰listadmin
║🔰admin [addamin]
║🔰adell [hapusadmin]
║🔰bdell [hapusbot]
║🔰bot [addbot]
║🔰listbot
║🔰/reset
║🔰.allkick [kickall]
╚⚜️FarelBot.Version⚜️
"""
def worker(op):
    global time
    global ast
    global groupParam
    try:
        if op.type in [0]:
            return
#=========================================================
        if op.type in [11,122]:
            try:
                if op.param1 in FarelBot['list']['protect']:
                    if op.param2 not in FarelBot['list']['owner'] and op.param2 not in FarelBot['list']['bot'] and op.param2 not in FarelBot['list']['admin']:
                        FarelBot["list"]["bleclist"][op.param2] = True
                        backup()
                        try:
                            Crot = []
                            for Patek in Bacok:
                                if op.param1 in Patek.getGroupIdsJoined():
                                    Crot.append(Patek)
                            L = random.choice(Crot)
                            deleteOtherFromChat(op.param1,[op.param2])
                            chat = L.getChats([op.param1])
                            if chat.chats[0].extra.groupExtra.preventedJoinByTicket == False:
                                chat.chats[0].extra.groupExtra.preventedJoinByTicket = True
                                L.updateChat(chat.chats[0],4)
                            else:pass
                        except:pass
            except:pass
#=========================================================
        if op.type in [13,124]:
            try:
                Sayang = [mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid,Kmid]
                for pasukan in Sayang:
                    if pasukan in op.param3.split("\x1e"):
                        if op.param2 not in FarelBot['list']['owner'] and op.param2 not in FarelBot['list']['bot'] and op.param2 not in FarelBot['list']['admin']:
                            pass
                        else:
                            KKami = [cl,aa,bb,cc,dd,ee,ff,gg,hh,ii,jj,kk]
                            for kawankuu in KKami:
                                try:
                                    if op.param1 not in kawankuu.getGroupIdsJoined():
                                        kawankuu.acceptChatInvitation(op.param1)
                                    else:pass
                                except:pass
                    else:pass
            except:pass
        if op.type in [13,124]:
            if op.param1 in FarelBot["list"]["protect"]:
                if op.param2 not in FarelBot['list']['owner'] and op.param2 not in FarelBot['list']['bot'] and op.param2 not in FarelBot['list']['admin']:
                    FarelBot["list"]["bleclist"][op.param2] = True
                    backup()
                    try:
                        inv1 = op.param3.replace('\x1e',',')
                        inv2 = inv1.split(',')
                        for userban in inv2:
                            if userban in FarelBot["list"]["bleclist"]:
                                aa.cancelChatInvitation(op.param1,[userban])
                            aa.deleteOtherFromChat(op.param1,[op.param2])
                    except:
                        try:
	                        inv1 = op.param3.replace('\x1e',',')
	                        inv2 = inv1.split(',')
	                        for userban in inv2:
	                            if userban in FarelBot["list"]["bleclist"]:
	                                bb.cancelChatInvitation(op.param1,[userban])
	                            bb.deleteOtherFromChat(op.param1,[op.param2])
                        except:
                            try:
	                            inv1 = op.param3.replace('\x1e',',')
	                            inv2 = inv1.split(',')
	                            for userban in inv2:
		                            if userban in FarelBot["list"]["bleclist"]:
		                                cc.cancelChatInvitation(op.param1,[userban])
		                            cc.deleteOtherFromChat(op.param1,[op.param2])
                            except:
	                            try:
		                            inv1 = op.param3.replace('\x1e',',')
		                            inv2 = inv1.split(',')
		                            for userban in inv2:
			                            if userban in FarelBot["list"]["bleclist"]:
			                                dd.cancelChatInvitation(op.param1,[userban])
			                            dd.deleteOtherFromChat(op.param1,[op.param2])
	                            except:
		                            try:
			                            inv1 = op.param3.replace('\x1e',',')
			                            inv2 = inv1.split(',')
			                            for userban in inv2:
				                            if userban in FarelBot["list"]["bleclist"]:
				                                ee.cancelChatInvitation(op.param1,[userban])
				                            ee.deleteOtherFromChat(op.param1,[op.param2])
		                            except:
			                            try:
				                            inv1 = op.param3.replace('\x1e',',')
				                            inv2 = inv1.split(',')
				                            for userban in inv2:
					                            if userban in FarelBot["list"]["bleclist"]:
					                                ff.cancelChatInvitation(op.param1,[userban])
					                            ff.deleteOtherFromChat(op.param1,[op.param2])
			                            except:
				                            try:
					                            inv1 = op.param3.replace('\x1e',',')
					                            inv2 = inv1.split(',')
					                            for userban in inv2:
						                            if userban in FarelBot["list"]["bleclist"]:
						                                gg.cancelChatInvitation(op.param1,[userban])
						                            gg.deleteOtherFromChat(op.param1,[op.param2])
				                            except:
					                            try:
						                            inv1 = op.param3.replace('\x1e',',')
						                            inv2 = inv1.split(',')
						                            for userban in inv2:
							                            if userban in FarelBot["list"]["bleclist"]:
							                                hh.cancelChatInvitation(op.param1,[userban])
							                            hh.deleteOtherFromChat(op.param1,[op.param2])
					                            except:
						                            try:
							                            inv1 = op.param3.replace('\x1e',',')
							                            inv2 = inv1.split(',')
							                            for userban in inv2:
								                            if userban in FarelBot["list"]["bleclist"]:
								                                ii.cancelChatInvitation(op.param1,[userban])
								                            ii.deleteOtherFromChat(op.param1,[op.param2])
						                            except:
							                            try:
								                            inv1 = op.param3.replace('\x1e',',')
								                            inv2 = inv1.split(',')
								                            for userban in inv2:
									                            if userban in FarelBot["list"]["bleclist"]:
										                            jj.cancelChatInvitation(op.param1,[userban])
									                            jj.deleteOtherFromChat(op.param1,[op.param2])
							                            except:
								                            try:
									                            inv1 = op.param3.replace('\x1e',',')
									                            inv2 = inv1.split(',')
									                            for userban in inv2:
										                            if userban in FarelBot["list"]["bleclist"]:
											                            kk.cancelChatInvitation(op.param1,[userban])
										                            kk.deleteOtherFromChat(op.param1,[op.param2])
								                            except:
									                            pass
                else:pass
                return
        if op.type in [17,130]:
            if op.param2 in FarelBot["list"]["bleclist"]:
                if op.param2 not in FarelBot['list']['owner'] and op.param2 not in FarelBot['list']['bot'] and op.param2 not in FarelBot['list']['admin']:
                    try:
                        aa.deleteOtherFromChat(op.param1,[op.param2])
                    except:
                        try:
                            bb.deleteOtherFromChat(op.param1,[op.param2])
                        except:
                            try:
                                cc.deleteOtherFromChat(op.param1,[op.param2])
                            except:
                                try:
                                    dd.deleteOtherFromChat(op.param1,[op.param2])
                                except:
                                    try:
                                        ee.deleteOtherFromChat(op.param1,[op.param2])
                                    except:
                                        try:
                                            ff.deleteOtherFromChat(op.param1,[op.param2])
                                        except:
                                            try:
	                                            gg.deleteOtherFromChat(op.param1,[op.param2])
                                            except:
	                                            try:
		                                            hh.deleteOtherFromChat(op.param1,[op.param2])
	                                            except:
		                                            try:
			                                            ii.deleteOtherFromChat(op.param1,[op.param2])
		                                            except:
			                                            try:
				                                            jj.deleteOtherFromChat(op.param1,[op.param2])
			                                            except:
				                                            try:
					                                            kk.deleteOtherFromChat(op.param1,[op.param2])
				                                            except:
					                                            pass
        if op.type in [32,126]:
            if op.param2 in FarelBot["list"]["bleclist"]:
                if op.param2 not in FarelBot['list']['owner'] and op.param2 not in FarelBot['list']['bot'] and op.param2 not in FarelBot['list']['admin']:
                    try:
                        aa.deleteOtherFromChat(op.param1,[op.param2])
                    except:
                        try:
                            bb.deleteOtherFromChat(op.param1,[op.param2])
                        except:
                            try:
                                cc.deleteOtherFromChat(op.param1,[op.param2])
                            except:
                                try:
                                    dd.deleteOtherFromChat(op.param1,[op.param2])
                                except:
                                    try:
                                        ee.deleteOtherFromChat(op.param1,[op.param2])
                                    except:
                                        try:
                                            ff.deleteOtherFromChat(op.param1,[op.param2])
                                        except:
                                            try:
	                                            gg.deleteOtherFromChat(op.param1,[op.param2])
                                            except:
	                                            try:
		                                            hh.deleteOtherFromChat(op.param1,[op.param2])
	                                            except:
		                                            try:
			                                            ii.deleteOtherFromChat(op.param1,[op.param2])
		                                            except:
			                                            try:
				                                            jj.deleteOtherFromChat(op.param1,[op.param2])
			                                            except:
				                                            try:
					                                            kk.deleteOtherFromChat(op.param1,[op.param2])
				                                            except:pass           
        if op.type in [17,130]:
            if op.param1 in FarelBot['list']['join']:
                if op.param2 not in FarelBot['list']['owner'] and op.param2 not in FarelBot['list']['bot'] and op.param2 not in FarelBot['list']['admin']:
                    FarelBot["list"]["bleclist"][op.param2] = True
                    backup()
                    try:
                        if op.param3 not in FarelBot["list"]["bleclist"]:
                        	aa.kickoutFromGroup(op.param1,[op.param2])
                    except: 
                        try:
                            if op.param3 not in FarelBot["list"]["bleclist"]:
                                bb.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                if op.param3 not in FarelBot["list"]["bleclist"]:
                                    cc.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    if op.param3 not in FarelBot["list"]["bleclist"]:
                                        dd.kickoutFromGroup(op.param1,[op.param2])
                                except: 
                                    try:
                                        if op.param3 not in FarelBot["list"]["bleclist"]:
                                            ee.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            if op.param3 not in FarelBot["list"]["bleclist"]:
                                                ff.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            try:
                                                if op.param3 not in FarelBot["list"]["bleclist"]:
                                                    gg.kickoutFromGroup(op.param1,[op.param2])
                                            except:
                                                try:
                                                    if op.param3 not in FarelBot["list"]["bleclist"]:
                                                        hh.kickoutFromGroup(op.param1,[op.param2])
                                                except:
                                                    try:
                                                        if op.param3 not in FarelBot["list"]["bleclist"]:
                                                            ii.kickoutFromGroup(op.param1,[op.param2])
                                                    except:
                                                        try:
                                                            if op.param3 not in FarelBot["list"]["bleclist"]:
                                                                jj.kickoutFromGroup(op.param1,[op.param2])
                                                        except:
                                                            try:
                                                                if op.param3 not in FarelBot["list"]["bleclist"]:
                                                                    kk.kickoutFromGroup(op.param1,[op.param2])
                                                            except:pass
				                                            
        if op.type in [17,130]:
            if op.param1 in FarelBot['list']['protect']:
                if op.param2 not in FarelBot['list']['owner'] and op.param2 not in FarelBot['list']['bot'] and op.param2 not in FarelBot['list']['admin']:
                    FarelBot["list"]["bleclist"][op.param2] = True
                    backup()
                    try:
                        if op.param3 not in FarelBot["list"]["bleclist"]:
                        	aa.kickoutFromGroup(op.param1,[op.param2])
                    except: 
                        try:
                            if op.param3 not in FarelBot["list"]["bleclist"]:
                                bb.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                if op.param3 not in FarelBot["list"]["bleclist"]:
                                    cc.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    if op.param3 not in FarelBot["list"]["bleclist"]:
                                        dd.kickoutFromGroup(op.param1,[op.param2])
                                except: 
                                    try:
                                        if op.param3 not in FarelBot["list"]["bleclist"]:
                                            ee.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            if op.param3 not in FarelBot["list"]["bleclist"]:
                                                ff.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            try:
                                                if op.param3 not in FarelBot["list"]["bleclist"]:
                                                    gg.kickoutFromGroup(op.param1,[op.param2])
                                            except:
                                                try:
                                                    if op.param3 not in FarelBot["list"]["bleclist"]:
                                                        hh.kickoutFromGroup(op.param1,[op.param2])
                                                except:
                                                    try:
                                                        if op.param3 not in FarelBot["list"]["bleclist"]:
                                                            ii.kickoutFromGroup(op.param1,[op.param2])
                                                    except:
                                                        try:
                                                            if op.param3 not in FarelBot["list"]["bleclist"]:
                                                                jj.kickoutFromGroup(op.param1,[op.param2])
                                                        except:
                                                            try:
                                                                if op.param3 not in FarelBot["list"]["bleclist"]:
                                                                    kk.kickoutFromGroup(op.param1,[op.param2])
                                                            except:pass                   
                return
        if op.type in [19,133]:
            if op.param1 in FarelBot['list']['protect']:
                if op.param2 not in FarelBot['list']['owner'] and op.param2 not in FarelBot['list']['bot'] and op.param2 not in FarelBot['list']['admin']:
                    FarelBot["list"]["bleclist"][op.param2] = True
                    backup()
                    try:
                        inv1 = op.param3.replace('\x1e',',')
                        inv2 = inv1.split(',')
                        for userban in inv2:
                            if userban in FarelBot["list"]["bleclist"]:
                                aa.cancelChatInvitation(op.param1,[userban])
                            aa.deleteOtherFromChat(op.param1,[op.param2])
                    except:
                        try:
	                        inv1 = op.param3.replace('\x1e',',')
	                        inv2 = inv1.split(',')
	                        for userban in inv2:
	                            if userban in FarelBot["list"]["bleclist"]:
	                                bb.cancelChatInvitation(op.param1,[userban])
	                            bb.deleteOtherFromChat(op.param1,[op.param2])
                        except:
                            try:
	                            inv1 = op.param3.replace('\x1e',',')
	                            inv2 = inv1.split(',')
	                            for userban in inv2:
		                            if userban in FarelBot["list"]["bleclist"]:
		                                cc.cancelChatInvitation(op.param1,[userban])
		                            cc.deleteOtherFromChat(op.param1,[op.param2])
                            except:
	                            try:
		                            inv1 = op.param3.replace('\x1e',',')
		                            inv2 = inv1.split(',')
		                            for userban in inv2:
			                            if userban in FarelBot["list"]["bleclist"]:
			                                dd.cancelChatInvitation(op.param1,[userban])
			                            dd.deleteOtherFromChat(op.param1,[op.param2])
	                            except:
		                            try:
			                            inv1 = op.param3.replace('\x1e',',')
			                            inv2 = inv1.split(',')
			                            for userban in inv2:
				                            if userban in FarelBot["list"]["bleclist"]:
				                                ee.cancelChatInvitation(op.param1,[userban])
				                            ee.deleteOtherFromChat(op.param1,[op.param2])
		                            except:
			                            try:
				                            inv1 = op.param3.replace('\x1e',',')
				                            inv2 = inv1.split(',')
				                            for userban in inv2:
					                            if userban in FarelBot["list"]["bleclist"]:
					                                ff.cancelChatInvitation(op.param1,[userban])
					                            ff.deleteOtherFromChat(op.param1,[op.param2])
			                            except:
				                            try:
					                            inv1 = op.param3.replace('\x1e',',')
					                            inv2 = inv1.split(',')
					                            for userban in inv2:
						                            if userban in FarelBot["list"]["bleclist"]:
						                                gg.cancelChatInvitation(op.param1,[userban])
						                            gg.deleteOtherFromChat(op.param1,[op.param2])
				                            except:
					                            try:
						                            inv1 = op.param3.replace('\x1e',',')
						                            inv2 = inv1.split(',')
						                            for userban in inv2:
							                            if userban in FarelBot["list"]["bleclist"]:
							                                hh.cancelChatInvitation(op.param1,[userban])
							                            hh.deleteOtherFromChat(op.param1,[op.param2])
					                            except:
						                            try:
							                            inv1 = op.param3.replace('\x1e',',')
							                            inv2 = inv1.split(',')
							                            for userban in inv2:
								                            if userban in FarelBot["list"]["bleclist"]:
								                                ii.cancelChatInvitation(op.param1,[userban])
								                            ii.deleteOtherFromChat(op.param1,[op.param2])
						                            except:
							                            try:
								                            inv1 = op.param3.replace('\x1e',',')
								                            inv2 = inv1.split(',')
								                            for userban in inv2:
									                            if userban in FarelBot["list"]["bleclist"]:
										                            jj.cancelChatInvitation(op.param1,[userban])
									                            jj.deleteOtherFromChat(op.param1,[op.param2])
							                            except:
								                            try:
									                            inv1 = op.param3.replace('\x1e',',')
									                            inv2 = inv1.split(',')
									                            for userban in inv2:
										                            if userban in FarelBot["list"]["bleclist"]:
											                            kk.cancelChatInvitation(op.param1,[userban])
										                            kk.deleteOtherFromChat(op.param1,[op.param2])
								                            except:pass
        if op.type in [19,133]:
            if op.param3 in FarelBot['list']['bot']:
                if op.param2 not in FarelBot['list']['owner'] and op.param2 not in FarelBot['list']['bot'] and op.param2 not in FarelBot['list']['admin']:
                    FarelBot["list"]["bleclist"][op.param2] = True
                    backup()
                    try:
                        if op.param3 not in FarelBot["list"]["bleclist"]:
                        	aa.kickoutFromGroup(op.param1,[op.param2])
                    except: 
                        try:
                            if op.param3 not in FarelBot["list"]["bleclist"]:
                                bb.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                if op.param3 not in FarelBot["list"]["bleclist"]:
                                    cc.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    if op.param3 not in FarelBot["list"]["bleclist"]:
                                        dd.kickoutFromGroup(op.param1,[op.param2])
                                except: 
                                    try:
                                        if op.param3 not in FarelBot["list"]["bleclist"]:
                                            ee.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            if op.param3 not in FarelBot["list"]["bleclist"]:
                                                ff.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            try:
                                                if op.param3 not in FarelBot["list"]["bleclist"]:
                                                    gg.kickoutFromGroup(op.param1,[op.param2])
                                            except:
                                                try:
                                                    if op.param3 not in FarelBot["list"]["bleclist"]:
                                                        hh.kickoutFromGroup(op.param1,[op.param2])
                                                except:
                                                    try:
                                                        if op.param3 not in FarelBot["list"]["bleclist"]:
                                                            ii.kickoutFromGroup(op.param1,[op.param2])
                                                    except:
                                                        try:
                                                            if op.param3 not in FarelBot["list"]["bleclist"]:
                                                                jj.kickoutFromGroup(op.param1,[op.param2])
                                                        except:
                                                            try:
                                                                if op.param3 not in FarelBot["list"]["bleclist"]:
                                                                    kk.kickoutFromGroup(op.param1,[op.param2])
                                                            except:pass
        if op.type in [19,133]:
            if op.param2 in FarelBot["list"]["bleclist"]:
                if op.param2 not in FarelBot['list']['owner'] and op.param2 not in FarelBot['list']['bot'] and op.param2 not in FarelBot['list']['admin']:
                    try:
                        aa.deleteOtherFromChat(op.param1,[op.param2])
                    except:
                        try:
                            bb.deleteOtherFromChat(op.param1,[op.param2])
                        except:
                            try:
                                cc.deleteOtherFromChat(op.param1,[op.param2])
                            except:
                                try:
                                    dd.deleteOtherFromChat(op.param1,[op.param2])
                                except:
                                    try:
                                        ee.deleteOtherFromChat(op.param1,[op.param2])
                                    except:
                                        try:
                                            ff.deleteOtherFromChat(op.param1,[op.param2])
                                        except:
                                            try:
	                                            gg.deleteOtherFromChat(op.param1,[op.param2])
                                            except:
	                                            try:
		                                            hh.deleteOtherFromChat(op.param1,[op.param2])
	                                            except:
		                                            try:
			                                            ii.deleteOtherFromChat(op.param1,[op.param2])
		                                            except:
			                                            try:
				                                            jj.deleteOtherFromChat(op.param1,[op.param2])
			                                            except:
				                                            try:
					                                            kk.deleteOtherFromChat(op.param1,[op.param2])
				                                            except:pass
#=========================================================
        if op.type in [19,133]:
            try:
                if op.param3 in FarelBot['list']['bot']:
                    if op.param2 not in FarelBot['list']['owner'] and op.param2 not in FarelBot['list']['bot'] and op.param2 not in FarelBot['list']['admin']:
                        FarelBot["list"]["bleclist"][op.param2] = True
                        backup()
                        try:
                            Crot = []
                            for Patek in Bacok:
                                if op.param1 in Patek.getGroupIdsJoined():
                                    Crot.append(Patek)
                            L = random.choice(Crot)
                            XYY = {}
                            chat = cl.getChats([op.param1]).chats[0]
                            for targets in FarelBot['list']['bot']:
                                if targets not in L.getProfile().mid:
                                    if targets not in list(chat.extra.groupExtra.inviteeMids) and targets not in list(chat.extra.groupExtra.memberMids):
                                        if targets not in L.getAllContactIds():
                                            L.findAndAddContactsByMid(targets)
                                            XYY[targets] = True
                                        else:
                                            XYY[targets] = True
                                    else:pass
                                else:pass
                            for target in FarelBot["list"]["bleclist"]:
                                if target in list(cl.getChats([op.param1]).chats[0].extra.groupExtra.memberMids):
                                    L.deleteOtherFromChat(op.param1,[target])
                                else:pass
                            L.inviteIntoChat(op.param1, XYY)
                            L.deleteOtherFromChat(op.param1,[op.param2])
                        except:pass
                if op.param1 in FarelBot['list']['protect']:
                    if op.param2 not in FarelBot['list']['owner'] and op.param2 not in FarelBot['list']['bot'] and op.param2 not in FarelBot['list']['admin']:
                        FarelBot["list"]["bleclist"][op.param2] = True
                        backup()
                        try:
                            if op.param3 not in FarelBot['list']['owner'] and op.param3 not in FarelBot['list']['bot'] and op.param2 not in FarelBot['list']['admin']:
                                Crot = []
                                for Patek in Bacok:
                                    if op.param1 in Patek.getGroupIdsJoined():
                                        Crot.append(Patek)
                                L = random.choice(Crot)
                                chat = cl.getChats([op.param1]).chats[0]
                                for target in FarelBot["list"]["bleclist"]:
                                    if target in list(cl.getChats([op.param1]).chats[0].extra.groupExtra.memberMids):
                                        L.deleteOtherFromChat(op.param1,[target])
                            else:pass
                        except:pass
                if op.param3 in FarelBot['list']['owner']:
                    if op.param2 not in FarelBot['list']['owner'] and op.param2 not in FarelBot['list']['bot'] and op.param2 not in FarelBot['list']['admin']:
                        FarelBot["list"]["bleclist"][op.param2] = True
                        backup()
                        try:
                            Crot = []
                            for Patek in Bacok:
                                if op.param1 in Patek.getGroupIdsJoined():
                                    Crot.append(Patek)
                            L = random.choice(Crot)
                            XYY = {}
                            chat = cl.getChats([op.param1]).chats[0]
                            for targets in FarelBot['list']['owner']:
                                if targets not in L.getProfile().mid:
                                    if targets not in list(chat.extra.groupExtra.inviteeMids) and targets not in list(chat.extra.groupExtra.memberMids):
                                        if targets not in L.getAllContactIds():
                                            L.findAndAddContactsByMid(targets)
                                            XYY[targets] = True
                                        else:
                                            XYY[targets] = True
                                    else:pass
                                else:pass
                            for target in FarelBot["list"]["bleclist"]:
                                if target in list(cl.getChats([op.param1]).chats[0].extra.groupExtra.memberMids):
                                    L.deleteOtherFromChat(op.param1,[target])
                                else:pass
                            L.inviteIntoChat(op.param1, XYY)
                        except:pass
            except:pass
#=========================================================
#=========================================================
#==============================
        if op.type in [25, 26]:
            msg = op.message
            text = str(msg.text)
            msg_id = msg.id
            receiver = msg.to
            msg.from_ = msg._from
            sender = msg._from
            cmd = text.lower()
            if msg.toType == 0 and sender != cl.profile.mid: to = sender
            else: to = receiver
            if msg._from in FarelBot['list']['owner']:
                if cmd == "ping":
                    if to in aa.getGroupIdsJoined():
                        aa.sendMessage(to,'~pong~')
                    else:pass
                    if to in bb.getGroupIdsJoined():
                        bb.sendMessage(to,'~pong~')
                    else:pass
                    if to in cc.getGroupIdsJoined():
                        cc.sendMessage(to,'~pong~')
                    else:pass
                    if to in dd.getGroupIdsJoined():
                        dd.sendMessage(to,'~pong~')
                    else:pass
                    if to in ee.getGroupIdsJoined():
                        ee.sendMessage(to,'~pong~')
                    else:pass
                    if to in ff.getGroupIdsJoined():
                        ff.sendMessage(to,'~pong~')
                    else:pass
                    if to in gg.getGroupIdsJoined():
                        gg.sendMessage(to,'~pong~')
                    else:pass
                    if to in hh.getGroupIdsJoined():
                        hh.sendMessage(to,'~pong~')
                    else:pass
                    if to in ii.getGroupIdsJoined():
                        ii.sendMessage(to,'~pong~')
                    else:pass
                    if to in ii.getGroupIdsJoined():
                        jj.sendMessage(to,'~pong~')
                    else:pass
                    if to in ii.getGroupIdsJoined():
                        kk.sendMessage(to,'~pong~')
                    else:pass

                if cmd == "help":
                  if msg._from in FarelBot['list']['owner']:
                    cl.sendMessage(to,helpM)

                if cmd == "sp" or cmd == 'speed':
                  if msg._from in FarelBot['list']['owner']:
                    start = time.time()
                    cl.getProfile()
                    total = time.time()-start
                    cl.sendMessage(to,str(total))
                    aa.sendMessage(to,str(total))
                    bb.sendMessage(to,str(total))
                    cc.sendMessage(to,str(total))
                    dd.sendMessage(to,str(total))
                    ee.sendMessage(to,str(total))
                    ff.sendMessage(to,str(total))
                    gg.sendMessage(to,str(total))
                    hh.sendMessage(to,str(total))
                    ii.sendMessage(to,str(total))
                    jj.sendMessage(to,str(total))
                    kk.sendMessage(to,str(total))

                if cmd == "listowner":
                    if msg._from in FarelBot['list']["owner"]:
                        mb = ""
                        b = 0
                        for m_id in FarelBot['list']["owner"]:
                            b = b + 1
                            end = '\n'
                            mb += str(b) + ". " +cl.getContact(m_id).displayName + "\n"
                        cl.sendMessage(msg.to,"\n| ⚜️ ʟɪꜱᴛ owner ⚜️\n\n"+mb+"\n|:「%s」⚜️ All owner ⚜️ \n" %(str(len(FarelBot['list']["owner"]))))                        

                if cmd == "Ownerdell" or cmd == 'Clearowner':
                  if msg._from in FarelBot['list']['owner']:
                      FarelBot['list']["owner"] = []
                      ang = cl.getContacts(FarelBot['list']["owner"])
                      mc = "%i Owner ☑️ " % len(ang)
                      cl.sendMessage(msg.to,"Done clear " +mc)
                      backup()
                       
                if cmd == "/groups":
                  if msg._from in FarelBot['list']['owner']:
                       ma = ""
                       a = 0
                       gid = cl.getGroupIdsJoined()
                       for i in gid:
                           G = cl.getGroup(i)
                           a = a + 1
                           end = "\n"
                           ma += "╠ " + str(a) + ". " +G.name+ "\n"
                       cl.sendMessage(msg.to,"╔══[ ⚜️ GROUP LIST ⚜️]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Groups ]")
 
                if cmd.startswith("bot "):
                    if msg._from in FarelBot['list']['owner']:
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"][0]["M"]
                       targets = []
                       for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                       for target in targets:
                               try:
                                   FarelBot['list']["bot"][target] = {}
                                   cl.sendMessage(msg.to,"Succes add bot☑️")
                                   backup()
                               except:pass
 
                if cmd.startswith("admin "):
                    if msg._from in FarelBot['list']['owner']:
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"][0]["M"]
                       targets = []
                       for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                       for target in targets:
                               try:
                                   FarelBot['list']["admin"][target] = {}
                                   cl.sendMessage(msg.to,"Succes add admin☑️")
                                   backup()
                               except:pass
                     
                if cmd == "adel" or cmd == 'adell':
                  if msg._from in FarelBot['list']['owner']:
                      FarelBot['list']['admin'] = {}
                      ang = cl.getContacts(FarelBot['list']['admin'])
                      mc = "「%i」admin☑️ " % len(ang)
                      cl.sendMessage(msg.to," ⚜️Done admin remove " +mc)
                      backup()
                     
                if cmd == "bdell" or cmd == 'bdel':
                  if msg._from in FarelBot['list']['owner']:
                      FarelBot['list']['bot'] = {}
                      ang = cl.getContacts(FarelBot['list']['bot'])
                      mc = "「%i」bots☑️ " % len(ang)
                      cl.sendMessage(msg.to," ⚜️Done  remove bots☑️ " +mc)
                      backup()
                        
                if cmd == "adminlist" or cmd == 'listadmin':
                    if msg._from in FarelBot['list']['owner']:
                        ma = ""
                        a = 0
                        for m_id in FarelBot['list']["admin"]:
                            a = a + 1
                            end = '\n'
                            ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                        cl.sendMessage(msg.to,"⚜️list Admin⚜️\n\n"+ma+"\n⚜️ all admin⚜️「%s]\n" %(str(len(FarelBot['list']["admin"]))))
                        
                if cmd == "botlist" or cmd == 'listbot':
                    if msg._from in FarelBot['list']['owner']:
                        ma = ""
                        a = 0
                        for m_id in FarelBot['list']['bot']:
                            a = a + 1
                            end = '\n'
                            ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                        cl.sendMessage(msg.to,"⚜️list bots⚜️\n\n"+ma+"\n⚜️ all bots⚜️「%s]\n" %(str(len(FarelBot['list']["bot"]))))

                if cmd == "/clearban" or cmd == '/cban':
                  if msg._from in FarelBot['list']['owner']:        
                      ragets = cl.getContacts(FarelBot['list']["bleclist"])
                      mc = "「%i」bleclist ☑️" % len(ragets)
                      FarelBot['list']["bleclist"] = {}
                      cl.sendMessage(msg.to,"⚜️Clear " +mc)
                      backup()

                if cmd == "/bl" or cmd == '/blc':
                  if msg._from in FarelBot['list']['owner']:
                      if FarelBot['list']["bleclist"] == {}:
                        cl.sendMessage(to,"⚜️No Bleclist🖐")
                      else:
                          mc = "[ bleclist ]"
                          for mi_d in FarelBot['list']["bleclist"]:
                              mc += "\n "+cl.getContact(mi_d).displayName
                          cl.sendMessage(msg.to,mc + " ")

                if cmd == "onpro":
                    if to not in FarelBot['list']['protect']:
                        FarelBot['list']['protect'].append(to)
                        cl.sendMessage(to,"⚜️ 𝑷𝒓𝒐 𝒎𝒐𝒅𝒆 𝒐𝒏 ☑️")
                        backup()
                    else:
                        cl.sendMessage(to,"⚜️ 𝑮𝒓𝒐𝒖𝒑 𝑷𝒓𝒐 𝒎𝒐𝒅𝒆 𝒐𝒏 ☑️")

                if cmd == "offpro":
                    if to not in FarelBot['list']['protect']:
                        cl.sendMessage(to,"⚜️ 𝑮𝒓𝒐𝒖𝒑 𝒎𝒐𝒅𝒆 𝒐𝒇𝒇 ☑️")
                    else:
                        FarelBot['list']['protect'].remove(to)
                        cl.sendMessage(to,"⚜️ 𝑮𝒓𝒐𝒖𝒑 𝑷𝒓𝒐 𝒎𝒐𝒅𝒆 𝒐𝒇𝒇 ☑️")
                        backup()

                if cmd == "onjoin":
                    if to not in FarelBot['list']['join']:
                        FarelBot['list']['join'].append(to)
                        cl.sendMessage(to,"⚜️ 𝑷𝒓𝒐𝒋𝒐𝒊𝒏 𝒐𝒏 ☑️")
                        backup()
                    else:
                        cl.sendMessage(to,"⚜️ 𝑷𝒓𝒐𝒋𝒐𝒊𝒏 𝒎𝒐𝒅𝒆 𝒐𝒏 ☑️")
                        
                if cmd == "offjoin":
                    if to not in FarelBot['list']['join']:
                        cl.sendMessage(to,"⚜️ 𝑷𝒓𝒐𝒋𝒐𝒊𝒏 𝒐𝒇𝒇 ☑️")
                    else:
                        FarelBot['list']['join'].remove(to)
                        cl.sendMessage(to,"⚜️ 𝑷𝒓𝒐𝒋𝒐𝒊𝒏 𝒎𝒐𝒅𝒆 𝒐𝒇𝒇 ☑️")

                if cmd == "/reset":
                  if settings["selfbot"] == True:
                    if msg._from in FarelBot['list']['owner']:
                       cl.sendMessage(msg.to, "⚜️Waittings 10 Seccond ....\n And You Klik Type [ Rs ]...")
                       settings["restartPoint"] = msg.to
                       restartBot()
                       cl.sendMessage(msg.to, "⚜️Done Restart...")                            

                if cmd == "rchat":
                    if msg._from in FarelBot['list']['owner']:
                       try:
                           cl.removeAllMessages(op.param2)                                  
                           cl.sendMessage(msg.to,"👉Clear Done ☑️")
                           aa.removeAllMessages(op.param2)                                  
                           aa.sendMessage(msg.to,"👉Clear Done ☑️")
                           bb.removeAllMessages(op.param2)                                  
                           bb.sendMessage(msg.to,"👉Clear Done ☑️")
                           cc.removeAllMessages(op.param2)                                  
                           cc.sendMessage(msg.to,"👉Clear Done ☑️")
                           dd.removeAllMessages(op.param2)                                  
                           dd.sendMessage(msg.to,"👉Clear Done ☑️")
                           ee.removeAllMessages(op.param2)                                  
                           ee.sendMessage(msg.to,"👉Clear Done ☑️")
                           ff.removeAllMessages(op.param2)                                  
                           ff.sendMessage(msg.to,"👉Clear Done ☑️")
                           gg.removeAllMessages(op.param2)                                  
                           gg.sendMessage(msg.to,"👉Clear Done ☑️")
                           hh.removeAllMessages(op.param2)                                  
                           hh.sendMessage(msg.to,"👉Clear Done ☑️")
                           ii.removeAllMessages(op.param2)                                  
                           ii.sendMessage(msg.to,"👉Clear Done ☑️")
                           jj.removeAllMessages(op.param2)                                  
                           jj.sendMessage(msg.to,"👉Clear Done ☑️")
                           kk.removeAllMessages(op.param2)                                  
                           kk.sendMessage(msg.to,"👉Clear Done ☑️")
                       except:pass
                if cmd == "mypic":
                    if msg._from in FarelBot['list']['owner']:
                        settings["Picture"] = True
                        cl.sendMessage(msg.to,"share pict")
                if cmd == "allpic":
                    if msg._from in FarelBot['list']['owner']:
                        settings["cPicture"] = True
                        cl.sendMessage(msg.to,"share pict")
                if cmd.startswith(".myname: "):
                  if msg._from in FarelBot['list']['owner']:
                    separate = msg.text.split(" ")
                    string = msg.text.replace(separate[0] + " ","")
                    if len(string) <= 10000000000:
                        profile = cl.getProfile()
                        profile.displayName = string
                        cl.updateProfile(profile)
                        cl.sendMessage(msg.to,"name changed to " + string + "")
                if cmd.startswith("botn1: "):
                  if msg._from in FarelBot['list']['owner']:
                    separate = msg.text.split(" ")
                    string = msg.text.replace(separate[0] + " ","")
                    if len(string) <= 10000000000:
                        profile = aa.getProfile()
                        profile.displayName = string
                        aa.updateProfile(profile)
                        aa.sendMessage(msg.to,"name changed to " + string + "")
                if cmd.startswith("botn2: "):
                  if msg._from in FarelBot['list']['owner']:
                    separate = msg.text.split(" ")
                    string = msg.text.replace(separate[0] + " ","")
                    if len(string) <= 10000000000:
                        profile = bb.getProfile()
                        profile.displayName = string
                        bb.updateProfile(profile)
                        bb.sendMessage(msg.to,"name changed to " + string + "")
                if cmd.startswith("botn3: "):
                  if msg._from in FarelBot['list']['owner']:
                    separate = msg.text.split(" ")
                    string = msg.text.replace(separate[0] + " ","")
                    if len(string) <= 10000000000:
                        profile = cc.getProfile()
                        profile.displayName = string
                        cc.updateProfile(profile)
                        cc.sendMessage(msg.to,"name changed to " + string + "")
                if cmd.startswith("botn4: "):
                  if msg._from in FarelBot['list']['owner']:
                    separate = msg.text.split(" ")
                    string = msg.text.replace(separate[0] + " ","")
                    if len(string) <= 10000000000:
                        profile = dd.getProfile()
                        profile.displayName = string
                        dd.updateProfile(profile)
                        dd.sendMessage(msg.to,"name changed to " + string + "")
                if cmd.startswith("botn5: "):
                  if msg._from in FarelBot['list']['owner']:
                    separate = msg.text.split(" ")
                    string = msg.text.replace(separate[0] + " ","")
                    if len(string) <= 10000000000:
                        profile = ee.getProfile()
                        profile.displayName = string
                        ee.updateProfile(profile)
                        ee.sendMessage(msg.to,"name changed to " + string + "")
                if cmd.startswith("botn6: "):
                  if msg._from in FarelBot['list']['owner']:
                    separate = msg.text.split(" ")
                    string = msg.text.replace(separate[0] + " ","")
                    if len(string) <= 10000000000:
                        profile = ff.getProfile()
                        profile.displayName = string
                        ff.updateProfile(profile)
                        ff.sendMessage(msg.to,"name changed to " + string + "")
                if cmd.startswith("botn7: "):
                  if msg._from in FarelBot['list']['owner']:
                    separate = msg.text.split(" ")
                    string = msg.text.replace(separate[0] + " ","")
                    if len(string) <= 10000000000:
                        profile = gg.getProfile()
                        profile.displayName = string
                        gg.updateProfile(profile)
                        gg.sendMessage(msg.to,"name changed to " + string + "")
                if cmd.startswith("botn8: "):
                  if msg._from in FarelBot['list']['owner']:
                    separate = msg.text.split(" ")
                    string = msg.text.replace(separate[0] + " ","")
                    if len(string) <= 10000000000:
                        profile = hh.getProfile()
                        profile.displayName = string
                        hh.updateProfile(profile)
                        hh.sendMessage(msg.to,"name changed to " + string + "")
                if cmd.startswith("botn9: "):
                  if msg._from in FarelBot['list']['owner']:
                    separate = msg.text.split(" ")
                    string = msg.text.replace(separate[0] + " ","")
                    if len(string) <= 10000000000:
                        profile = ii.getProfile()
                        profile.displayName = string
                        ii.updateProfile(profile)
                        ii.sendMessage(msg.to,"name changed to " + string + "")
                if cmd.startswith("botn10: "):
                  if msg._from in FarelBot['list']['owner']:
                    separate = msg.text.split(" ")
                    string = msg.text.replace(separate[0] + " ","")
                    if len(string) <= 10000000000:
                        profile = jj.getProfile()
                        profile.displayName = string
                        jj.updateProfile(profile)
                        jj.sendMessage(msg.to,"name changed to " + string + "")
                if cmd.startswith("botn11: "):
                  if msg._from in FarelBot['list']['owner']:
                    separate = msg.text.split(" ")
                    string = msg.text.replace(separate[0] + " ","")
                    if len(string) <= 10000000000:
                        profile = kk.getProfile()
                        profile.displayName = string
                        kk.updateProfile(profile)
                        kk.sendMessage(msg.to,"name changed to " + string + "")          
                if cmd.startswith("allname: "):
                 if msg._from in FarelBot['list']['owner']:
                   separate = msg.text.split(" ")
                   string = msg.text.replace(separate[0] + " ","")
                   if len(string) <= 10000000000:
                      profile = cl.getProfile()
                      profile.displayName = string
                      cl.updateProfile(profile)
                      cl.sendMessage(msg.to,"name changed to " + string + "")
                      profile = aa.getProfile()
                      profile.displayName = string
                      aa.updateProfile(profile)
                      aa.sendMessage(msg.to,"name changed to " + string + "")
                      profile = bb.getProfile()
                      profile.displayName = string
                      bb.updateProfile(profile)
                      bb.sendMessage(msg.to,"name changed to " + string + "")
                      profile = cc.getProfile()
                      profile.displayName = string
                      cc.updateProfile(profile)
                      cc.sendMessage(msg.to,"name changed to " + string + "")
                      profile = dd.getProfile()
                      profile.displayName = string
                      dd.updateProfile(profile)
                      dd.sendMessage(msg.to,"name changed to " + string + "")
                      profile = ee.getProfile()
                      profile.displayName = string
                      ee.updateProfile(profile)
                      ee.sendMessage(msg.to,"name changed to " + string + "")
                      profile = ff.getProfile()
                      profile.displayName = string
                      ff.updateProfile(profile)
                      ff.sendMessage(msg.to,"name changed to " + string + "")
                      profile = gg.getProfile()
                      profile.displayName = string
                      gg.updateProfile(profile)
                      gg.sendMessage(msg.to,"name changed to " + string + "")
                      profile = hh.getProfile()
                      profile.displayName = string
                      hh.updateProfile(profile)
                      hh.sendMessage(msg.to,"name changed to " + string + "")
                      profile = ii.getProfile()
                      profile.displayName = string
                      ii.updateProfile(profile)
                      ii.sendMessage(msg.to,"name changed to " + string + "")
                      profile = jj.getProfile()
                      profile.displayName = string
                      jj.updateProfile(profile)
                      jj.sendMessage(msg.to,"name changed to " + string + "")
                      profile = kk.getProfile()
                      profile.displayName = string
                      kk.updateProfile(profile)
                      kk.sendMessage(msg.to,"name changed to " + string + "")
                if msg.contentType == 1:
                 if msg._from in FarelBot['list']['owner']:
                   if settings["Picture"] == True:
                     path1 = cl.downloadObjectMsg(msg_id)
                     settings["Picture"] = False
                     cl.updateProfilePicture(path1)
                     cl.sendMessage(msg.to, "Succes")
                if msg.contentType == 1:
                 if msg._from in FarelBot['list']['owner']:
                   if settings["cPicture"] == True:
                     path1 = cl.downloadObjectMsg(msg_id)
                     path2 = aa.downloadObjectMsg(msg_id)
                     path3 = bb.downloadObjectMsg(msg_id)
                     path4 = cc.downloadObjectMsg(msg_id)
                     path5 = dd.downloadObjectMsg(msg_id)
                     path6 = ee.downloadObjectMsg(msg_id)
                     path7 = ff.downloadObjectMsg(msg_id)
                     path8 = gg.downloadObjectMsg(msg_id)
                     path9 = hh.downloadObjectMsg(msg_id)
                     path10 = ii.downloadObjectMsg(msg_id)
                     path11 = jj.downloadObjectMsg(msg_id)
                     path12 = kk.downloadObjectMsg(msg_id)   
                     settings["cPicture"] = False
                     cl.updateProfilePicture(path1)
                     cl.sendMessage(msg.to, "Succes")
                     aa.updateProfilePicture(path2)
                     aa.sendMessage(msg.to, "Succes")
                     bb.updateProfilePicture(path3)
                     bb.sendMessage(msg.to, "Succes")
                     cc.updateProfilePicture(path4)
                     cc.sendMessage(msg.to, "Succes")
                     dd.updateProfilePicture(path5)
                     dd.sendMessage(msg.to, "Succes")
                     ee.updateProfilePicture(path6)
                     ee.sendMessage(msg.to, "Succes")
                     ff.updateProfilePicture(path7)
                     ff.sendMessage(msg.to, "Succes")
                     gg.updateProfilePicture(path8)
                     gg.sendMessage(msg.to, "Succes")
                     hh.updateProfilePicture(path9)
                     hh.sendMessage(msg.to, "Succes")
                     ii.updateProfilePicture(path10)
                     ii.sendMessage(msg.to, "Succes")                     
                     jj.updateProfilePicture(path10)
                     jj.sendMessage(msg.to, "Succes")                     
                     kk.updateProfilePicture(path10)
                     kk.sendMessage(msg.to, "Succes")

                if cmd == '.cek':
                  if msg._from in FarelBot['list']['owner']:
                    Aku = [cl,aa,bb,cc,dd,ee,ff,gg,hh,ii,jj,kk]
                    for Farel in Aku:
                      if Farel.getProfile().mid:
                          if msg.to in Farel.getGroupIdsJoined():
                              try:Farel.kickoutFromChat(to,['uacbca7e1b2e4ada531969459d5652f40']);has1 ='OK'
                              except:has1 = 'NOT'
                              if has1 == 'OK':sil1 = '🔰 𝒏𝒐𝒓𝒎𝒂𝒍 ☑️'
                              else:sil1 = '📛 𝒍𝒊𝒎𝒊𝒕 ❌'
                              try:Farel.inviteIntoChat(to,[Farel.getProfile().mid]);has2 = 'OK'
                              except:has2 = 'NOT'
                              if has2 == 'OK':sil2 = '🔰 𝒏𝒐𝒓𝒎𝒂𝒍 ☑️'
                              else:sil2 = '📛 𝒍𝒊𝒎𝒊𝒕 ❌'
                              Farel.sendMessage(to, '{}'.format(sil2))

                if cmd == "listpro":
                    ma = ""
                    mb = ""
                    a = 0
                    b = 0
                    gid = FarelBot["list"]["protect"]
                    for group in gid:
                        a = a + 1
                        end = '\n║'
                        ma += str(a) + ". " +cl.getChats([group]).chats[0].chatName + "\n║"
                    gid = FarelBot["list"]["join"]
                    for group in gid:
                        b = b + 1
                        end = '\n║'
                        mb += str(b) + ". " +cl.getChats([group]).chats[0].chatName + "\n║"
                    cl.sendMessage(to,"╔═╬LIST PROTECT ╬═╗\n║\n║PRO ALL :\n║"+ma+"\n║PRO JOIN :\n║"+mb+"\n╚╬ Total [%s] aktif ╬╝" %(str(len(FarelBot["list"]["protect"])+len(FarelBot["list"]["join"]))))

                if cmd.startswith("sepak "):
                    try:
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        targets = []
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        for target in targets:
                            FarelBot["list"]["bleclist"][target] = True
                            Crot = []
                            for Patek in Bacok:
                                if to in Patek.getGroupIdsJoined():
                                    Crot.append(Patek)
                            L = random.choice(Crot)
                            L.deleteOtherFromChat(to,[target])
                    except:pass

                if cmd == "/by":
                  if msg._from in FarelBot['list']['owner']:
                    G = cl.getGroup(msg.to)
                    cl.leaveGroup(msg.to)

                if cmd == "/out":
                  if msg._from in FarelBot['list']['owner']:
                    G = cl.getGroup(msg.to)
                    aa.leaveGroup(msg.to)
                    bb.leaveGroup(msg.to)
                    cc.leaveGroup(msg.to)
                    dd.leaveGroup(msg.to)
                    ee.leaveGroup(msg.to)
                    ff.leaveGroup(msg.to)
                    gg.leaveGroup(msg.to)
                    hh.leaveGroup(msg.to)
                    ii.leaveGroup(msg.to)
                    jj.leaveGroup(msg.to)
                    kk.leaveGroup(msg.to)

                if cmd.startswith(".allkick"):
                  if msg._from in FarelBot['list']['owner']:
                      if msg.toType == 2:
                          chat = cl.getGroup(msg.to)
                          nama = [contact.mid for contact in chat.members]
                          for x in nama:
                              if x not in FarelBot['list']['owner']:
                                  if x not in FarelBot['list']['admin']:
                                      if x not in FarelBot['list']['bot']:
                                          try:
                                              kick=[aa,bb,cc,dd,ee,ff,gg,hh,ii,jj,kk]
                                              Farels=random.choice(kick)
                                              Farels.deleteOtherFromChat(msg.to,[x])
                                          except:
                                              print ("👉limit boss ☑️")

                if cmd == "/in":
                    try:
                        L = cl
                        XYY = {}
                        chat = cl.getChats([to]).chats[0]
                        for targets in FarelBot['list']['bot']:
                            if targets not in L.getProfile().mid:
                                if targets not in list(chat.extra.groupExtra.inviteeMids) and targets not in list(chat.extra.groupExtra.memberMids):
                                    if targets not in L.getAllContactIds():
                                        L.findAndAddContactsByMid(targets)
                                        XYY[targets] = True
                                    else:
                                        XYY[targets] = True
                                else:pass
                            else:pass
                        L.inviteIntoChat(to, XYY)
                        KKami = [aa,bb,cc,dd,ee,ff,gg,hh,ii,jj,kk]
                        for kawankuu in KKami:
                            try:
                                if to not in kawankuu.getGroupIdsJoined():
                                    kawankuu.acceptChatInvitation(to)
                                else:pass
                            except:pass
                    except:pass

    except Exception as catch:
        trace = catch.__traceback__
        print("Error Name: "+str(trace.tb_frame.f_code.co_name)+"\nError Filename: "+str(trace.tb_frame.f_code.co_filename)+"\nError Line: "+str(trace.tb_lineno)+"\nError: "+str(catch))

with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
    while True:
        try:
            ops = cl.fetchOps()
            for op in ops:
                if op.revision == -1 and op.param2 != None:
                    cl.globalRev = int(op.param2.split("\x1e")[0])
                if op.revision == -1 and op.param1 != None:
                    cl.individualRev = int(op.param1.split("\x1e")[0])
                cl.localRev = max(op.revision, cl.localRev)
                executor.submit(worker,op)
        except:
            pass