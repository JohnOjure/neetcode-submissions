class Solution:
    lnd, ek, sfl, table = [], {}, None, None

    def encode(self, strs: List[str]) -> str:
        fl = "".join(strs)
        self.sfl = list(set(fl))

        self.lnd = [len(subl) for subl in strs]

        for i in range(1, len(self.lnd)): self.lnd[i] += self.lnd[i-1]  

        for i, elem in enumerate(self.sfl): self.ek[elem] = self.sfl[len(self.sfl)-i-1]

        self.table = str.maketrans(self.ek)
        return fl.translate(self.table)

    def decode(self, s: str) -> List[str]:
        d_s = s.translate(self.table)

        return [d_s[i:j] for i, j in zip([0] + self.lnd[:-1], self.lnd)]