class bil (): 
  hjul=4
  bilräkning=0
  def __init__(self, model, pris):
        self.model = model
        self.pris = pris
        self.utrustning = []

        bil.bilräkning += 1
  def  visabil (self):
        print(f"Model: {self.model}, Pris: {self.pris}") 
  
  def minpris(aPrice):
    return int(aPrice * 0.66)
  
  def __add__(self, other):
        return self.pris + other.pris
  
  def merutrustning(self, nyutrustning ):
        self.utrustning.append(nyutrustning)
  
  def __lt__(self, other):
    print(f'Är {other.model} dyrare än {self.model}?')
    return self.pris< other.pris
  
  def __eq__(self, other):
    print(f'kostar {other.model} lika mycket som {self.model}?')
    return self.pris==other.pris
    
    




Saab=bil('Saab9000',900000)
BMW=bil('BMW',700000)
print(BMW==Saab) 