import os

#Python OS module is used for OS related operations

os.mkdir("C:\\Users\\Ashish\\Desktop\\SkillUpgrade\\pythonOSdirectory") # Create Directory
os.rmdir("C:\\Users\\Ashish\\Desktop\\SkillUpgrade\\pythonOSdirectory") # Remove Directory

os.listdir("C:\\Users\\Ashish\\Desktop")

os.walk("C:\\Users\\Ashish\\Desktop\\SkillUpgrade")

for (root,dirs,files) in os.walk('C:\\Users\\Ashish\\Desktop\\SkillUpgrade'): 
        print(root) 
        print(dirs) 
        print(files) 
        print('--------------------------------')
        break
