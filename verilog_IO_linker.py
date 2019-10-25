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
	
	def scan_all(self):
		for lineTxt in iter(self.fp):
			self.remove_commet(lineTxt)
			if (self.rangeCM==0):
				self.get_words()
				self.get_modueName()

	
	
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
		
	def get_words(self):
		self.words = self.remain_txt.split(" ")

	def get_modueName(self):
		for word in self.words:
			if (word=="module"):
				self.num_module+=1
				self.nextWord_is_moduleName = 1
			else:
				if (self.nextWord_is_moduleName):
					self.nextWord_is_moduleName = 0
					self.moduleName = word

	



def main():
	fp = open("D:\\DevProjects\\anaconda\\verilog_IO_linker\\axis_async_fifo_adapter.v", "r")
	VIOL = class__verilog_IO_linker(fp)

	VIOL.scan_all()

	fp.close()

if __name__ =="__main__":
	main()