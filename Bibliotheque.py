from Livre import Livre
from Utilisateur import Utilisateur

class Bibliotheque:
    def __init_(self):
        self.livres = []
        self.utilisateurs = []

    def ajouter_livre(self, titre, auteur, isbn):
        livre = Livre(titre, auteur, isbn)
        self.livres.append(livre)
        print("Livre ajouté avec succès.")

    def enregistrer_utilisateur(self, nom, identifiant):
        utilisateur = Utilisateur(nom, identifiant)
        self.utilisateurs.append(utilisateur)
        print("Utilisateur enregistré.")

    def lister_livres(self, uniquement_disponibles=False):
        for livre in self.livres:
            if not uniquement_disponibles or livre.est_disponible():
                livre.afficher_info()

    def trouver_livre(self, isbn):
        for livre in self.livres:
            if livre.get_isbn() == isbn:
                return livre
        return None

    def trouver_utilisateur(self, identifiant):
        for utilisateur in self.utilisateurs:
            if utilisateur.identifiant == identifiant:
                return utilisateur
        return None