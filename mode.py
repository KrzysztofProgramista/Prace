from scipy import stats
oceny = [3,6,4,3,5,3,5,6,5,4,3,4,4,4,3,2,5]
mode = stats.mode(oceny)
print("mode: ")
print(mode)