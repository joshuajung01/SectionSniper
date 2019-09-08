def find_avai_class(data, dept, class_num):
    """
    Takes in a given data set and a class.
    Returns an array of the classes that are open of a specific type.
    """
    arr = []
    temp_arr = data["data"]
    for c_ass in temp_arr:
        for key in c_ass:
            if key == "openSection" and c_ass[key] == True:
                arr.append(dept + " " + class_num + " " + c_ass["sequenceNumber"])
    return arr

def find_all_class(data, dept, class_num):
    """
    Takes in a given data set and a class.
    Returns an array of the classes that are open of a specific type.
    """
    arr = []
    temp_arr = data["data"]
    for c_ass in temp_arr:
        for key in c_ass:
            if key == "openSection":
                arr.append(dept + " " + class_num + " " + c_ass["sequenceNumber"])
    return arr

def check_class(fullname, arr):
    """
    Takes in the full name of a specific class and an array of the available open classes. Ex: MATH 251 509
    Returns Boolean variable to see if the specific class is open
    """
    if fullname in arr:
        return True
    else:
        return False