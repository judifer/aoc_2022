from collections import defaultdict

inp = [[y.strip() for y in x.split("\n")] for x in open("day11.txt").read().split("\n\n")]

monkeys = defaultdict(list)
monkeys_2 = defaultdict(list)
operations = defaultdict(list)
for i in inp:
    _, curr_mon = i[0].split()
    curr_mon = int(curr_mon[:-1])
    _, it = i[1].split(": ")
    items = [int(x) for x in it.split(", ")]
    for j in items:
        monkeys[curr_mon].append(j)
        monkeys_2[curr_mon].append(j)
    _, _, _, _, operator, number = i[2].split()
    operations[curr_mon].append(operator)
    operations[curr_mon].append(number)
    _, _, _, div = i[3].split()
    div = int(div)
    operations[curr_mon].append(div)
    _, _, _, _, _, truetarget = i[4].split()
    truetarget = int(truetarget)
    operations[curr_mon].append(truetarget)
    _, _, _, _, _, falsetarget = i[5].split()
    falsetarget = int(falsetarget)
    operations[curr_mon].append(falsetarget)

round = 0
active = defaultdict()
for i in monkeys.keys():
    active[i] = 0

for _ in range(20):
    for i in monkeys.keys():
        for j in monkeys[i]:
            testing = operations[i][2]
            true_mon = operations[i][3]
            false_mon = operations[i][4]
            active[i] += 1
            if operations[i][0] == "*":
                if operations[i][1] == "old":
                    div = j
                else:
                    div = int(operations[i][1])
                new_num = (j * div) // 3
                if (new_num / testing) == (new_num // testing):
                    monkeys[true_mon].append(new_num)
                else:
                    monkeys[false_mon].append(new_num)
            elif operations[i][0] == "+":
                if operations[i][1] == "old":
                    div = j
                else:
                    div = int(operations[i][1])
                new_num = (j + div) // 3
                if (new_num / testing) == (new_num // testing):
                    monkeys[true_mon].append(new_num)
                else:
                    monkeys[false_mon].append(new_num)
        monkeys[i] = list()

result = sorted(active.values())
print(result[-1] * result[-2])

# Part 2

active = defaultdict()
for i in monkeys.keys():
    active[i] = 0

modifier = 1
for i in operations.keys():
    modifier *= operations[i][2]

for _ in range(10000):
    for i in monkeys_2.keys():
        for j in monkeys_2[i]:
            testing = operations[i][2]
            true_mon = operations[i][3]
            false_mon = operations[i][4]
            active[i] += 1
            if operations[i][0] == "*":
                if operations[i][1] == "old":
                    div = j
                else:
                    div = int(operations[i][1])
                new_num = (j * div) % modifier
                if new_num % testing == 0:
                    monkeys_2[true_mon].append(new_num)
                else:
                    monkeys_2[false_mon].append(new_num)
            elif operations[i][0] == "+":
                if operations[i][1] == "old":
                    div = j
                else:
                    div = int(operations[i][1])
                new_num = (j + div) % modifier
                if new_num % testing == 0:
                    monkeys_2[true_mon].append(new_num)
                else:
                    monkeys_2[false_mon].append(new_num)
        monkeys_2[i] = list()

result = sorted(active.values())
print(result[-1] * result[-2])