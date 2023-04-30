class AprioriAlgorithm:
    def __init__(self,min_support_threshold,min_conf_threshold,dataset):
        self.min_conf_threshold = min_conf_threshold
        self.min_support_threshold = min_support_threshold
        self.items = []
        self.dataset = dataset
        self.k = 1

    """
    Creating itemsets of size 1 i.e the first candidate set
    params -> None
    returns -> void
    """
    def distinct_itemsets(self):
        items = self.dataset['items']
        for item in items:
            if item not in self.items:
                self.items.append(item)

    """
    Making candidate set iteratively
    params -> None
    returns -> <list>candidate set
    """
    def make_candidate_sets(self):
        pass
                    

    """
    Return the max value of k
    """
    def get_max_k():
        pass

    """
    Making item set
    params -> <str>item : item
              <str>other_item : item
    returns -> <str>item set
    """
    def make_itemset(self,item, other_item):
        return str(item +" "+other_item)

    """
    Checks if the itemset belongs to any row in the dataset
    params -> <str>item_set : item set
    returns -> <bool>
    """
    def is_valid_itemset(self, item_set):
        isValid = False
        
        for row in self.dataset["items"]:
            if self.row_contains_all(row, item_set):
                isValid = True
                print(row)
                break

        return isValid
    
    """
    Checks whether certain row contains all the items
    params -> <str>row : dataset row
              <str>item_set : item set
    returns -> <bool>
    """
    def row_contains_all(self,row,item_set):
        lst = []
        
        for item in item_set.split(" "):
            if item in row:
                lst.append(True)
            else:
                lst.append(False)
        return not lst.__contains__(False)

    def print_candidate_set(self,candidate_set):
        for item in candidate_set:
            print(item)

    def run(self):
        # self.distinct_itemsets()
        # candidate_set = []
        # self.print_candidate_set(self.make_candidate_sets())
        
        isValid = self.is_valid_itemset("I1 I2 I5")
        print(isValid)
        
