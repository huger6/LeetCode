def main():
    nums, target = get_input_and_return()
    if nums is not None and target is not None:
        result = get_pairs(nums, int(target))
        print(result)


def get_input_and_return():
    numbers = input("Input: ")
    inicial_bracket_position = numbers.find("[")
    final_bracket_position = numbers.find("]")
    equalsign_position = numbers.find("=")

    if inicial_bracket_position == -1 or final_bracket_position == -1 or equalsign_position == -1:
        print("Invalid input format.")
        return None, None

    target = numbers[equalsign_position + 1:].strip()  # Get target from after '='
    list_as_string = numbers[inicial_bracket_position + 1: final_bracket_position].split(",")
    nums = list(map(int, list_as_string))  # Convert list elements to integers

    if not all_integers(nums) or not target.isdigit():
        print("Invalid input format.")
        return None, None

    return nums, target


def all_integers(lst):
    return all(isinstance(x, int) for x in lst)


def get_pairs(lst, target):
    pairs = []
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] + lst[j] == target:
                pairs.append((i, j))  # Fix here
    return pairs


if __name__ == "__main__":
    main()
