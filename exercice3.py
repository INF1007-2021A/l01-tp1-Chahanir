
def decomposer(secondes):

    # TODO: Assigner à la variable "annees" le nombre d'années
    annees = (secondes/(365*24*60*60))
    secondes_restantes_apres_annees = (annees-int(annees))*(365*24*60*60)
    # TODO: Assigner à la variable "semaines" le nombre de semaines restantes
    semaines = (secondes_restantes_apres_annees/(7*24*60*60))
    secondes_restantes_apres_semaines = (semaines - int(semaines))*(7*24*60*60)
    # TODO: Assigner à la variable "jours" le nombre de jours restants
    jours = (secondes_restantes_apres_semaines/(24*60*60))
    secondes_restantes_apres_jours = (jours - int(jours))*(24*60*60)

    # TODO: Assigner à la variable "heures" le nombre d'heures restantes
    heures = (secondes_restantes_apres_jours/(60*60))
    secondes_restantes_apres_heures = (heures - int(heures))*(60*60)

    # TODO: Assigner à la variable "minute" le nombre de minutes restantes
    minutes = (secondes_restantes_apres_heures)/60
    secondes_restantes_apres_minutes = (minutes - int(minutes))*60

    # TODO: Assigner à la variable "secondes" le nombre de secondes restantes
    secondes = secondes_restantes_apres_minutes

    # TODO: Afficher le nombres d'années, semaines, jours, heures, minutes et secondes
    print(annees ,semaines ,jours ,heures ,minutes ,secondes)

    return (int(annees) ,int(semaines) ,int(jours) ,int(heures), int(minutes), int(secondes))

if __name__ == '__main__':
    secondes = int(input("Entrer les secondes: "))
    print(decomposer(secondes))
