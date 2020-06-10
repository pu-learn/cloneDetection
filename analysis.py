#-*- coding:UTF-8 -*-
import os
import sys
def normalize(name,target):
	file=open(name,'r')
	linelist=file.readline().split()
	#line=linelist[0]
	line=' '.join(linelist)
	flag=False
	while line:
		newf=open(target,'a+')
		if line!="{" and line!="}":
			if flag==False:
				flag=True
			else:
				newf.write("\n")
		newf.write(line)
		newf.close()
		linelist=file.readline().split()
		if linelist:
			line=' '.join(linelist)
		else:
			line=''
	file.close()
def get_file(dir,target,mod):
		newDir = dir
		newtarget=target
		if os.path.isfile(dir):
			st=newDir.rfind('\\')
			name=newDir[st+1:]
			newtarget+=newDir[st:]
			print(newDir,newtarget)
			if mod==1:
				os.system("path_of_lex.yy.exe "+newDir+" "+newtarget)
			else:
				normalize(newDir,newtarget)
		elif os.path.isdir(dir):
			for s in os.listdir(dir):
				newDir=os.path.join(dir,s)
				get_file(newDir,newtarget,mod)
get_file(sys.argv[1],"path_of_step1",1)
get_file("path_of_step1","path_of_analysis",2)
