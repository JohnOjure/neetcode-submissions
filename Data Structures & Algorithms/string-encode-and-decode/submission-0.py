class Solution:
    
    lnd = []
    ek = {}
    sfl = None
    table = None

    def encode(self, strs: List[str]) -> str:
        fl = "".join(strs)
        self.sfl = list(set(fl))
        print(self.sfl)
        lsfl = len(self.sfl)

        self.lnd = [len(subl) for subl in strs]
        print(self.lnd)

        for i in range(1, len(self.lnd)): #build lnd
            self.lnd[i] += self.lnd[i-1]  
        # self.lnd[0] -= 1
        # self.lnd = self.lnd[:-1]
        print(self.lnd)

        for i, elem in enumerate(self.sfl): #build ek
            self.ek[elem] = self.sfl[lsfl-i-1]
        print(self.ek)

        self.table = str.maketrans(self.ek)
        e_fl = fl.translate(self.table) #encoding
        
        print(e_fl)
        return e_fl



    def decode(self, s: str) -> List[str]:
        d_s = s.translate(self.table)
        print(d_s)

        return [d_s[i:j] for i, j in zip([0] + self.lnd[:-1], self.lnd)]

        


