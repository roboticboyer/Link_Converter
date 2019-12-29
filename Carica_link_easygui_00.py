#!/usr/bin/python3

import sys
#from os import path
import os.path
#import os
import easygui as eg 
avvio=0 

def creahtml():
	global avvio
	global directory
	if avvio==0 :
		#Apre file txt
		path = eg.fileopenbox(msg='Please locate link file',
                    title='Link File', default='*.txt',
                    filetypes='*.txt')
		#print(path)
		directory=os.path.dirname(str(path))
		#print(directory)
		avvio=1
	else:
		default_dir=directory+"/*.txt"
		path = eg.fileopenbox(msg='Please locate link file',
                    title='Link File', default=default_dir,
                    filetypes='*.txt')
		#print(path)
		directory=os.path.dirname(str(path))

	path_no_ext=path[:-3]
	path_htm=path_no_ext+"htm"
	# Apre file htm
	fow = open(path_htm, "w")
	fow.write("<HTML>\n<HEAD><TITLE>ELENCO SITI</TITLE></HEAD>\n<BODY>\n")
	fow.write("<H1 ALIGN=CENTER><P><B>Elenco siti</B></H1><H3 ALIGN=LEFT><P>\n")
	
	with open(path) as fin:
		for line in fin:
			http_find=line.find('http')
			google_find=line.find('google')
			uguale_find=line.find('=')
			num_caratteri=len(line)
			if http_find == 0 :
				fow.write("<A target=\"_blank\" HREF=\"")
				fow.write(line)
				fow.write("\">")
				if google_find > 0 :
					fow.write("Google link")
				elif num_caratteri > 100 :
					fow.write(line[:90] + " --- link")
				else :
					#window.ui.T_log.appendPlainText("Trovato link " + line)
					fow.write(line)
				fow.write("</A><P>\n")
			elif uguale_find == 0:
				fow.write("<hr>")
			else :
				fow.write(line)
				fow.write("<P>\n")
		
	# Close opend files
	#filetxt.close()
	fow.write("</BODY>\n</HTML>\n")
	fow.close()
	eg.msgbox('File Convertito', 'Carica Link')


if __name__ == '__main__':
	ok=1
	while(ok==1):
		creahtml()
		msg = "Premi Continue per convertire un altro file..."
		title = "Carica Link"
		if eg.ccbox(msg, title):     # show a Continue/Cancel dialog
			ok=1
		else:  # user chose Cancel
			sys.exit(0)
