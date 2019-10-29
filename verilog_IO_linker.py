import verilog_parser

class class__verilog_IO_linker():
	def __init__(self, fileName):
		self.parser = verilog_parser.class__parser(fileName)
		self.module_data_list = self.parser.get_module_data()
		self.link_prefix = "pf_"
		self.link_suffix = ""
		self.link_inst_name = "aa_inst"
		self.comma_left = 0
		self.tab_char = '\t'
		self.gen_para_assign_mode = 1
		self.templateCode_list = []
		self.link_actIdx = 0
		self.MOD_DATA__MODULE_INFO = 0
		self.MOD_DATA__MODULE_INFO_NAME = 0
		self.MOD_DATA__IO_INFO = 1
		self.MOD_DATA__IO_INFO_NAME = 0
		self.MOD_DATA__IO_INFO_TYPE = 1
		self.MOD_DATA__IO_INFO_BIT = 2
		self.MOD_DATA__PARA_INFO = 2
		self.MOD_DATA__PARA_INFO_NAME = 0
		self.MOD_DATA__PARA_INFO_VAL = 1
		
	
	def __gen__tmpl_assign(self,modData):
		self.templateCode_list.append ("\n// --- assign input/inout ---\n")

		for IO_info in modData[self.MOD_DATA__IO_INFO]:
			IO_name = IO_info[self.MOD_DATA__IO_INFO_NAME].strip()
			IO_type = IO_info[self.MOD_DATA__IO_INFO_TYPE].strip()
			if ((IO_type == "input")|(IO_type == "inout")):
				lineTxt = "assign "
				lineTxt += self.link_prefix + IO_name + self.link_suffix
				lineTxt += " = "
				lineTxt += " ;\n"
				self.templateCode_list.append (lineTxt)
	
	def __gen__tmpl_def_IOs(self,modData):
		self.templateCode_list.append ("\n// --- input/output ---\n")

		for IO_info in modData[self.MOD_DATA__IO_INFO]:
			IO_name = IO_info[self.MOD_DATA__IO_INFO_NAME].strip()
			IO_type = IO_info[self.MOD_DATA__IO_INFO_TYPE].strip()
			IO_bit_list = IO_info[self.MOD_DATA__IO_INFO_BIT]
			lineTxt = "wire "
			if (IO_bit_list):
				lineTxt += '[ '

				# Auto link parameter
				for bit_word in IO_bit_list:
					temp = bit_word.strip()
					for paraInfo in self.module_data_list[self.link_actIdx][self.MOD_DATA__PARA_INFO]:
						paraName = paraInfo[self.MOD_DATA__PARA_INFO_NAME].strip()
						if (paraName) in temp:
							# find linker para
							temp = temp.replace(paraName,self.link_prefix+paraName+self.link_suffix)
							break

					lineTxt += temp
				lineTxt += ' ] '
			lineTxt += self.link_prefix + IO_name + self.link_suffix
			lineTxt += " ;\n"
			self.templateCode_list.append (lineTxt)

	def __gen__tmpl_def_paras(self,modData):
		self.templateCode_list.append ("\n// --- parameter ---\n")

		for paraInfo in modData[self.MOD_DATA__PARA_INFO]:
			paraName = paraInfo[self.MOD_DATA__PARA_INFO_NAME].strip()
			paraVal_list = paraInfo[self.MOD_DATA__PARA_INFO_VAL]
			lineTxt = "localparam "
			lineTxt += self.link_prefix + paraName + self.link_suffix
			lineTxt += " = "
			if (self.gen_para_assign_mode):
				for word in paraVal_list:
					lineTxt += word.strip()
			lineTxt += " ;\n"
			self.templateCode_list.append (lineTxt)
	

	def __gen__tmpl_inst(self,modData):
		self.templateCode_list.append ("\n// --- instance module ---\n")

		lineTxt = ""
		lineTxt = modData[self.MOD_DATA__MODULE_INFO][self.MOD_DATA__MODULE_INFO_NAME] + " # " + chr(40) + '\n'
		self.templateCode_list.append (lineTxt)
		lineTxt = ""

		# Parameters
		self.__gen__tmpl_inst_link(modData[self.MOD_DATA__PARA_INFO])
				
		self.templateCode_list.append (chr(41) + '\n')

		self.templateCode_list.append (self.link_inst_name+'\n')

		self.templateCode_list.append (chr(40) + '\n')

		# IOs		
		self.__gen__tmpl_inst_link(modData[self.MOD_DATA__IO_INFO])

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

	def gen_code(self):
		self.templateCode_list = []
		self.templateCode_list.append ("// ----- verilog IO linker generated -----\n")
		self.__gen__tmpl_def_paras(self.module_data_list[self.link_actIdx])
		self.__gen__tmpl_def_IOs(self.module_data_list[self.link_actIdx])
		self.__gen__tmpl_inst(self.module_data_list[self.link_actIdx])
		self.__gen__tmpl_assign(self.module_data_list[self.link_actIdx])
		return (self.templateCode_list)
	
	def gen_code_file(self,filePath):
		if (len(self.templateCode_list)==0):
			self.gen_code()
		fp = open(filePath, "w")
		for line in self.templateCode_list:
			fp.write (line)

	def show_code(self):
		for line in self.templateCode_list:
			p_line = line
			if (line[len(line)-1:]=='\n'):
				p_line = line[:len(line)-1]
			print (p_line)
	
	def reparse(self,fileName):
		self.parser = verilog_parser.class__parser(fileName)


def main():
	filePath = "D:\\DevProjects\\anaconda\\verilog_IO_linker\\axis_async_fifo_adapter.v"
	
	VIOL = class__verilog_IO_linker(filePath)

	code_list = VIOL.gen_code()

	VIOL.gen_code_file("D:\\DevProjects\\anaconda\\verilog_IO_linker\\gen.v")

	VIOL.show_code()
	
	print ("\n\n\n\nfinish")


if __name__ =="__main__":
	main()