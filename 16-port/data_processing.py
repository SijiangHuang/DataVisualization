old_lines = []
with open("./test-topo.csv", "r") as f:
    old_lines = f.readlines()
new_lines = ""
new_lines += old_lines[0]
for i in range(1, len(old_lines)):
    new_lines += (old_lines[i].strip() + "," + str(i) + "\n")
with open("./test-topo-new.csv", "w") as f:
    f.write(new_lines)