import numpy as np


class class__verilog_IO_linker():
	def __init__(self, fp):
		self.fp = fp
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
		self.char_list = ['(' , ')' , ',' , ';']
		self.varVal_temp =""
		self.varVal =""
		self.paras_list = []
		self.IOs_list = []
	
	def scan_all(self):
		for lineTxt in iter(self.fp):
			self.remove_commet(lineTxt)
			self.add_speac()

			if (self.rangeCM==0):
				if (self.word_preProc()==1):
					pb=1
					# self.parse()
					self.parse_module_title()

	def parse_module_title(self):
		WORD_TYPE_NONE = 0
		WORD_TYPE_MOD_NAME = 1
		WORD_TYPE_PARA_NAME = 2
		WORD_TYPE_PARA_VALUE = 3
		WORD_TYPE_PARA_LBKT = 4
		WORD_TYPE_SYMBO_EQUA = 5
		nextWord_type = WORD_TYPE_NONE
		STS_MODULE_TITLE = 0
		STS_PARA_TITLE = 1
		sts = STS_MODULE_TITLE
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
		
		if (titleParaMode==1):
			c_words,r_words = self.parse_bucket(title_para_and_IO_words[word_SI:])
			self.parseFlow_title_para(c_words)		
		
		c_words,r_words = self.parse_bucket(r_words)
		self.parseFlow_title_IO(c_words)
		aaa=1
	
	def parseFlow_title_IO(self,word_list):
		while (1):
			finded , c_words , word_list = self.parse_symbo(word_list,',')
			IO_name , IO_type = self.parse_IO(c_words)
			self.IOs_list.append ([IO_name,IO_type])

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
		IO_name = ""
		IO_type = ""
		for idx,word in enumerate(word_list):
			if (idx==0):
				IO_type = word
			else:
				if (idx==1):
					if (word=="wire"):
						IO_type = IO_type + " " + word
					else:
						IO_name = word
				else:
					IO_name = word

		return (IO_name,IO_type)




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

	
	def parse(self):
		nextWord_type = "none"
		sts__in_title_para = 0
		for word in self.seg_words:
			if (nextWord_type=="module_name"):
				self.moduleName = word
				self.num_module += 1
				nextWord_type = "none"
			elif (sts__in_title_para):
				if (",") in word:
					pass
				else:
					pass
					# if (word=="parameter"):
					# 	nextWord_type = "parameter_name"
					# else:

					# if (self.norm_word_check(word)):
					# 	if (word!="parameter"):
					# 		self.paraName = word



			if (word=="module"):
				nextWord_type = "module_name"
			elif (word=="#"):
				sts__in_title_para = 1
				nextWord_type = "left_bkt"
			elif (nextWord_type!="none"):
				if (nextWord_type=="left_bkt"):
					if (word==chr(40)):
						nextWord_type = "para_name"
				elif (nextWord_type == "para_name"):
					if (word!="parameter"):
						self.paraName = word
						nextWord_type = "para_val"
				elif (nextWord_type == "para_val"):
					if ((word!=",")|(word!=chr(41))):
						self.varVal_temp = self.varVal_temp + word
					else:
						self.varVal = self.varVal_temp
						self.varVal_temp = ""
						if (word==","):
							nextWord_type = "para_name"
						else:
							nextWord_type = "none"
			


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
	fp = open("D:\\DevProjects\\anaconda\\verilog_IO_linker\\axis_async_fifo_adapter.v", "r")
	VIOL = class__verilog_IO_linker(fp)

	VIOL.scan_all()

	fp.close()

if __name__ =="__main__":
	main()