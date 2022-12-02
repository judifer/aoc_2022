game = [x.strip() for x in open("day02.txt").readlines()]
part_one = {"A X": 4, "A Y": 8, "A Z": 3, "B X": 1, "B Y": 5, "B Z": 9, "C X": 7, "C Y": 2, "C Z": 6}
part_two = {"A X": 3, "A Y": 4, "A Z": 8, "B X": 1, "B Y": 5, "B Z": 9, "C X": 2, "C Y": 6, "C Z": 7}
print(f"Part 1: {sum(part_one[i] for i in game)} | Part 2: {sum(part_two[i] for i in game)}")