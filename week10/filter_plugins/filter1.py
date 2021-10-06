# 3 Functions - one for each filter
def filter1(a_string):
    return a_string.upper()

def filter2(a_string):
    return a_string.lower()

def filter3(a_string):
    return a_string.capitalize()

# Boilerplate Class and method
class FilterModule(object):
    def filters(self):

        return {"Filter1": filter1,
                "Filter2": filter2,
                "Filter3": filter3
        }