def generate_truthtable(number_of_variables=0):
    if number_of_variables == 0:
        return "You need to enter an integer"
    else:
        total_combinations = 2**number_of_variables
        combinations_list = []
        for i in range(total_combinations):
            bin_equivalent = bin(i)[2:]
            while len(bin_equivalent)<number_of_variables:
                bin_equivalent = "0" + bin_equivalent
            combinations_list.append(tuple(int(val)for val in bin_equivalent))
        return combinations_list

print(generate_truthtable())

def evaluate_propositional_logic(c_list):
    print("A B C Result")
    for combination in c_list:
        A, B, C = combination
        # Example logic: (A AND B) OR C
        result = int((A and B) or C)
        print(f"{A} {B} {C} {result}")
        
evaluate_propositional_logic(generate_truthtable(3))