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
	
	def scan_all(self):
		for lineTxt in iter(self.fp):
			self.remove_commet(lineTxt)

			if (self.rangeCM==0):
				if (self.word_preProc()==1):
					pb=1
					self.parse()

	
	def parse(self):
		next_is_moduleName = 0
		sts__in_title_para = 0
		for word in self.seg_words:
			if (next_is_moduleName):
				self.moduleName = word
				self.num_module += 1
				next_is_moduleName = 0
			elif (sts__in_title_para):
				if (",") in word:
					pass
				else:
					pass


			if (word=="module"):
				next_is_moduleName = 1
			elif (word=="#"):
				sts__in_title_para = 1


	def word_preProc(self):
		# clear \n
		if (self.remain_txt[len(self.remain_txt)-1:]=='\n'):
			self.remain_txt = self.remain_txt[:len(self.remain_txt)-1]

		self.add_speac()

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
		char_list = ['(' , ')' , ',' , ';']
		for ch in char_list:
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