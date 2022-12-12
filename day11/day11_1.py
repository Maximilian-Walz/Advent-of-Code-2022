import re

with open("input.txt") as file:
    # Parse the input
    monkeys_input = file.read().split("\n\n")
    monkeys = []
    for monkey_input in monkeys_input:
        monkey = {"item_count": 0}
        monkey["items"] = [int(item) for item in re.search(r'Starting items: (.*)', monkey_input).group(1).split(", ")]
        monkey["operation"] = re.search(r'Operation: new = old (.*)', monkey_input).group(1).split(" ")
        monkey["test_value"] = int(re.search(r'Test: divisible by (\d*)', monkey_input).group(1))
        monkey["true_target"] = int(re.search(r'If true: throw to monkey (\d*)', monkey_input).group(1))
        monkey["false_target"] = int(re.search(r'If false: throw to monkey (\d*)', monkey_input).group(1))
        monkeys.append(monkey)

    # 20 Rounds
    for i in range(20):
        for monkey in monkeys:
            while len(monkey["items"]) > 0:
                # Monkey inspects item
                item = monkey["items"].pop(0)
                monkey["item_count"] += 1
                value = item if monkey["operation"][1] == "old" else int(monkey["operation"][1]) 
                if monkey["operation"][0] == "+":
                    item += value
                elif monkey["operation"][0] == "*":
                    item *= value

                # Monkey gets bored
                item //= 3

                # Monkey tests item
                target = monkey["true_target"] if item % monkey["test_value"] == 0 else monkey["false_target"]
                
                # Monkey throws item
                monkeys[target]["items"].append(item)

    print((lambda x: x[0] * x[1])(sorted([monkey["item_count"] for monkey in monkeys], reverse=True)[:2]))
    