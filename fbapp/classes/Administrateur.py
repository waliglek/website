from Utilisateur import Utilisateur

class Administrateur(Utilisateur):

    def __init__(self, nom_utilisateur="", nom="", prenom="", motdepasse="", sexe="" ):
        Utilisateur.__init__(self,nom_utilisateur,nom,prenom,motdepasse,sexe)

'''
    def addSeance(seance=Seance, day=Day):
        return 0;

    def removeSeance(seance=Seance, day=Day):
        return 0;

    def modifySeance(seance=Seance):
        return 0;
    
    def addExo(exo=Exo, day=Day):
        return 0;

    def removeExo(exo=Exo, day=Day):
        return 0;
    
    def modifyExo(exo=Exo):
        return 0;
'''  