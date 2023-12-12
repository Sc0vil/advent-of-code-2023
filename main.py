# This is a sample Python script.
import re


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def advt1_part1_code():
    # Open the input file to read the datas
    output = 0
    with open('inputs/advtc1-input.txt', 'r') as file:
        for line in file:
            print(line.strip())
            line_without_char = ''.join(char for char in line.strip() if char.isdigit())
            first_line_number = line_without_char[0]
            if len(line_without_char) == 1:
                line_output = first_line_number + first_line_number
                output += int(line_output)
            else:
                last_line_number = line_without_char[-1]
                line_output = first_line_number + last_line_number
                output += int(line_output)
        print("\nPUZZLE OUTPUT = " + str(output))


def advt1_part2_code():
    # Open the input file to read the datas
    output = 0
    matrice_numb_in_letters = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    with open('inputs/advtc1-input.txt', 'r') as file:
        for line in file:
            index = 0
            line_transformed_in_digit = line.strip()
            print("first line => " + line_transformed_in_digit)
            for numb_match in matrice_numb_in_letters:
                if line_transformed_in_digit.__contains__(numb_match):
                    line_transformed_in_digit = line_transformed_in_digit.replace(numb_match,
                                                                                  numb_match[0] + str(index) +
                                                                                  numb_match[-1])
                index += 1
            print("final line => " + line_transformed_in_digit)
            line_without_char = ''.join(char for char in line_transformed_in_digit if char.isdigit())
            print("final line without char => " + line_without_char)
            first_line_number = line_without_char[0]
            print(len(line_without_char))
            if len(line_without_char) == 1:
                line_output = first_line_number + first_line_number
                output += int(line_output)
            else:
                last_line_number = line_without_char[-1]
                line_output = first_line_number + last_line_number
                output += int(line_output)
            print(line_output)
        print("\nPUZZLE OUTPUT = " + str(output))


def advt2_part1_code():
    game_sum = 0
    game_condition = 1
    game_rules = {"red": 12, "green": 13, "blue": 14}
    with open('inputs/advtc2-input.txt', 'r') as file:
        for line in file:
            game_id = line.strip().split(":")[0].replace("Game ", "")
            game_sets = line.strip().split(":")[1].split(";")
            for game_set in game_sets:
                cube_colors = game_set.split(",")
                for cube_color in cube_colors:
                    cube_number = ''.join(char for char in cube_color if char.isdigit())
                    cube_color = ''.join(char for char in cube_color if char.isalpha())
                    if int(cube_number) > game_rules[cube_color]:
                        game_condition = 0
                        break
            if game_condition == 0:
                game_condition = 1
            else:
                game_sum += int(game_id)
        print("Game sum = " + str(game_sum))

def advt2_part2_code():
    game_power_sum = 0
    fewest_cubes = {"red": 0, "green": 0, "blue": 0}
    with open('inputs/advtc2-input.txt', 'r') as file:
        for line in file:
            game_sets = line.strip().split(":")[1].split(";")
            for game_set in game_sets:
                cube_colors = game_set.split(",")
                print(cube_colors)
                for cube_color in cube_colors:
                    cube_number = ''.join(char for char in cube_color if char.isdigit())
                    cube_color = ''.join(char for char in cube_color if char.isalpha())
                    fewest_cubes[cube_color] = cube_number
                
                if cube_number game_rules[color]
        print("Game power sum = " + str(game_power_sum))


if __name__ == '__main__':
    advt2_part2_code()
