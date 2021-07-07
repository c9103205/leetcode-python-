def twoSum(nums, target):
    answer = []
     ## python 想遍歷指定 index時，這樣寫。
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i == j:
                continue
            if (nums[i] + nums[j]) == target :
                answer.append(nums[i])
                answer.append(nums[j])
                print(answer)
                return answer;

if __name__ == "__main__":
    nums = [2,7,11,15]
    twoSum(nums,9)

# https://leetcode.com/problems/two-sum/
