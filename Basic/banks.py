class Banks():
    
    def __init__(self,user):
        self.__name=user
        self.__balance=0
        self.__title='Taipei Bank'
        self.__rate=30
        self.__service_charge=0.01
    
    def save_money(self,money):
        self.__balance+=money
        print('Saving',money,'has completed.')
    
    def withdraw_money(self,money):
        self.__balance-=money
        print('Withdrawing',money,'has completed.')
    
    def get_balance(self):
        print(self.__name.title(),'has',self.__balance)
        
    def usa_to_taiwan(self,usa_dollar):
        self.result=self.__cal_rate(usa_dollar)
        return self.result
    
    def __cal_rate(self,usa_dollar):
        return int(usa_dollar*self.__rate*(1-self.__service_charge))
    
    def bank_title(self):
        return self.__title
    
class Daan_Banks(Banks):
    
    def __init__(self,user):
        self.title='Taipei Bank - Daan Branch'
    
    def bank_title(self):
        return self.title