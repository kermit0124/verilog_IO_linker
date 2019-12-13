import verilog_parser
class class__verilog_IO_linker():
	def __init__(self, fileName):
		self.version = "0.2.1"

		fileTxt = ""
		try:
			self.fp = open (fileName,'r')
			fileTxt = self.fp.read()
			self.fp.close()
		except:
			self.fp = ''
			# print ("File path error")
		

		self.parser = verilog_parser.class__parser(fileTxt)
		self.module_data_list = self.parser.get_module_data()
		self.link_prefix = "pf_"
		self.link_suffix = ""
		self.link_inst_name = "inst_name"
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
		self.gen_assign_tmpl_input = 0
		self.gen_assign_tmpl_output = 0
		self.link_param_keep_name = 1
		self.link_wire_add_under_line = 1
	
	def __gen__str_show_module(self):
		return ("// *** module: "+self.link_inst_name+" ( "+self.module_data_list[self.link_actIdx][self.MOD_DATA__MODULE_INFO][self.MOD_DATA__MODULE_INFO_NAME]+" ) ***\n")
	
	def __gen__tmpl_assign(self,modData):
		if (self.gen_assign_tmpl_input):
			self.templateCode_list.append ("\n// --- assign input/inout ---\n")
			self.templateCode_list.append (self.__gen__str_show_module())

			for IO_info in modData[self.MOD_DATA__IO_INFO]:
				IO_name = IO_info[self.MOD_DATA__IO_INFO_NAME].strip()
				IO_type = IO_info[self.MOD_DATA__IO_INFO_TYPE].strip()
				if ((IO_type == "input")|(IO_type == "inout")):
					lineTxt = "assign "
					if (self.link_wire_add_under_line):
						lineTxt += '_' + self.link_prefix + IO_name + self.link_suffix
					else:
						lineTxt += self.link_prefix + IO_name + self.link_suffix
					lineTxt += " = "
					lineTxt += " ;\n"
					self.templateCode_list.append (lineTxt)
		
		if (self.gen_assign_tmpl_output):
			self.templateCode_list.append ("\n// --- assign output ---\n")
			self.templateCode_list.append (self.__gen__str_show_module())
			
			for IO_info in modData[self.MOD_DATA__IO_INFO]:
				IO_name = IO_info[self.MOD_DATA__IO_INFO_NAME].strip()
				IO_type = IO_info[self.MOD_DATA__IO_INFO_TYPE].strip()
				if (IO_type == "output"):					
					lineTxt = "assign "
					lineTxt += " = "
					lineTxt += self.link_prefix + IO_name + self.link_suffix + " ;\n"
					self.templateCode_list.append (lineTxt)


	
	def __gen__tmpl_def_IOs(self,modData):
		self.templateCode_list.append ("\n// --- input/output ---\n")
		self.templateCode_list.append (self.__gen__str_show_module())

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
			
			if (self.link_wire_add_under_line):
				lineTxt += '_' + self.link_prefix + IO_name + self.link_suffix
			else:
				lineTxt += self.link_prefix + IO_name + self.link_suffix
			lineTxt += " ;\n"
			self.templateCode_list.append (lineTxt)

	def __gen__tmpl_def_paras(self,modData):
		self.templateCode_list.append ("\n// --- parameter ---\n")
		self.templateCode_list.append (self.__gen__str_show_module())

		for paraInfo in modData[self.MOD_DATA__PARA_INFO]:
			paraName = paraInfo[self.MOD_DATA__PARA_INFO_NAME].strip()
			paraVal_list = paraInfo[self.MOD_DATA__PARA_INFO_VAL]
			lineTxt = "localparam "
			lineTxt += self.link_prefix + paraName + self.link_suffix
			lineTxt += " = "
			if (self.gen_para_assign_mode):
				for word in paraVal_list:
					
					# auto link parameter
					replace_paraName_word = word.strip()
					for cmpParaInfo in modData[self.MOD_DATA__PARA_INFO]:
						cmpParaName = cmpParaInfo[self.MOD_DATA__PARA_INFO_NAME].strip()
						if (cmpParaName==replace_paraName_word):
							replace_paraName_word = replace_paraName_word.replace(cmpParaName,	self.link_prefix+cmpParaName+self.link_suffix)
							break
					
					if (self.link_param_keep_name):
						replace_paraName_word = paraName

					lineTxt += replace_paraName_word+' '
			lineTxt += " ;\n"
			self.templateCode_list.append (lineTxt)
	

	def __gen__tmpl_inst(self,modData):
		self.templateCode_list.append ("\n// --- instance module ---\n")
		self.templateCode_list.append (self.__gen__str_show_module())

		lineTxt = ""
		lineTxt = modData[self.MOD_DATA__MODULE_INFO][self.MOD_DATA__MODULE_INFO_NAME] + " # " + chr(40) + '\n'
		self.templateCode_list.append (lineTxt)
		lineTxt = ""

		# Parameters
		self.__gen__tmpl_inst_link(modData[self.MOD_DATA__PARA_INFO],1)
				
		self.templateCode_list.append (chr(41) + '\n')

		self.templateCode_list.append (self.link_inst_name+'\n')

		self.templateCode_list.append (chr(40) + '\n')

		# IOs		
		self.__gen__tmpl_inst_link(modData[self.MOD_DATA__IO_INFO])

		self.templateCode_list.append (chr(41) + ' ; \n')

	def __gen__tmpl_inst_link(self,IO_or_para_list,isParam=0):		
		lineTxt = ""
		for idx,data in enumerate(IO_or_para_list):
			lineTxt = lineTxt + self.tab_char
			if ((self.comma_left)&(idx!=0)):
				lineTxt += ','
			lineTxt = lineTxt + '.' + data[0].strip() + ' ( ' 
			if (self.link_wire_add_under_line & (isParam==0)):
				lineTxt += '_'+ self.link_prefix + data[0].strip() + self.link_suffix
			else:
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
		code_list = self.gen_code()
		fp = open(filePath, "w")
		for line in self.templateCode_list:
			fp.write (line)
		fp.close()
		return (code_list)

	def show_code(self):
		for line in self.templateCode_list:
			p_line = line
			if (line[len(line)-1:]=='\n'):
				p_line = line[:len(line)-1]
			print (p_line)
	
	def reparse_file(self,fileName):
		self.fp = open (fileName,'r')
		self.reparse_txt(self.fp.read())
		self.fp.close()
	
	def reparse_txt(self,all_txt):
		self.parser = verilog_parser.class__parser(all_txt)
		self.module_data_list = self.parser.get_module_data()


	def select_modulde(self,module_idx):
		if (module_idx<len(self.module_data_list)):
			self.link_actIdx = module_idx
		else:
			self.link_actIdx = 0
			print ("Error index, select default (0)")
	
	def get_num_module(self):
		return (self.parser.__num_module)
	
	def get_module_name_list(self):
		nameList = []
		for moduleData in self.module_data_list:
			nameList.append (moduleData[self.MOD_DATA__MODULE_INFO])
		return (nameList)

