import os
import shutil
cur_dir = os.path.dirname(__file__) #to git the path of this file
print (cur_dir)
for fname in os.listdir(cur_dir):   #to git all files  in this directory
  
    if fname.endswith('.png','.jpg'):
        if os.path.exists("images"):os.mkdir("images")
        shutil.copy(fname, "images")
        os.remove(fname)
        print ("done")
        
    if fname.endswith('.html','.py','.cpp','.java','js','.css','.c'):
        if os.path.exists("codes"):os.mkdir("codes")
        shutil.copy(fname, "codes")
        os.remove(fname)
        print ("done")
        
    if fname.endswith('.MP3','.MP4','.WMV'):
        if os.path.exists("music"):os.mkdir("music")
        shutil.copy(fname, "music")
        os.remove(fname)
        print ("done")
        
            
    
