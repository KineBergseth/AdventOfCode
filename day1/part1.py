with open("day1_input.txt") as calories_list:
    lines = calories_list.readlines()
input_values = [line.strip() for line in lines]


def sort_elves_by_calories(rations):
    elf_calorie_count = []
    calories = 0

    for snack in rations:
        if snack == '':
            elf_calorie_count.append(calories)
            calories = 0
            continue

        calories += int(snack)

    return sorted(elf_calorie_count, reverse=True)


def find_most_calories(rations):
    calorie_list = sort_elves_by_calories(rations)
    return calorie_list[0]


def top_three_calories(rations):
    calorie_list = sort_elves_by_calories(rations)
    return sum(calorie_list[:3])


if __name__ == "__main__":
    print(f'Part 1: {find_most_calories(input_values)}')
    print(f'Part 2: {top_three_calories(input_values)}')
