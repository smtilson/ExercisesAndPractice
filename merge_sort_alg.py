
def sort(sample_list):
    if len(sample_list) == 1:
        return sample_list
    part_1 = sample_list[:len(sample_list)//2]
    part_2 = sample_list[len(sample_list)//2:]
    print(f"We split {sample_list} into the two parts: {part_1} and {part_2}")
    new_part_1 = sort(part_1)
    new_part_2 = sort(part_2)
    new_list = merge(new_part_1, new_part_2)
    print(f"{new_list} is now sorted.")
    return new_list


def merge(sample_1, sample_2):
    new_list = []
    print(f"We now wish to merge {sample_1} and {sample_2}.")
    while len(sample_1)>0 and len(sample_2)>0:
        if sample_1[0]>=sample_2[0]:
            if len(sample_2)>1:
                print(f"we remove {sample_2[0]} from {sample_2} and add it to {new_list}")
            new_list.append(sample_2.pop(0))
        else:
            if len(sample_1) > 1:
                print(f"we remove {sample_1[0]} from {sample_1} and add it to {new_list}")
            new_list.append(sample_1.pop(0))
    if sample_1:
        if len(sample_1) > 1 and len(new_list) < 1:
            print(f"Finally, we extend {new_list} by {sample_1} to finish the merge.")
        new_list.extend(sample_1)
        print(f"Thus we obtain {new_list}")
    else:
        if len(sample_2)>1 and len(new_list)<1:
            print(f"Finally, we extend {new_list} by {sample_2} to finish the merge.")
        new_list.extend(sample_2)
        print(f"Thus we obtain {new_list}")
    return new_list

test = [12,3,123,4,123,465,56,234,65471,2,4,2,6,]
type([])
sort(test)
new_test = [14,23,15,234,16,6]
new_test_1, new_test_2 = [14,23,15],[234,16,6]
new_test_1, new_test_2 = [14,15,23],[6,16,234]
merged =[6,14,15,16,23, 234]