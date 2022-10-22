'''
Implement the IceCreamMachine's scoops method so that it returns all combinations of one ingredient and one topping. 
If there are no ingredients or toppings, the method should return an empty list.

For example, IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce"]).scoops() 
should return [['vanilla', 'chocolate sauce'], ['chocolate', 'chocolate sauce']].
'''
class IceCreamMachine:
    
    def __init__(self, ingredients, toppings):
        self.ingredients = ingredients
        self.toppings = toppings
        
    def scoops(self):
        result = []
        for sabor in self.ingredients:
            for toping in self.toppings:
                merge = []
                merge.append(sabor)
                merge.append(toping)
                result.append(merge)
        return result

machine = IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce", "vanilla sauce"])
print(machine.scoops()) #should print[['vanilla', 'chocolate sauce'], ['chocolate', 'chocolate sauce']]