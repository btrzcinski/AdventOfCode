from numpy import matrix
from operator import itemgetter

def moves_from_x(x):
    for i in range(len(x)):
        for j in range(len(x)):
            if i < j:
                yield x[:i] + [x[i] + 1] + x[i+1:j] + [x[j] - 1] + x[j+1:]
            elif i > j:
                yield x[:j] + [x[j] - 1] + x[j+1:i] + [x[i] + 1] + x[i+1:]

def solve_for_x(fun, starting_x):
    x = starting_x.copy()
    solved = False
    while not solved:
        best_move = max([(move, fun(move)) for move in moves_from_x(x)], key=itemgetter(1))
        if best_move[1] <= fun(x):
            solved = True
        else:
            x = best_move[0]
    return x

# props = [[cap, dur, flav, text], [cap, dur, flav, text], ...]
def generate_score_objective_function_from_properties(props):
    return lambda x: (matrix(x) * matrix(props)).clip(min=0).prod()

def generate_calorie_objective_function_from_properties(props, cals, cal_ceiling):
    return lambda x: 0.000001*generate_score_objective_function_from_properties(props)(x) - abs(calories_for_x(x, cals) - cal_ceiling)

def evaluate_x_with_props(x, props):
    return generate_score_objective_function_from_properties(props)(x)

def solve_for_x_from_props(props):
    fun = generate_score_objective_function_from_properties(props)
    starting_x = [100 // len(props)] * len(props)
    starting_x[-1] += 100 % len(props)
    return solve_for_x(fun, starting_x)

def calories_for_x(x, cals):
    return (matrix(x)*matrix(cals).T)[0,0]

def solve_for_x_with_cal_penalty(props, cals, cal_ceiling):
    starting_x = solve_for_x_from_props(props)
    fun = generate_calorie_objective_function_from_properties(props, cals, cal_ceiling)
    return solve_for_x(fun, starting_x)

def main():
    ingredients = []
    cals = []
    with open("Day15.txt") as f:
        for line in f:
            # Sprinkles: capacity 2, durability 0, flavor -2, texture 0, calories 3
            _, _, cap, _, dur, _, flav, _, text, _, cal = [x.strip(",") for x in line.strip().split()]
            props = [int(x) for x in (cap, dur, flav, text)]
            ingredients.append(props)
            cals.append(int(cal))
    print("ingredients =", ingredients)
    print("cals =", cals)
    solution = solve_for_x_from_props(ingredients)
    score = evaluate_x_with_props(solution, ingredients)
    print("Solution:", solution)
    print("Score:", score)
    cal_solution = solve_for_x_with_cal_penalty(ingredients, cals, 500)
    cal_score = evaluate_x_with_props(cal_solution, ingredients)
    cal_solution_cals = calories_for_x(cal_solution, cals)
    print("Cals solution:", cal_solution)
    print("Cals score:", cal_score)
    print("Cals cals:", cal_solution_cals)

if __name__ == "__main__":
    main()
