import os
import shutil

def copy_result(src,dst):
    for timestep in os.listdir(src):
        shutil.copy(os.path.join(src,timestep,timestep+'.txt'),os.path.join(dst,timestep+'.txt'))
        
        
        
copy_result('runs/detect','submission/0529')