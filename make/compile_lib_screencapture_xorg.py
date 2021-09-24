# -*- coding: utf-8 -*-
'''
This Source Code Form is subject to the terms of the Mozilla
Public License, v. 2.0. If a copy of the MPL was not distributed
with this file, You can obtain one at http://mozilla.org/MPL/2.0/.
'''
import compile_generic

class Compile(compile_generic.Compile):
    
    def __init__(self):
        compile_generic.Compile.__init__(self,"lib_screencapture","xorg")
    
    def get_os_config(self,osn):
        conf=None
        if osn=="linux":
            conf={}
            conf["outname"]="dwagscreencapturexorg.so" 
            conf["libraries"]=["X11", "Xext", "dl", "Xtst", "Xdamage", "Xfixes"]
            conf["cpp_compiler_flags"]="-DOS_XORG"
        return conf
    

if __name__ == "__main__":    
    m = Compile()
    m.run()
    
    
    
    
    
    