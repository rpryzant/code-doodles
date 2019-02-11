"""summary ranges

array a (int)

return list of strings describing ranges

a range = a consecutive subsequence of a that incrases w/slope 1 
a range description: %s->%s % first element of range, last element of range


negative numbers count as range? 
any guarentees on length of a? no
repeats?

== PSEUDOCODE 

# check extreme a cases

set range start to a[0]
loop through rest of a
	if a[i] - a[i - 1] > 1:
		add range ending at i-1 to output
		set range start to a[i]

add range ending at a[-1] to output

return output

== EXAMPLE 0 1 2 4 5 7
                     ^
range start	7
out		[0->2, 4->5, 7]

"""





def summary_ranges(a):
	if not a:
		return []

	out = []
	rs = a[0]
	for i, x in enumerate(a[1:]):
		if x - a[i] > 1:
			out.append('%d->%d' % (rs, a[i])if a[i] != rs else str(rs))
			rs = x
	out.append('%d->%d' % (rs, a[-1]) if a[-1] != rs else str(rs))

	return out


print summary_ranges([0,1,2,4,5,7])
print summary_ranges([0,2,3,4,6,8,9])
