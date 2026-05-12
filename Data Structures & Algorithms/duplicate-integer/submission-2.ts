class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums: number[]): boolean {
        const cache = new Set()

        for (const num of nums) {
            if(cache.has(num) === true) {
                return true
            }

            cache.add(num)
        }

        return false
    }
}
