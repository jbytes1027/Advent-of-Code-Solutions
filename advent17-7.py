from statistics import mode
log = []
tree = []

# parse log
for line in open("advent/input.txt"):
    line = line.replace(",","").rstrip().split()
    
    new_log_line = {
        "name": line[0],
        "weight": int(line[1][1:-1]),
        "branches":[]
    }

    tree.append(dict(new_log_line))

    if "->" in line:
        new_log_line["branch_names"] = line[line.index("->")+1:]
    
    log.append(dict(new_log_line))


def get_branch_cumulative_weight(branch):
    # get all siblings
    if len(branch["branches"]) == 0:
        return branch["weight"]

    total = 0
    for child in branch["branches"]:
        total += get_branch_cumulative_weight(child)
    total += branch["weight"]
    
    return total


def find_corrected_wrong_child_weight(parent_branch, expected_parent_weight=0):
    child_weights = []
    for child_branch in parent_branch["branches"]:
        child_weights.append(get_branch_cumulative_weight(child_branch))
    
    expected_child_weight_cumulative = mode(child_weights)# (get_branch_cumulative_weight(parent_branch) - parent_branch["weight"]) / len(parent_branch["branches"])

    # is problem parent weight or a child weight
    # check children
    for child_branch in parent_branch["branches"]:
        child_weight_cumulative = get_branch_cumulative_weight(child_branch)

        if child_weight_cumulative != expected_child_weight_cumulative: # if problem is child
            return find_corrected_wrong_child_weight(child_branch, expected_child_weight_cumulative) # find problem in child

    # problem is current branch weight
    return (expected_parent_weight - get_branch_cumulative_weight(parent_branch)) + parent_branch["weight"]


def find_branch(l, name):
    for branch in l:
        if branch["name"] == name:
            return branch
        
        found = find_branch(branch["branches"],name)
        if found != None:
            return found


# assemble tree
for line in log:
    if "branch_names" not in line:
        continue
    
    for child_name in line["branch_names"]:
        child = find_branch(tree, child_name)
        parent = find_branch(tree, line["name"])
        parent["branches"].append(dict(child))
        tree.remove(child)


for i in tree:
    print(find_corrected_wrong_child_weight(i))
    # print(i,"\n")