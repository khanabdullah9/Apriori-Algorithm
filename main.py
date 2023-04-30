import datasets
import apriori

if __name__ == "__main__":

    algo = apriori.AprioriAlgorithm(
        min_support_threshold = 0,
        min_conf_threshold = 0,
        dataset = datasets.get_dataset()
    )

    algo.run()
    
    
    