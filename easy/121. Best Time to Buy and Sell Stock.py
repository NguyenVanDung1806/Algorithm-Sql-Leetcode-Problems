# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.
def maxProfit(self , prices):
    min_price = float("inf") #được khởi tạo với giá trị float("inf") (vô cùng lớn), để đảm bảo rằng bất kỳ giá trị nào trong danh sách prices cũng sẽ nhỏ hơn min_price trong lần lặp đầu tiên.
    max_profit = 0
    for price in prices:
        min_price = min(min_price,price)
        max_profit = max(max_profit,price - min_price)
    return max_profit
# Giả sử prices = [7, 1, 5, 3, 6, 4]:
# Bước đầu tiên:
# min_price = float("inf")
# max_profit = 0
# Duyệt qua danh sách:
# price = 7: min_price được cập nhật thành 7, max_profit vẫn là 0.
# price = 1: min_price được cập nhật thành 1, max_profit vẫn là 0.
# price = 5: max_profit được cập nhật thành 5 - 1 = 4.
# price = 3: max_profit vẫn là 4 vì 3 - 1 = 2 nhỏ hơn 4.
# price = 6: max_profit được cập nhật thành 6 - 1 = 5.
# price = 4: max_profit vẫn là 5 vì 4 - 1 = 3 nhỏ hơn 5.
# Kết quả cuối cùng:
# max_profit là 5.
# Do đó, lợi nhuận tối đa có thể đạt được từ việc mua và bán cổ phiếu là 5.





