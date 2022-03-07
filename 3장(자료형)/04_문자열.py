# 문자열 실습

# 큰 따옴표(double quotation marks), 작은 따옴표(single quotation marks)

print("Hello, my friend!")
print("Hello, \"woo\" my friend!")
print("Hello, 'woo' my friend!")

# 이스케이프 문자들의 기능을 제거하기 위해서는 문자열 앞에 r을 붙여준다.
print("c:\temp\name\a.txt")
print(r"c:\temp\name\a.txt")

message = "Hello python"
print("\"%s\"의 길이:"%message, len(message))