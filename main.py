def calculate_slot_probabilities(items):
    slot_probabilities = []
    for i in range(4):
        slot_types = {"E": 0, "C": 0, "L": 0, "R": 0}
        for item in items:
            slot_type = item[i]
            if slot_type in slot_types:
                slot_types[slot_type] += 1
        slot_probability = {}
        for slot_type, count in slot_types.items():
            probability = count / len(items)
            slot_probability[slot_type] = probability
        slot_probabilities.append(slot_probability)
    results = {}
    for i in range(len(slot_probabilities)):
        for j in range(i+1, len(slot_probabilities)):
            for k in range(j+1, len(slot_probabilities)):
                for l in range(k+1, len(slot_probabilities)):
                    result = ""
                    for slot_type in ["E", "C", "L", "R"]:
                        max_probability = max(slot_probabilities[i][slot_type], slot_probabilities[j][slot_type], slot_probabilities[k][slot_type], slot_probabilities[l][slot_type])
                        if max_probability == 0:
                            result += "-"
                        else:
                            for slot in [i, j, k, l]:
                                if slot_probabilities[slot][slot_type] == max_probability:
                                    result += items[slot][slot_type]
                                    break
                    if result in results:
                        results[result] += 1
                    else:
                        results[result] = 1
    total_combinations = sum(results.values())
    for result, count in sorted(results.items(), key=lambda x: x[1], reverse=True):
        probability = count / total_combinations
        print(result + ":", probability)

# Example usage:
items = [
    {"E": "L", "E": "C"},
    {"E": "L", "C": "C"},
    {"C": "L", "L": "E"},
    {"E": "E", "C": "C"},
    {"L": "C", "L": "L"}
]
calculate_slot_probabilities(items)
