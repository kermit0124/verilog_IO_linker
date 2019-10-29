import numpy as np
import verilog_parser

class class__verilog_IO_linker():
	def __init__(self, fileName):
		self.parser = verilog_parser.class__parser(fileName)
		self.module_data_list = self.parser.get_module_data()


def main():
	filePath = "D:\\DevProjects\\anaconda\\verilog_IO_linker\\axis_async_fifo_adapter.v"
	VIOL = class__verilog_IO_linker(filePath)
	
	print ("finish")


if __name__ =="__main__":
	main()