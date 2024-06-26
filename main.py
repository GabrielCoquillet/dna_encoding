# A --> 00
# T --> 11
# c --> 01
# G --> 10

class TO_DNA:

    def bin_to_dna(self,Bin):
        Dna = ''
        for i in range(0, len(Bin), 2):
            if Bin[i] != '0' and Bin[i] != '1':
                return False
            if Bin[i + 1] != '0' and Bin[i + 1] != '1':
                return False
            if Bin[i] == '0':
                if Bin[i + 1] == '1':
                    Dna = Dna + 'C'
                if Bin[i + 1] == '0':
                    Dna = Dna + 'A'
            if Bin[i] == '1':
                if Bin[i + 1] == '1':
                    Dna = Dna + 'T'
                if Bin[i + 1] == '0':
                    Dna = Dna + 'G'
        return Dna

    def txt_to_bin(self,txt):
        binaire = ''
        binary = ''
        for lettre in txt:
            b = str(bin(ord(lettre)))
            for i in range(2, len(b)):
                binary = binary + b[i]
            binaire = binaire + binary
        for i in range(8):
            if len(binaire) % 8 != 0:
                binaire = '0' + binaire
        return binaire

    def txt_to_dna(self,txt):
        Dna = ''
        bin = 0
        for elt in txt:
            bin = self.txt_to_bin(elt)
            Dna = Dna + self.bin_to_dna(bin)
        return Dna


class To_Txt:

    def dna_to_txt(self,Dna):
        bin = self.dna_to_bin(Dna)
        txt = self.bin_to_txt(bin)
        return txt

    def dna_to_bin(self,Dna):
        bin = ''
        for i in range(len(Dna)):
            if Dna[i] == 'A':
                bin = bin + '00'
            elif Dna[i] == 'T':
                bin = bin + '11'
            elif Dna[i] == 'C':
                bin = bin + '01'
            elif Dna[i] == 'G':
                bin = bin + '10'
        return bin

    def bin_to_txt(self,Bin):
        txt = ''
        cpt = 0
        for i in range(0, len(Bin) // 8):
            bin = '0b' + Bin[cpt:8 + cpt]
            ord = int(bin, 2)
            txt += chr(ord)
            cpt += 8
        return txt