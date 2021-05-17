import unittest


# the analyze function takes in an var arguent of numbers
# it should return a dicitonary of {'mean':0,'median':0,'mode':0,'largest':0,'smallest':0}
def analyze(*nums):
    nums = list(nums)
    nums.sort()
    nums_sum = sum(nums)
    nums_mean = nums_sum / len(nums)
    if len(nums) % 2 == 0:
        nums_median = (nums[len(nums) // 2] + nums[len(nums) // 2 + 1]) / 2
    else:
        nums_median = nums[len(nums) // 2]
    nums_mode_dict = {}
    for num in nums:
        if str(num) not in nums_mode_dict:
            nums_mode_dict[str(num)] = 1
        else:
            nums_mode_dict[str(num)] += 1
    nums_mode = int(
        sorted(nums_mode_dict, key=nums_mode_dict.get, reverse=True)[0])
    nums_largest = nums[-1]
    nums_smallest = nums[0]
    results = {
        "mean": nums_mean,
        "median": nums_median,
        "mode": nums_mode,
        "largest": nums_largest,
        "smallest": nums_smallest,
    }
    return results


########################### TESTS ##############################################################
class TestMethods(unittest.TestCase):

    def test_analyze_1(self):
        data = analyze(1, 2, 2, 2, 3)
        self.assertDictEqual(data, {
            'mean': 2,
            'median': 2,
            'mode': 2,
            'largest': 3,
            'smallest': 1
        })

    def test_analyze_2(self):
        data = analyze(10, 5, 10, 200, -65)
        self.assertDictEqual(data, {
            'mean': 32,
            'median': 10,
            'mode': 10,
            'largest': 200,
            'smallest': -65
        })


if __name__ == '__main__':
    unittest.main()
