import re
class Bitwidth():
    def __init__(self,str = "",owner_obj = None):
        str = str.replace(' ','').replace('[','').replace(']','')
        self.str = str
        self.link_str = str

        temp_lt = str.split(':')
        
        if (len(temp_lt)!=2):
            if (str != ''):
                print ("Bitwidth error str:" , str)
            else:
                self.top_str = '0'
                self.down_str = '0'
                self.str = '%s:%s'%(self.top_str,self.down_str)

        else:
            self.top_str = temp_lt[0]
            self.down_str = temp_lt[1]

        self.owner_obj = owner_obj
        self.link_param_obj = []
        pass
    def __repr__(self):
        return ('[%s]'%(self.str))
        pass

    def SetOwner(owner_obj):
        self.owner_obj = owner_obj

    def LinkParameter(self,link_lt):
        re_txt = r'[^\W]+'
        re_res_lt = re.findall(re_txt,self.link_str)
        link_succ = True
        for re_res in re_res_lt:
            check_all_num = re.findall(r'[^0-9]',re_res)
            if (len(check_all_num)>0):
                link_succ = False
                for link in link_lt:
                    if ((link.name) == re_res):
                        link_succ = True
                        self.link_str = self.link_str.replace(link.name,'$'+str(len(self.link_param_obj)))
                        self.link_param_obj.append (link)
                        break
                
                if (link_succ == False):
                    # print ('Bitwidth: link parameter failed! Can\'t find',re_res,', port name:',self.owner_obj.owner_obj.name,'/',self.owner_obj.name)
                    print ('Bitwidth: link parameter failed! Can\'t find parameter: %s, port name: %s/%s'%(
                        re_res
                        ,self.owner_obj.owner_obj.name
                        ,self.owner_obj.name))
        return (link_succ)

class Param_bitwidth(Bitwidth):
    def __init__(self,str = "",owner_obj = None):
        super(Param_bitwidth, self).__init__(str,owner_obj)

        if (str == ''):
            self.unsize = True
        else:
            self.unsize = False

def test():
    A = Bitwidth('[ass:0]')
    pass


# test()