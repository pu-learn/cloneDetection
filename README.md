# cloneDetection
分为两个部分：
 1、词法分析
 2、克隆检测
词法分析部分由analysis.py执行，在使用之前需要修改analysis.py中"path_of_lex.yy.exe "、"path_of_step1"、"path_of_analysis"；
path_of_lex.yy.exe——lex.yy.exe所在目录，path_of_step1——词法分析后存储文件的目录，path_of_analysis——标准化后存储文件的目录；
使用命令python analysis.py "需要进行词法分析的目录"执行；
克隆检测部分由detect.py执行，使用命令python detect.py "词法分析后文件的存储目录" q e theta
q，e，theta为用户设置的参数，q为窗口大小，e为编辑距离，theta为阙值。
