import itertools
from collections import defaultdict
from enum import Enum
import random

class Rarity(Enum):
    UNCOMMON = "uncommon"
    RARE = "rare"
    EPIC = "epic"

def calculate_slot_probabilities(items, top_n=10):
    if len(items) != 5:
        print("Must use 5 items for enhancement!")
        return -1

    slot_probabilities = []
    total_price = 0
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
        
    total_price = sum(item["price"] for item in items)

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
    
    print(f"Total price: {total_price}")

def calculate_item_stats(rarity):
    efficiency, luck, comfort, resilience = 0.0, 0.0, 0.0, 0.0
    if rarity == Rarity.UNCOMMON:
        efficiency = random.uniform(9.6, 21.6)
        luck = random.uniform(9.6, 21.6)
        comfort = random.uniform(9.6, 21.6)
        resilience = random.uniform(9.6, 21.6)
    elif rarity == Rarity.RARE:
        efficiency = random.uniform(18.0, 42.0)
        luck = random.uniform(18.0, 42.0)
        comfort = random.uniform(18.0, 42.0)
        resilience = random.uniform(18.0, 42.0)
    elif rarity == Rarity.EPIC:
        efficiency = random.uniform(33.6, 75.6)
        luck = random.uniform(33.6, 75.6)
        comfort = random.uniform(33.6, 75.6)
        resilience = random.uniform(33.6, 75.6)

    print(f"efficiency: {efficiency:.1f}, luck: {luck:.1f}, comfort: {comfort:.1f}, resilience: {resilience:.1f}")


# Example usage:
items = [
    {"slot1": "C", "slot2": "C", "slot3": "C", "slot4": "C", "price": 5800},
    {"slot1": "L", "slot2": "C", "slot3": "L", "slot4": "L", "price": 3600},
    {"slot1": "L", "slot2": "C", "slot3": "C", "slot4": "L", "price": 4525},
    {"slot1": "C", "slot2": "C", "slot3": "C", "slot4": "L", "price": 5555},
    {"slot1": "C", "slot2": "C", "slot3": "C", "slot4": "C", "price": 6999}
]
calculate_slot_probabilities(items, top_n=15)
calculate_item_stats(Rarity.EPIC)