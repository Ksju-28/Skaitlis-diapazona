#Izveidot funkciju, kas pārbauda, vai skaitlis atrodas lietotāja noteiktā diapazonā vai nē.
def noteiktDiapazonu(d1,d2,sk):
  rezultats = "Skaitlis nav diapozonā!"
  if d1>=sk<=d2:
    rezultats = "Skaitlis ir diapozonā!"
  return rezultats

d1 = int(input("Ievadi diapozona sākumu: "))
d2 = int(input("Ievadi diapozona beigas: "))
sk = int(input("Ievadi skaitli: "))
rez = noteiktDiapazonu(d1,d2,sk)
print(rez)