def minimum_index(seq):
    if len(seq) == 0:
        raise ValueError("Cannot get the minimum value index from an empty sequence")
    min_idx = 0
    for i in range(1, len(seq)):
        if seq[i] < seq[min_idx]:
            min_idx = i
    return min_idx
class TestDataEmptyArray(object):
    
    @staticmethod
    def get_array():
        a = []
        return(a)

class TestDataUniqueValues(object):

    @staticmethod
    def get_array():
        return([1,2,3,4,5])

    @staticmethod
    def get_expected_result():
        return 0

class TestDataExactlyTwoDifferentMinimums(object):

    @staticmethod
    def get_array():
       return([9,0,0,4,7,2])

    @staticmethod
    def get_expected_result():
        return 1

