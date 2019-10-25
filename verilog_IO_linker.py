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
		self.proc_word = ""
	
	def scan_all(self):
		for lineTxt in iter(self.fp):
			self.remove_commet(lineTxt)
			if (self.rangeCM==0):
				self.word_preProc()
				for self.proc_word in self.words:
					self.get_modueName()

	def word_preProc(self):
		# clear \n
		if (self.remain_txt[len(self.remain_txt)-1:]=='\n'):
			self.remain_txt = self.remain_txt[:len(self.remain_txt)-1]

		self.words = self.remain_txt.split(" ")

	
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
		

	def get_modueName(self):
		if (self.nextWord_is_moduleName):
			self.nextWord_is_moduleName = 0
			self.moduleName = self.proc_word
			self.sts__in_module = 1
			self.num_module+=1

		if (self.proc_word=="module"):
			self.nextWord_is_moduleName = 1
		elif (self.proc_word=="endmodule"):
			self.sts__in_module = 0
	
	# def get_params(self):




def main():
	fp = open("D:\\DevProjects\\anaconda\\verilog_IO_linker\\axis_async_fifo_adapter.v", "r")
	VIOL = class__verilog_IO_linker(fp)

	VIOL.scan_all()

	fp.close()

if __name__ =="__main__":
	main()