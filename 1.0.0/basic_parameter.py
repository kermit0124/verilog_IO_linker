import re
import bitwidth

class Basic_parameter():
    def __init__(self,name_str,value,depth_str=""):
        # rm_lt = ["[","]"," "]
        # for rm_word in rm_lt:
        #     depth_str = depth_str.replace(rm_word,"")
        
        # if (depth_str!=''):
        #     depth_str = "[%s]"%depth_str

        # self.depth_str = depth_str
        self.value = value
        self.link_value = value
        self.bitwidth = bitwidth.Param_bitwidth(depth_str,self)
        self.name = name_str
        self.owner_obj = None
        self.link_param_obj = []

    def SetOwner(self,owner_obj):
        self.owner_obj = owner_obj
    
    def LinkParameter(self,link_lt):
        # re_txt = r'\w+'
        # value = self.value
        # re_res_lt = re.findall(re_txt,value)
        # for re_res in re_res_lt:
        #     for link in link_lt:
        #         if (link.name) in self.value:
        #             self.value = self.value.replace(link.name,'$'+str(len(self.link_param_obj)))
        #             self.link_param_obj.append (link)

        link_succ = True
        re_txt = r'[\w\']+'
        re_res_lt = re.findall(re_txt,self.link_value)
        for re_res in re_res_lt:
            # check_all_num = re.findall(r'[^0-9]',re_res)
            check_bin_hex_symbo = re.findall(r'(((.+|)\'[bhd])|)(\w+)',re_res)
            
            check_value = re_res
            if (check_bin_hex_symbo!=[]):
                check_value = check_bin_hex_symbo[0][3]

            check_all_num = re.findall(r'[^0-9]',check_value)
            if (check_all_num!=[]):
                link_succ = False
                for link in link_lt:
                    if ((link.name) == re_res):
                        link_succ = True
                        self.link_value = self.link_value.replace(link.name,'$'+str(len(self.link_param_obj)))
                        self.link_param_obj.append (link)
                        break
                
                if (link_succ == False):
                    print ('Parameter: link parameter failed! Can\'t find:%s, parameter:%s, value:%s'%(re_res,self.name,self.value))
        return (link_succ)




class ClassParameter(Basic_parameter):
    def __init__(self,name_str,value,depth_str=""):
        self.override_txt = value
        self.override_objID = None
        self.ignore = False
        super(ClassParameter, self).__init__(name_str.replace(' ',''),value.replace(' ',''),depth_str)
    # def GetVerilogCode(self):
    #     vec_str = self.depth_str if (self.depth_str!="") else ""
    #     rt = vec_str + self.name + " = " + self.value
    #     return (rt)

