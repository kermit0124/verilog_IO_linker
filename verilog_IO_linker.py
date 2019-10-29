import numpy as np


class class__verilog_IO_linker():
	def __init__(self, fileName):
		self.fp = open(fileName, "r")
		self.rangeCM = 0
		self.remain_txt = ""
		self.words = []
		self.num_module = 0
		self.moduleName = ""
		self.nextWord_is_moduleName = 0
		self.sts__in_module = 0
		self.sts__in_module_title = 0
		self.proc_word = ""
		self.sts__in_bracket = 0
		self.sts__in_title_para = 0
		self.bracket_stack = 0
		self.seg_words = []
		self.num_paras = 0
		self.paraName = ""
		self.paraValue = ""
		self.char_list = ['(' , ')' , ',' , ';','[',']']
		self.varVal_temp =""
		self.varVal =""
		self.paras_list = []
		self.IOs_list = []
		self.inText = 0

		self.scan_all()
		self.fp.close()
	
	def scan_all(self):
		for lineTxt in iter(self.fp):
			self.remove_commet(lineTxt)
			self.add_speac()

			if (self.rangeCM==0):
				if (self.word_preProc()==1):

					if (self.sts__in_module==0):
						self.parseFlow_module_title()
					else:
						self.parseFlow_body()
	
	def __bodyDict_para(self,idx):
		paraName,paraValue = self.parse_parameter(self.seg_words[idx:])
		self.paras_list.append ([paraName,paraValue])
	def __bodyDict_IO(self,idx):
		self.parse_IO(self.seg_words[idx:])

	def parseFlow_body(self):
		dict = {
			"parameter":self.__bodyDict_para
			,"input":self.__bodyDict_IO
			,"output":self.__bodyDict_IO
			,"inout":self.__bodyDict_IO
		}
		idx_st = 0
		for idx,word in enumerate(self.seg_words):
			if (self.inText==1):
				if (chr(34)) in word:
					self.inText = 0
			else:
				if (chr(34)) in word:
					self.inText = 1
				else:
					if (dict.get(word)):
						dict[word](idx)
		
		para_words = self.seg_words[idx_st:]

	def parseFlow_module_title(self):
		WORD_TYPE_NONE = 0
		WORD_TYPE_MOD_NAME = 1
		nextWord_type = WORD_TYPE_NONE
		titlePara_words = []
		num_bkt = 0
		titlePara_SI = 0
		titlePara_EI = 0
		for idx,word in enumerate(self.seg_words):
			if (nextWord_type == WORD_TYPE_NONE):				
				if (word == "module"):
					nextWord_type = WORD_TYPE_MOD_NAME
			
			elif(nextWord_type == WORD_TYPE_MOD_NAME):
				self.moduleName = word
				nextWord_type = WORD_TYPE_NONE
				titlePara_SI = idx+1
				break
		title_para_and_IO_words = self.seg_words [titlePara_SI:]

		titleParaMode = 0
		for idx,word in enumerate(title_para_and_IO_words):
			if (word=="#"):
				titleParaMode = 1
				word_SI = idx+1
				break
			elif (word == chr(40)):
				word_SI = idx
				break
		
		c_words,r_words = "" , ""
		if (titleParaMode==1):
			c_words,r_words = self.parse_bucket(title_para_and_IO_words[word_SI:])
			self.parseFlow_title_para(c_words)		
		
		c_words,r_words = self.parse_bucket(r_words)
		self.parseFlow_title_IO(c_words)

		self.sts__in_module = 1

	
	def parseFlow_title_IO(self,word_list):

		while (1):
			finded , c_words , word_list = self.parse_symbo(word_list,',')
			
			title_def_mode = 0
			for word in c_words:
				if ((word=="input")|(word=="output")|(word=="inout")):
					title_def_mode = 1

			if (title_def_mode):
				self.parse_IO(c_words)
				# IO_name , IO_type , IO_bitWidth = self.parse_IO(c_words)
				# self.IOs_list.append ([IO_name,IO_type,IO_bitWidth])

			if (finded==0):
				break


	def parseFlow_title_para(self,word_list):
		while (1):
			finded , c_words , word_list = self.parse_symbo(word_list,',')
			paraName , paraValue = self.parse_parameter(c_words)
			self.paras_list.append ([paraName,paraValue])

			if (finded==0):
				break
	
	def parse_parameter(self,word_list):
		finded_eq , c_eq_words , r_eq_words = self.parse_symbo(word_list,'=')
		paraName = ""
		paraValue = ""
		if (finded_eq):
			for word in c_eq_words:
				if (word != "parameter"):
					paraName = word
			
			paraValue = r_eq_words

		return (paraName,paraValue)
	
	def parse_IO(self,word_list):
		df_format_bitwidth = 0
		df_format_wire = 0
		for word in word_list:
			if ('[') in word:
				df_format_bitwidth = 1
			elif (']') in word:				
				df_format_bitwidth = 1
			elif (word == "wire"):
				df_format_wire = 1

		IO_name = ""
		IO_type = ""
		IO_bitWidth = []
		for idx,word in enumerate(word_list):
			if ((df_format_bitwidth==0)&(df_format_wire==0)):
				if (idx==0):
					IO_type = word
				else:
					IO_name = word
				IO_bitWidth = None
			elif ((df_format_bitwidth==0)&(df_format_wire==1)):
				if ((idx==0)|(idx==1)):
					if (word!="wire"):
						IO_type = word
				else:
					IO_name = word
				IO_bitWidth = None
			elif ((df_format_bitwidth==1)&(df_format_wire==0)):
				if (idx==0):
					IO_type = word
				else:
					IO_bitWidth , r_words = self.parse_bitWidth(word_list[idx:])
					for word2 in r_words:
						IO_name = IO_name + word2 + " "
					break				
			else:
				if ((idx==0)|(idx==1)):
					if (word!="wire"):
						IO_type = word
				else:
					IO_bitWidth , r_words = self.parse_bitWidth(word_list[idx:])
					for word2 in r_words:
						IO_name = IO_name + word2 + " "
					break
		self.IOs_list.append([IO_name,IO_type,IO_bitWidth])

		# return (IO_name.strip(),IO_type.strip(),IO_bitWidth)

	def parse_bitWidth(self,word_list):
		idx_s , idx_e = 0 , 0
		for idx,word in enumerate(word_list):
			if (chr(91)) in word:
				idx_s = idx
				if (chr(93)) in word:
					idx_e = idx
			elif (chr(93)) in word:
				idx_e = idx
				break
		
		bitWidth = []
		if (idx_s == idx_e):
			bitWidth = word_list[idx_s+1]
		else:
			bitWidth = word_list[idx_s+1:idx_e]
		r_words = word_list[idx_e+1:]

		return (bitWidth , r_words)

	def parse_symbo(self,word_list,find_symbo):
		idx_end = 0
		finded = 0
		c_words = ''
		r_words = ''
		for idx,word in enumerate(word_list):
			if (word==find_symbo):
				idx_end = idx
				finded = 1
				break
		if (finded==1):
			c_words = word_list[:idx_end]
			r_words = word_list[idx_end+1:]
		else:
			c_words = word_list
			r_words = ""

		return (finded,c_words,r_words)

	def parse_bucket(self,word_list):
		num_bkt = 0
		for idx,word in enumerate(word_list):
			if (word == chr(40)):
					if (num_bkt ==0):
						titlePara_SI = idx+1
					num_bkt += 1
			elif (word == chr(41)):
				num_bkt -= 1
				if (num_bkt==0):
					titlePara_EI = idx
					inBucket_words = word_list[titlePara_SI:titlePara_EI]
					break
		
		remain_words = word_list[titlePara_EI+1:]
		return (inBucket_words,remain_words)



	def norm_word_check(self,word):
		for ch in self.char_list:
			if (word==ch):
				return (0)
		return (1)


	def word_preProc(self):
		# clear \n
		if (self.remain_txt[len(self.remain_txt)-1:]=='\n'):
			self.remain_txt = self.remain_txt[:len(self.remain_txt)-1]

		reamin_split = self.remain_txt.split(" ")
		for temp in reamin_split:
			if (temp!=''):
				if (temp==';'):
					self.seg_words = self.words
					self.words =[]
					return (1)
				else:
					self.words.append (temp)
		
		return (-1)
	
	def add_speac(self):
		for ch in self.char_list:
			if (len(self.remain_txt)>1):
				if (ch) in self.remain_txt:
					self.remain_txt =  self.remain_txt.replace(ch," "+ch+" ")

	
	def remove_commet(self,lineTxt):
		remain_txt = ""
		if (self.rangeCM==0):
			if ("/*") in lineTxt:
				if ("*/") in lineTxt:
					self.rangeCM = 0
					remain_txt = remain_txt + lineTxt.split("/*")[0] + " "
					remain_txt += lineTxt.split("*/")[1]
					a=1
				else:
					self.rangeCM = 1
			else:
				remain_txt = lineTxt
		else:
			if ("*/") in lineTxt:
				self.rangeCM = 0
				remain_txt = lineTxt.split("*/")[1]
		remain_txt = remain_txt.split("//")[0]
		self.remain_txt = remain_txt
		



def main():
	filePath = "D:\\DevProjects\\anaconda\\verilog_IO_linker\\axis_async_fifo_adapter.v"
	VIOL = class__verilog_IO_linker(filePath)
	
	print ("finish")


if __name__ =="__main__":
	main()