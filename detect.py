#!/usr/bin/python3
#-*- coding:UTF-8 -*-
from scipy.special import perm, comb
from itertools import permutations, combinations
import itertools
import sys
import csv
import os
class Detection:
	def detect(self,F,q,e,theta,filelist):
		candMap={}
		hashSet=[]
		hashSubset=[]
		fid=1
		for f in F:
			L=len(f)
			numWin=L-q+1
			k=0
			for i in range(numWin):
				T=f[i]
				newf=f[i:i+q]
				for j in combinations(newf,q-e):
					k=hash(j)
					v=fid
					hashSubset.append((k,i))
					temp=[]
					if k in candMap:
						temp=candMap[k]
					if v not in temp:
						temp.append(v)
					candMap[k]=temp
			fid+=1
			hashSet.append(hashSubset)
			hashSubset=[]
		candPair=[]
		clonePair=[]
		for map in candMap:
			if len(candMap[map])>=2:
				for p in combinations(candMap[map],2):
					if p not in candPair:
						candPair.append(p)
		for pair in candPair:
			listA=pair[0]-1
			listB=pair[1]-1
			ret = self.setIntersection(hashSet[listA],hashSet[listB])
			start1=[]
			start2=[]
			numMatch1,start1 = self.findGrams(hashSet[listA],ret)
			numMatch2,start2 = self.findGrams(hashSet[listB],ret)
			if numMatch1>=(theta*(len(F[listA])-q+1)) or numMatch2>=(theta*(len(F[listB])-q+1)):
				DirA,nameA=filelist[listA][0],filelist[listA][1]
				DirB,nameB=filelist[listB][0],filelist[listB][1]
				for i in range(len(ret)):
					temp=[]
					if len(start1[i])>1 or len(start2[i])>1:
						for item in list(itertools.product(start1[i],start2[i])):
							temp=[DirA,nameA,item[0],item[0]+q-1,DirB,nameB,item[1],item[1]+q-1]
							clonePair.append(temp)
					else:
						temp=[DirA,nameA,start1[i][0],start1[i][0]+q-1,DirB,nameB,start2[i][0],start2[i][0]+q-1]
						clonePair.append(temp)
		with open("path_of_csv","w") as csvfile:
			writer = csv.writer(csvfile)
			for pair in clonePair:
				writer.writerow(pair)
	def findGrams(self,hashSet,grams):
		win=[]
		count=0
		for g in grams:
			temp=[value[1] for (index,value) in enumerate(hashSet) if value[0] == g]#找出g在hashset中出现的所有位置对应窗口开始行
			count+=len(temp)
			win.append(temp)
		return count,win
	def setIntersection(self,l1,l2):
		hash1=list(set([i[0] for i in l1]))
		hash2=list(set([i[0] for i in l2]))
		ret=[i for i in hash1 if i in hash2]
		return ret
	def get_file(self,dir,filelist,Fd):
		newDir = dir
		if os.path.isfile(dir):
			st=newDir.rfind('\\')
			name=newDir[st+1:]
			newDir=newDir[:st]
			filelist.append((newDir,name))
			file=open(dir,'r')
			text=file.readlines()
			temp=[]
			for t in text:
				t=str(t)
				temp.append(t)
			Fd.append(temp)
		elif os.path.isdir(dir):
			for s in os.listdir(dir):
				newDir=os.path.join(dir,s)
				self.get_file(newDir,filelist,Fd)
		return filelist,Fd
det = Detection()
q=int(sys.argv[2])
e=int(sys.argv[3])
theta=float(sys.argv[4])
filelist=[]
Fd=[]
filelist,Fd=det.get_file(sys.argv[1],filelist,Fd)
det.detect(Fd,q,e,theta,filelist)
