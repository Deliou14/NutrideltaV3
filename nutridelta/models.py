import datetime

from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth.models import User


class Profile(models.Model):
    user=models.IntegerField()
    identifiant=models.IntegerField()




# Besoin officiels en vitamines selon sexe, age ,lactation et grossesse
class Anc(models.Model):
    anc_vitamineA = models.FloatField()
    anc_vitamineC = models.FloatField()
    anc_vitamineD = models.FloatField()
    anc_vitamineE = models.FloatField()
    anc_vitamineK1 = models.FloatField()
    anc_vitamineK2 = models.FloatField()
    anc_vitamineB1 = models.FloatField()
    anc_vitamineB2 = models.FloatField()
    anc_vitamineB3 = models.FloatField()
    anc_vitamineB5 = models.FloatField()
    anc_vitamineB6 = models.FloatField()
    anc_vitamineB8 = models.FloatField()
    anc_vitamineB9 = models.FloatField()
    anc_vitamineB12 = models.FloatField()
    anc_calcium = models.FloatField()
    anc_cuivre = models.FloatField()
    anc_fer = models.FloatField()
    anc_iode = models.FloatField()
    anc_magnesium = models.FloatField()
    anc_manganese = models.FloatField()
    anc_phosphore = models.FloatField()
    anc_potassium = models.FloatField()
    anc_selenium = models.FloatField()
    anc_zinc = models.FloatField()

    type_sexe = models.FloatField()
    age_from = models.FloatField()
    age_to = models.FloatField()
    lactation = models.FloatField()
    grossesse = models.FloatField()


# Influence du sport sur la depense calorique
class Sport(models.Model):
    name = models.CharField(max_length=100)
    depense_energetique = models.FloatField()

    def __str__(self):
        return self.name


# quantite en vitamine pour une categorie d'aliment donnée
class Category_Aliment(models.Model):
    name = models.CharField(max_length=100)
    poid_portion = models.FloatField()

    vitamineA = models.FloatField()
    vitamineC = models.FloatField()
    vitamineD = models.FloatField()
    vitamineE = models.FloatField()
    vitamineK1 = models.FloatField()
    vitamineK2 = models.FloatField()
    vitamineB1 = models.FloatField()
    vitamineB2 = models.FloatField()
    vitamineB3 = models.FloatField()
    vitamineB5 = models.FloatField()
    vitamineB6 = models.FloatField()
    vitamineB8 = models.FloatField()
    vitamineB9 = models.FloatField()
    vitamineB12 = models.FloatField()
    calcium = models.FloatField()
    cuivre = models.FloatField()
    fer = models.FloatField()
    iode = models.FloatField()
    magnesium = models.FloatField()
    manganese = models.FloatField()
    phosphore = models.FloatField()
    potassium = models.FloatField()
    selenium = models.FloatField()
    zinc = models.FloatField()


# pourcentage pour un utilisateur, pour un microNutriment
class Pourcentage_microNutri_user(models.Model):
    user_id = models.IntegerField()
    microNutri = models.CharField(max_length=100)
    pourcentage_satisfait = models.IntegerField()


# prescription->nb de pillules pour un microNutriment
class Prescription_microNutri_user(models.Model):
    id_utilisateur = models.IntegerField()
    vitamineA = models.FloatField()
    vitamineC = models.FloatField()
    vitamineD = models.FloatField()
    vitamineE = models.FloatField()
    vitamineK1 = models.FloatField()
    vitamineK2 = models.FloatField()
    vitamineB1 = models.FloatField()
    vitamineB2 = models.FloatField()
    vitamineB3 = models.FloatField()
    vitamineB5 = models.FloatField()
    vitamineB6 = models.FloatField()
    vitamineB8 = models.FloatField()
    vitamineB9 = models.FloatField()
    vitamineB12 = models.FloatField()
    calcium = models.FloatField()
    cuivre = models.FloatField()
    fer = models.FloatField()
    iode = models.FloatField()
    magnesium = models.FloatField()
    manganese = models.FloatField()
    phosphore = models.FloatField()
    potassium = models.FloatField()
    selenium = models.FloatField()
    zinc = models.FloatField()


class MicroNutriment(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Objectif(models.Model):
    name = models.CharField(max_length=100)
    image_name = models.CharField(max_length=100, default="")
    def __str__(self):
        return self.name



# QUESTIONS

class ObjectifQuestion(models.Model):
    name = models.CharField(max_length=100)
    objectif = models.ForeignKey(Objectif, on_delete=models.CASCADE)
    def __str__(self):
        return '%s %s %s' % (self.id, self.name, self.objectif)


class LinkObjectifMicro(models.Model):
    objectif = models.ForeignKey(Objectif, on_delete=models.CASCADE)
    microNutriment = models.ForeignKey(MicroNutriment, on_delete=models.CASCADE)
    def __str__(self):
        return '%s %s' % (self.objectif, self.microNutriment)


class MicroQuestion(models.Model):
    name = models.CharField(max_length=100)
    microNutriment = models.ForeignKey(MicroNutriment, on_delete=models.CASCADE)
    def __str__(self):
        return self.name



# REPONSES
class Regime(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return  self.name


class ObjectifChoice(models.Model):
    user_id = models.IntegerField()
    objectif = models.ForeignKey(Objectif, on_delete=models.CASCADE)


    

class ReponseProfil(models.Model):
    @classmethod
    def create(cls, user_id):
        cls(user_id = user_id)
        return ReponseProfil

    TAILLE_CHOICES = [(i, i) for i in range(30, 220)]
    AGE_CHOICES = [(i, i) for i in range(0, 110)]
    POID_CHOICES = [(i, i) for i in range(2, 200)]

    user_id = models.IntegerField()
    age = models.IntegerField(default = 40, choices=AGE_CHOICES)
    taille = models.IntegerField(default=170, choices=TAILLE_CHOICES)
    poid = models.IntegerField(default=70, choices=POID_CHOICES)
    sexe = models.BooleanField(default = True, help_text="True=Homme")
    enceinte = models.BooleanField(default=False)
    allaitante = models.BooleanField(default=False)
    regime = models.ForeignKey(Regime, on_delete=models.CASCADE, null= True)
    alcool = models.IntegerField(default = 0)
    cigarette = models.IntegerField(default = 0)

    date = models.DateField(auto_now=False, auto_now_add=True)
    last_modif = models.DateField(auto_now=True, auto_now_add=False)




class SportChoice(models.Model):
    user_id = models.IntegerField()
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    frequency = models.IntegerField(default = 0)

    def __str__(self):
        return '%s %s' % (self.user_id, self.name)


class ReponsesMicroQuestion(models.Model):
    user_id = models.IntegerField()
    question = models.ForeignKey(MicroQuestion, on_delete=models.CASCADE)
    value = models.FloatField()

    date = models.DateField(auto_now=False, auto_now_add=True)
    last_modif = models.DateField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return '%s %s' % (self.user_id, self.question)


class ReponsesObjectifQuestion(models.Model):
    user_id = models.IntegerField()
    question = models.ForeignKey(ObjectifQuestion, on_delete=models.CASCADE)
    value = models.IntegerField()

    date = models.DateField(auto_now=False, auto_now_add=True)
    last_modif = models.DateField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return '%s %s' % (self.user_id, self.question)


class ReponsesAlimentation(models.Model):
    user_id = models.IntegerField()
    Category_Aliment = models.ForeignKey(Category_Aliment, on_delete=models.CASCADE)
    value = models.FloatField()

    date = models.DateField(auto_now=False, auto_now_add=True)
    last_modif = models.DateField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return '%s %s' % (self.user_id, self.Category_Aliment)
