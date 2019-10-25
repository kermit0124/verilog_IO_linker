import numpy as np



def main():
	fp = open("D:\\DevProjects\\anaconda\\verilog_IO_linker\\axis_async_fifo_adapter.v", "r")

	num_module = 0
	rangeCM = 0
	PF__moduleName = 0
	moduleName = ""

	for lineTxt in iter(fp):
		remain_txt = ""
		if (rangeCM==0):
			if ("/*") in lineTxt:
				if ("*/") in lineTxt:
					rangeCM = 0
					remain_txt = remain_txt + lineTxt.split("/*")[0] + " "
					remain_txt += lineTxt.split("*/")[1]
					a=1
				else:
					rangeCM = 1
			else:
				remain_txt = lineTxt
		else:
			if ("*/") in lineTxt:
				rangeCM = 0
				remain_txt = lineTxt.split("*/")[1]
		remain_txt = remain_txt.split("//")[0]


		if (rangeCM==0):
			parse_keywords = remain_txt.split(" ")
			for parse_keyword in parse_keywords:
				if (PF__moduleName==1):
					PF__moduleName = 0
					moduleName = parse_keyword


				if (parse_keyword=="module"):
					num_module+=1
					PF__moduleName = 1
				

	fp.close()
	a=0

if __name__ =="__main__":
	main()