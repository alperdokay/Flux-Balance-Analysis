# Author : Alper Dokay

# Flux Balance Analysis

reaction_scores = {'R1':3, 'R2': 4, 'R3': 5}
upper_bounds = {'R1': 9, 'R2': 16, 'R3': 25}
lower_bounds = {'R1': 0.775, 'R2': 0.875, 'R3': 0.975}

def minimize_upper_bound(r_scores, u_bounds):
    """ 
        params:
            - r_scores : Reaction scores - type(dict) { [reaction_name]: [score]}
            - u_bounds : Upper bounds - type(dict) { [reaction_name]: [upper_bound_score]}
        desc:
            - minimization of upper bound scores
                * returns minimized upper bounds - type(dict)
    """
    minimized = {}
    for r in r_scores:
        minimized[r] = u_bounds[r] - r_scores[r]
    return minimized

def minimize_lower_bound(r_scores, l_bounds):
    """ 
        params:
            - r_scores : Reaction scores - type(dict) { [reaction_name]: [score]}
            - l_bounds : Lower bounds - type(dict) { [reaction_name]: [upper_bound_score]}
        desc:
            - minimization of lower bound scores
                * returns minimized lower bounds - type(dict)
    """
    minimized = {}
    for r in r_scores:
        minimized[r] = r_scores[r] - l_bounds[r]
    return minimized

print(minimize_upper_bound(reaction_scores, upper_bounds))
print(minimize_lower_bound(reaction_scores, lower_bounds))