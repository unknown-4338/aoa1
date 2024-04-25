flag = False

def print_subset_sum(i, n, _set, target_sum, subset):
	global flag
	
	if target_sum == 0:
		
		flag = True
		print("[", end=" ")
		for element in subset:
			print(element, end=" ")
		print("]", end=" ")
		return

	if i == n:
		
		return

	
	print_subset_sum(i + 1, n, _set, target_sum, subset)

	if _set[i] <= target_sum:
		subset.append(_set[i])

		
		print_subset_sum(i + 1, n, _set, target_sum - _set[i], subset)

	
		subset.pop()


if __name__ == "__main__":
	
	set_1 = [1, 2, 1]
	sum_1 = 3
	n_1 = len(set_1)
	subset_1 = []
	print("Output 1:")
	print_subset_sum(0, n_1, set_1, sum_1, subset_1)
	print()
	flag = False

	
	set_2 = [3, 34, 4, 12, 5, 2]
	sum_2 = 30
	n_2 = len(set_2)
	subset_2 = []
	print("Output 2:")
	print_subset_sum(0, n_2, set_2, sum_2, subset_2)
	if not flag:
		print("There is no such subset")
