import itertools
from collections import defaultdict

def calculate_slot_probabilities(items, top_n=10):
    if len(items) != 5:
        print("Must use 5 items for enhancement!")
        return -1

    slot_probabilities = []
    for i in range(4):
        slot_types = {"E": 0, "C": 0, "L": 0, "R": 0}
        for item in items:
            slot_type = item["slot" + str(i+1)]
            if slot_type in slot_types:
                slot_types[slot_type] += 1
        slot_probability = {}
        for slot_type, count in slot_types.items():
            probability = count / len(items)
            slot_probability[slot_type] = probability
        print(f"Slot {i + 1}: {slot_probability}")
        slot_probabilities.append(slot_probability)

    results = {}
    for combination in itertools.product(*[list(slot.keys()) for slot in slot_probabilities]):
        probability = 1
        for i, slot_type in enumerate(combination):
            probability *= slot_probabilities[i][slot_type]
        results["".join(combination)] = probability

    sorted_results = sorted(results.items(), key=lambda x: x[1], reverse=True)

    combined_results = defaultdict(float)
    for result, probability in sorted_results:
        sorted_letters = "".join(sorted([letter for letter in result]))
        combined_results[sorted_letters] += probability

    total_probability = sum(combined_results.values())
    top_results = sorted(combined_results.items(), key=lambda x: x[1], reverse=True)[:top_n]
    for result, probability in top_results:
        print(f"{result}: {probability/total_probability:.2%}")


# Example usage:
items = [
    {"slot1": "E", "slot2": "L", "slot3": "E", "slot4": "C"},
    {"slot1": "E", "slot2": "L", "slot3": "C", "slot4": "C"},
    {"slot1": "C", "slot2": "L", "slot3": "L", "slot4": "E"},
    {"slot1": "E", "slot2": "E", "slot3": "C", "slot4": "C"},
    {"slot1": "L", "slot2": "C", "slot3": "L", "slot4": "L"}
]
calculate_slot_probabilities(items, top_n=20)
