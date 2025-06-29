def numdecode(n):
    def decode(index):
        if index == len(n):
            return 1
        if n[index] == '0':
            return 0
        count = decode(index + 1)
        if index + 1 < len(n) and 10 <= int(n[index:index+2]) <= 26:
            count += decode(index + 2)
        return count
    return decode(0)
input_string = "226"
result = numdecode(input_string)
print("Number of ways to decode:", result)