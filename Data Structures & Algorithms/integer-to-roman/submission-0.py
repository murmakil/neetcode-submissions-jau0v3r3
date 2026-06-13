class Solution:
    def intToRoman(self, num: int) -> str:
        num_str = str(num)
        d = dict([[1, "I"], [2, "II"], [3, "III"], [4, "IV"], [5, "V"], [6, "VI"],
          [7, "VII"], [8, "VIII"], [9, "IX"], [10, "X"], [50, "L"], [100, "C"],
          [500, "D"], [1000, "M"]])
        nums = []
        while len(num_str) != 0:
            nums.append(num_str[0] + ("0")* (len(num_str) - 1))
            num_str = num_str.replace(num_str[0], "", 1)
        nums = [int(num) for num in nums if num[0] != "0"]
        keys = []
        i = 0
        for k in reversed(d.keys()):
            if k > nums[i]:
                continue
            elif k == nums[i]:
                keys.append(k)
                if nums[i] != nums[-1]:
                    i += 1
            else:
                keys.append(k)
        res = ""
        for num in nums:
            while num < keys[0]:
                keys.pop(0)
            if num == 900:
                res += "CM"
            elif num == 90:
                res += "XC"
            elif num == 40:
                res += "XL"
            elif num == 400:
                res += "CD"
            elif num % keys[0] == 0:
                res += (d[keys[0]]) * int(num/keys[0])
            elif num in keys:
                res += d[num]
            else:
                res += (d[keys[0]]) * int(num/keys[0])
                nums.insert(nums.index(num)+1, num - keys[0])
                keys.pop(0)
        return res