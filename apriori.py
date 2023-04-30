class AprioriAlgorithm:
    def __init__(self,min_support_threshold,min_conf_threshold,dataset):
        self.min_conf_threshold = min_conf_threshold
        self.min_support_threshold = min_support_threshold
        self.items = []
        self.dataset = dataset
        self.k = 1

    def distinct_itemsets(self):
        items = self.dataset['items']
        for item in items:
            if item not in self.items:
                self.items.append(item)


    def make_candidate_sets(self):
        candidate_set = []
        for item in self.items:
            for other_item in self.items:

                if item != other_item:
                    item_set = self.make_itemset(item, other_item)

                    if self.is_valid_itemset(item_set) and item_set not in candidate_set:
                        candidate_set.append(item_set)

        return candidate_set
                    

    """
    Return the max value of k
    """
    def get_max_k():
        pass

    def make_itemset(self,item, other_item):
        return str(item +" "+other_item)

    def is_valid_itemset(self, item_set):
        isValid = False
        
        for row in self.dataset["items"]:
            if self.row_contains_all(row, item_set):
                isValid = True
                print(row)
                break

        return isValid
    
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
        
