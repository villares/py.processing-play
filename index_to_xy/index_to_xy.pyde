TUPLES = []
row_size, num_lines = 5, 4
for y in range(num_lines):
    for x in range(row_size):
        TUPLES.append((x, y))

for i, (x, y) in enumerate(TUPLES):
    println((x,
             y,
             i % row_size,
             int(i / row_size)
             ))
