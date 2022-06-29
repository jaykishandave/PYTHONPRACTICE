# Exercise 3: Create a new string made of the first, middle, and last characters of
# each input string

s1 = "America"
s2 = "Japan"

size_s1 = len(s1)
size_s2 = len(s2)
mid_s1 = size_s1//2
mid_s2 = size_s2//2
m_s1=s1[mid_s1]
m_s2=s2[mid_s2]
f_s1 = s1[0]
f_s2 = s2[0]

new_str=f_s1+f_s2+m_s1+m_s2+s1[size_s1-1]+s2[size_s2-1]

print(new_str)

