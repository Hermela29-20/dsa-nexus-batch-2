class Solution(object):
    def convertTemperature(self, celsius):
        k=celsius+273.15
        f=celsius*1.8+32.00
        return [k,f]
        
