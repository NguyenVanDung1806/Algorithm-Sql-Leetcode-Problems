"""For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
 Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
 I can be placed before V (5) and X (10) to make 4 and 9. 
 X can be placed before L (50) and C (100) to make 40 and 90. 
 C can be placed before D (500) and M (1000) to make 400 and 900.
 Given a roman numeral, convert it to an integer

Ví dụ, 2 được viết là II trong số La Mã, chỉ cần cộng hai số đơn vị lại với nhau. 12 được viết là XII, đơn giản là X + II. Số 27 được viết là XXVII, tức là XX + V + II.

Số La Mã thường được viết từ lớn nhất đến nhỏ nhất từ ​​trái sang phải. Tuy nhiên, số bốn không phải là IIII. Thay vào đó, số bốn được viết là IV. Vì số một đứng trước số năm nên ta trừ nó đi để được bốn. Nguyên tắc tương tự cũng áp dụng cho số chín, được viết là IX. Có sáu trường hợp sử dụng phép trừ:

I có thể được đặt trước V (5) và X (10) để tạo thành 4 và 9.
X có thể được đặt trước L (50) và C (100) để tạo thành 40 và 90.
C có thể được đặt trước D (500) và M (1000) để tạo thành 400 và 900.
Cho một số La Mã, hãy chuyển đổi nó thành số nguyên."""

# IV = 1 + 5 - 2(1) = 4
#a + b -2(a)
#s = XLIX
def romanToInt(self, s):
    dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
            }
    curr = 0
    total = 0 
    prev = 0 
    if i in range (len(s)):
        curr = dict[s[i]] #lay s tai vi tri thu i=0=X => dict(X)=10
        if curr > prev : 
            total = total + curr - 2*(prev)# IV = 1 + 5 - 2(1) = 4
        else :
            total += curr
    prev = curr # ban chat la gia tri dau no se set cho hai thang bang nhau 
    # no se nhau thang phia truoc de tiep tuc duyet
    return total 
    
        