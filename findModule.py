# from
# http://effbot.org/librarybook/sys.htm
import sys
def dump(module):
	print module, "=>",
	if module in sys.builtin_module_names:
		print "<BUILTIN>"
	else:
		module = __import__(module)
		print module.__file__
	# end if
# end dump

dump("string")
dump("parser")
