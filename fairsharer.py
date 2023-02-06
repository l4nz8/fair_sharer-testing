def fair_sharer(values, num_iterations, share=0.1):

    for i in range(num_iterations):
        max_index = values.index(max(values))
        max_value = values[max_index]
        share_value = int(max_value * share)
        values[max_index] -= share_value * 2
        values[max_index -1] += share_value
        values[(max_index +1) % len(values)] += share_value

    return values


values = [0, 1000, 800, 0]
print(fair_sharer(values, 3))