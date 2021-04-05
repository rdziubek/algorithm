A = [0, 1, 0, 1, 2, 3]

max_local = max_total = A[0]
for x in A[1:]:
	max_local = max(x, max_local + x)
	max_total = max(max_total, max_local)
print(max_total)
