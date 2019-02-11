"""is valid number

what is a valid number?

134
534
0
0.5
.5
1e4
1e-4
-4
-01e5
“   4  ”
0.3e2
1e0.4e2 == NO!

rules:
digits
decimals
whitespace allowed at edges
negative/positive
	exponential before OR after decimal (mutually exclusive)


everything bug exponents:
	

“[-+]?(\d*\.?\d*|\d+e[-+]?\d+|\d*\.\d+e[-+]?\d+)"""
def is_number(s):
	# regular numbers
	if re.findall("[-+]?\d*\.?\d*", s.strip()):
		return True
	# exponents before decimal
	elif re.findall("[-+]?(\d+e[-+]?\d+)", s.strip()):
		return True
	# exponents after decimal
	elif re.findall("[-+]?(\d*\.\d+e[-+]?\d+)", s.strip()):
			return True

		return False
	



