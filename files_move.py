import os
import shutil

#找到 桌面->华科科协文件->稿件 
rootdir = r"C:\Users\admin\Desktop\华科科协文件移动\稿件"

#获取目录下的文件名清单
files = os.listdir(rootdir)

#将清单输出在屏幕上，供我们检查上一步是否成功获取
print(files)

#遍历'稿件'目录下的所有文件夹
for _ in range(len(files)):

    #找到次级目录,例如 桌面->华科科协文件->稿件->1 杨梅
    #并获取目录下的文件名清单
    files_lower = os.listdir(rootdir + "\\" + files[_])

    #遍历次级目录下的所有文件夹
    for i in range(len(files_lower)):

        #找到次级目录的下一级目录，例如 桌面->华科科协文件->稿件->1 杨梅->第65期
        #并获取目录下的文件名清单
        files_final = os.listdir(rootdir + "\\" + files[_] +"\\"+ files_lower[i])

        #将列表输出在屏幕上，供我们查看所有文档名
        print(files_final)

        #遍历上述列表
        for name in files_final:
            if "翻译" in name or "转" in name:
                #每个转译原本的完整路径
                full_path = os.path.join("C:/Users/admin/Desktop/华科科协文件移动/稿件/"+ files[_]+"/"+ files_lower[i]+ "/"+name)
                #目标路径
                des_path = "C:/Users/admin/Desktop/华科科协文件移动/转译原本"
                #移动文件到目标路径
                shutil.move(full_path,des_path)

