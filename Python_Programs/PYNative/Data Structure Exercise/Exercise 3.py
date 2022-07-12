"""Exercise 3: Slice list into 3 equal chunks and reverse each chunk"""

sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
size = len(sample_list)
chunk_size = int(size / 3)
start = 0
end = chunk_size

for i in range(3):
    index = slice(start, end)
    list_chunk = sample_list[index]
    print(list_chunk)
    start = end
    end += chunk_size
