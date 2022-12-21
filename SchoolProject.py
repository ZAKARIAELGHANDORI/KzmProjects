class Niveau:
    def __init__(self, Nom):
        self.Nom = Nom

    def __str__(self):
        return 'le niveau est : ' + self.Nom


class etudiant:
    nbr_etu = -1
    nmbr=0

    def __init__(self, Nom, Sexe, Niveau):
        self.Nom = Nom
        self.Sexe = Sexe
        self.Niveau = Niveau

        etudiant.nbr_etu = etudiant.nbr_etu + 1

    def __str__(self):
        etudiant.nmbr+=1
        return f"le nom de l'etudiant {etudiant.nmbr} est : {self.Nom} et {self.Niveau} de sexe {self.Sexe} "


class Profsseur:
    nbr_prof = 0

    def __init__(self, Nom, Sexe, TarifHoraire):
        self.Nom = Nom
        self.Sexe = Sexe
        self.TarifHoraire = TarifHoraire
        Profsseur.nbr_prof += 1

    def __str__(self):
        return f"le professeur {self.Nom} de sexe {self.Sexe} pour un tarif d'horaire jusqu'a {self.TarifHoraire} "





class cours:
    def __init__(self, Nom, DateDebut, DateFin):
        self.Nom = Nom
        self.DateDebut = DateDebut
        self.DateFin = DateFin

    def __str__(self):
        return f"Pour le cour {self.Nom}  l'heure de commencement est {self.DateDebut} et pour l'heure de termination est {self.DateFin} "


class Class:
    def __int__(self, Nomc, Niveau):
        self.Nomc = Nomc
        self.Niveau = Niveau

    def __str__(self):
        return 'Pour la ' + self.Nomc

#### main

##Declararion des etudiant

E1 = etudiant("ZAKARIA", "MALE", Niveau("3éme année"))
E2 = etudiant("ANASS", "MALE", Niveau("3éme année"))
E3 = etudiant("ABDESAMAD", "MALE", Niveau("2éme année"))

#Declaration des professeurs

P1 = Profsseur("EZATI", "MALE", "300DH")
P2 = Profsseur("DOHA", "FEMALE", "350DH")
P3 = Profsseur("DAKIR", "MALE", "400DH")
P4 = Profsseur("BENMAKHLOUF", "MALE", "450DH")

#Declaration des cours

C1 = cours("JAVA", "16H00", "18H00")
C2 = cours("DATA BASES", "14H00", "15H45")
C3 = cours("WEB DEVELOPMENT", "10H00", "12H00")

##Declaration des class

Cl1 = Class()
Cl1.Nomc = "Class 1"
Cl1.Niveau = Niveau("3éme année ")

Cl2 = Class()
Cl2.Nomc = "Class 2"
Cl2.Niveau = Niveau("2éme année ")

print(f"le nombre d'etudiants de cette ecole est : {etudiant.nbr_etu}\n")
print(f"le nombre de professeurs de cette ecole est : {Profsseur.nbr_prof}\n")

print(f"{E1.Niveau} pour l'etudiant : {E1.Nom} \n")
print(f"{Cl1} {Cl1.Niveau} \n")


#parcourir les etudiants

cour=[C1 , C2 , C3]
for x in cour:
    print(f"{x}\n")
#parcourir les cours

etu=[E1 , E2 , E3]
for x in etu:
    print(f"{x}\n")

#parcourir les professeurs

prof=[P1 , P2 , P3, P4]
for x in prof:
    print(x)
#FINN
