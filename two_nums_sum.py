
# array = [3, 5, -4, 8, 11, 1, -1, 6]
# Target sum = 10
# 需找出兩數相加為taget sum，第一直覺會使用雙迴圈，但這邊使用一個hash table可以減少時間複雜度

def twoNumberSum(array, targetSum):
    hash_table = {}

    for i in array:
        num = targetSum - i
        if not num in hash_table:
            hash_table[i] = True
        elif num in hash_table:
            return [num, i]

    return []