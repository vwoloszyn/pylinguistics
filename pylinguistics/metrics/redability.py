 def redability(self): 
        return min(self.calc_flesch_kincaid_grade(), self.calc_coleman_liau_index())

    def calc_coleman_liau_index (self):
        texto = self.text.decode('utf-8')
        x=0
        try:
            x= textstat.coleman_liau_index(texto)
        except:
            x=0
        return x

    def calc_flesch_kincaid_grade (self):
        texto = self.text.decode('utf-8')
        x=0
        try:
            ASL = textstat.avg_sentence_length(texto)
            ASW = textstat.avg_syllables_per_word(texto)
            FKRA = float(0.39 * ASL) + float(11.8 * ASW) - 15.59
            x= round(FKRA, 1)
        except:
            x=0
        return x
