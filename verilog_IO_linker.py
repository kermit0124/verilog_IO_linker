import verilog_parser

class class__verilog_IO_linker():
	def __init__(self, fileName):
		self.parser = verilog_parser.class__parser(fileName)
		self.module_data_list = self.parser.get_module_data()
		self.link_prefix = "pf_"
		self.link_suffix = "_sf"
		self.link_inst_name = "aa_inst"
		self.comma_left = 0
		self.tab_char = '\t'
		self.templateCode_list = []
		
		self.__gen__tmpl_inst(self.module_data_list[0])
	
	# def gen_code(self):
	# 	for module_data in self.module_data_list:
	def __gen__tmpl_inst(self,modData):
		MOD_DATA__MODULE_INFO = 0
		MOD_DATA__MODULE_INFO_NAME = 0
		MOD_DATA__IO_INFO = 1
		MOD_DATA__PARA_INFO = 2
		MOD_DATA__PARA_INFO_NAME = 0
		MOD_DATA__PARA_INFO_VAL = 1

		lineTxt = ""
		lineTxt = modData[MOD_DATA__MODULE_INFO][MOD_DATA__MODULE_INFO_NAME] + " # " + chr(40) + '\n'
		self.templateCode_list.append (lineTxt)
		lineTxt = ""

		# Parameters
		self.__gen__tmpl_inst_link(modData[MOD_DATA__PARA_INFO])
				
		self.templateCode_list.append (chr(41) + '\n')

		self.templateCode_list.append (self.link_inst_name+'\n')

		self.templateCode_list.append (chr(40) + '\n')

		# IOs		
		self.__gen__tmpl_inst_link(modData[MOD_DATA__IO_INFO])

		self.templateCode_list.append (chr(41) + ' ; \n')

	def __gen__tmpl_inst_link(self,IO_or_para_list):		
		lineTxt = ""
		for idx,data in enumerate(IO_or_para_list):
			lineTxt = lineTxt + self.tab_char
			if ((self.comma_left)&(idx!=0)):
				lineTxt += ','
			lineTxt = lineTxt + '.' + data[0].strip() + ' ( ' 
			lineTxt += self.link_prefix + data[0].strip() + self.link_suffix
			lineTxt += ' ) '
			if ((self.comma_left==0)&(idx!=(len(IO_or_para_list)-1))):
				lineTxt += ','
			lineTxt += '\n'
			self.templateCode_list.append (lineTxt)
			lineTxt = ""


def main():
	filePath = "D:\\DevProjects\\anaconda\\verilog_IO_linker\\axis_async_fifo_adapter.v"
	VIOL = class__verilog_IO_linker(filePath)

	show_code(VIOL.templateCode_list)
	
	print ("finish")

def show_code(code_list):
	for line in code_list:
		print (line)

if __name__ =="__main__":
	main()