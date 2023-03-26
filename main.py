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
        slot_probabilities.append(slot_probability)

    results = {}
    for i in range(len(slot_probabilities[0])):
        for j in range(len(slot_probabilities[1])):
            for k in range(len(slot_probabilities[2])):
                for l in range(len(slot_probabilities[3])):
                    result = ""
                    total_probability = 1
                    for m, slot in enumerate([i, j, k, l]):
                        slot_key = "slot" + str(m+1)
                        slot_type = list(slot_probabilities[m].keys())[slot]
                        result += slot_key + slot_type
                        total_probability *= slot_probabilities[m][slot_type]
                    if result in results:
                        results[result] += total_probability
                    else:
                        results[result] = total_probability

    sorted_results = sorted(results.items(), key=lambda x: x[1], reverse=True)
    for i in range(min(top_n, len(sorted_results))):
        result, probability = sorted_results[i]
        print(result + ":", probability)

# Example usage:
items = [
    {"slot1": "E", "slot2": "L", "slot3": "E", "slot4": "C"},
    {"slot1": "E", "slot2": "L", "slot3": "C", "slot4": "C"},
    {"slot1": "C", "slot2": "L", "slot3": "L", "slot4": "E"},
    {"slot1": "E", "slot2": "E", "slot3": "C", "slot4": "C"},
    {"slot1": "L", "slot2": "C", "slot3": "L", "slot4": "L"}
]
calculate_slot_probabilities(items, top_n=20)
