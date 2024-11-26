class Solution:
    def threeSum(self, nums):
        n = len(nums)
        nums.sort()  # O(nlogn)
        three_sums = []

        # Two-pointer search: O(n^2)
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip duplicate numbers

            target = -nums[i]
            left, right = i + 1, n - 1

            while left < right:
                current_sum = nums[left] + nums[right]

                if current_sum == target:
                    three_sums.append([nums[i], nums[left], nums[right]])

                    # Skip duplicates for left and right elements
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # Move both pointers inward after finding a valid triplet
                    left += 1
                    right -= 1
                elif current_sum < target:
                    # Move left pointer to increase the sum
                    left += 1
                else:
                    # Move right pointer to decrease the sum
                    right -= 1

        return three_sums