def input_int():
	tempIn = input()
	if (tempIn==''):
		return (0)
	else:
		return (int(tempIn))

def main():
	pass
def ui():
	print ("File:")
	# filePath = input()
	# filePath = "D:\\DevProjects\\anaconda\\verilog_IO_linker\\axis_async_fifo_adapter.v"
	# filePath = ""
	
	VIOL = class__verilog_IO_linker(filePath)
	print ("Module:")
	for idx, module_info in enumerate(VIOL.module_data_list):
		for module_name in module_info[VIOL.MOD_DATA__MODULE_INFO_NAME]:
			print (idx," : ",module_name)

	print ("Select module 0~%d : "%(len(VIOL.module_data_list)-1),end="")
	VIOL.select_modulde (input_int())

	print ("prefix : ",end="")
	VIOL.link_prefix = input()

	print ("suffix : ",end="")
	VIOL.link_suffix = input()

	print ("left comma mode (0 or 1) : ",end="")
	VIOL.comma_left = input_int()
	

	print ("Instance name : ",end="")
	VIOL.link_inst_name = input()

	print ("Generate...\n\n")
	code_list = VIOL.gen_code_file("D:\\DevProjects\\anaconda\\verilog_IO_linker\\gen.v")
	VIOL.show_code()


	# code_list = VIOL.gen_code()

	# VIOL.gen_code_file("D:\\DevProjects\\anaconda\\verilog_IO_linker\\gen.v")

	# VIOL.show_code()

	# VIOL.select_modulde(1)
	# VIOL.gen_code_file("D:\\DevProjects\\anaconda\\verilog_IO_linker\\gen_2.v")
	
	print ("\n\n\n\nfinish")


if __name__ =="__main__":
	main()