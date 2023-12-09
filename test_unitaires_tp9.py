from unittest import TestCase
from calcul import Fraction


class TestFraction(TestCase):
    def test___init__(self):
        frac0 = Fraction()
        frac1 = Fraction(1, 2)
        frac2 = Fraction(50, 25)
        frac3 = Fraction(1, -2)
        frac4 = Fraction(-1, 2)
        frac5 = Fraction(-1, -2)
        frac6 = Fraction(0, 10)
        #frac7 = Fraction(10, 0)

        #Par défaut
        self.assertEqual(frac0.numerateur, 0, "__init__ : Numérateur Par défaut")
        self.assertEqual(frac0.denominateur, 1, "__init__ : Dénominateur par défaut")
        #Basique
        self.assertEqual(frac1.numerateur, 1, "__init__ : Numérateur Basique")
        self.assertEqual(frac1.denominateur, 2, "__init__ : Dénominateur Basique")
        #Grande valeurs
        self.assertEqual(frac2.numerateur, 2, "__init__ : Numérateur Grande valeurs")
        self.assertEqual(frac2.denominateur, 1, "__init__ : Dénominateur Grande valeurs")
        #dénominateur négatif
        self.assertEqual(frac3.numerateur, -1, "__init__ : Numérateur, dénominateur négatif")
        self.assertEqual(frac3.denominateur, 2, "__init__ : Dénominateur, dénominateur négatif")
        # numérateur négatif
        self.assertEqual(frac4.numerateur, -1, "__init__ : Numérateur, Numérateur négatif")
        self.assertEqual(frac4.denominateur, 2, "__init__ : Dénominateur, Numérateur négatif")
        # numérateur et dénominateur négatif
        self.assertEqual(frac5.numerateur, 1, "__init__ : Numérateur avec numérateur et dénominateur négatif")
        self.assertEqual(frac5.denominateur, 2, "__init__ : dénominateur avec numérateur et dénominateur négatif")
        #numérateur nul
        self.assertEqual(frac6.numerateur, 0, "__init__ : Numérateur nul")
        self.assertEqual(frac6.denominateur, 1, "__init__ : Dénominateur avec numérateur nul")
        #Diviseur 0 RAISES
        self.assertRaises(ZeroDivisionError, Fraction, 10, 0)
        #un élément n'est pas un entier TypeError
        self.assertRaises(TypeError, Fraction, "a", 2)




    def test___str__(self):
        frac0 = Fraction()
        frac1 = Fraction(1, 2)
        frac2 = Fraction(50, 25)
        frac3 = Fraction(1, -2)
        frac4 = Fraction(-1, 2)
        frac5 = Fraction(-1, -2)
        frac6 = Fraction(0, 10)


        #Par défaut
        self.assertEqual(frac0.__str__(), "0", "__str__ : Numérateur Par défaut")
        #Basique
        self.assertEqual(frac1.__str__(), "1/2", "__str__ : Numérateur Basique")
        #Grande valeurs
        self.assertEqual(frac2.__str__(), "2", "__str__ :  Grande valeurs")
        #dénominateur négatif
        self.assertEqual(frac3.__str__(), "-1/2", "__str__ : dénominateur négatif")
        # numérateur négatif
        self.assertEqual(frac4.__str__(), "-1/2", "__str__ : Numérateur négatif")
        # numérateur et dénominateur négatif
        self.assertEqual(frac5.__str__(), "1/2", "__str__ : numérateur et dénominateur négatif")
        # numérateur nul
        self.assertEqual(frac6.__str__(), "0", "__str__ : Numérateur nul")

    def test_as_mixed_number(self):
        frac0 = Fraction()
        frac1 = Fraction(3, 2)
        frac2 = Fraction(70, 20)
        frac3 = Fraction(1, -2)
        frac4 = Fraction(-1, 2)
        frac5 = Fraction(-1, -2)
        frac6 = Fraction(0, 10)

        #Par défaut
        self.assertEqual(frac0.as_mixed_number(), "0", "as_mixed_number : test par défaut")
        #Basique
        self.assertEqual(frac1.as_mixed_number(), "1 et 1/2", "as_mixed_number : test faction basique")
        #Grande valeurs
        self.assertEqual(frac2.as_mixed_number(), "3 et 1/2", "as_mixed_number : test grande fraction")
        #dénominateur négatif
        self.assertEqual(frac3.as_mixed_number(), "-1 et 1/2", "as_mixed_number : test avec un numérateur négatif")
        # numérateur négatif
        self.assertEqual(frac4.as_mixed_number(), "-1 et 1/2", "as_mixed_number : test avec un dénominateur négatif")
        # numérateur et dénominateur négatif
        self.assertEqual(frac5.as_mixed_number(), "1/2","as_mixed_number : test normal avec un dénominateur et numérateur négatif")
        # numérateur nul
        self.assertEqual(frac6.as_mixed_number(), "0", "as_mixed_number : test avec un numérateur nul")

    def test___add__(self):
        frac0 = Fraction()
        frac1 = Fraction(1, 2)
        frac2 = Fraction(70, 20)
        frac3 = Fraction(1, -2)
        frac4 = Fraction(-1, 2)
        frac5 = Fraction(-1, -2)
        frac6 = Fraction(0, 10)
        frac7 = Fraction(-0, 10)
        frac8 = Fraction(0, 10)
        frac9 = Fraction(0, 10)

        other0 = Fraction()
        other1 = Fraction(3, 4)
        other2 = Fraction(220, 5)
        other3 = Fraction(3, 4)
        other4 = Fraction(3, 4)
        other5 = Fraction(-3, -4)
        other6 = Fraction(3, 4)
        other7 = Fraction(3, 4)
        other8 = Fraction(3, -4)
        other9 = Fraction(-3, 4)

        #Par défaut
        self.assertEqual(frac0.__add__(other0).__str__(), "0", "__add__ : Par défaut")
        #Basique
        self.assertEqual(frac1.__add__(other1).__str__(), "5/4", "__add__ : Basique")
        #Grande valeurs
        self.assertEqual(frac2.__add__(other2).__str__(), "95/2", "__add__ : Grande valeurs")
        #dénominateur négatif
        self.assertEqual(frac3.__add__(other3).__str__(), "1/4", "__add__ :dénominateur négatif")
        # numérateur négatif
        self.assertEqual(frac4.__add__(other4).__str__(), "1/4","__add__ : numérateur négatif")
        # numérateur et dénominateur négatif
        self.assertEqual(frac5.__add__(other5).__str__(), "5/4","__add__ : numérateur et dénominateur négatif")
        # numérateur nul
        self.assertEqual(frac6.__add__(other6).__str__(), "3/4", "__add__ : numérateur nul")
        # numérateur nul avec signe - devant le 0
        self.assertEqual(frac7.__add__(other7).__str__(), "3/4", "__add__ : numérateur nul avec signe - devant le 0")
        # numérateur nul avec - au dénominateur
        self.assertEqual(frac8.__add__(other8).__str__(), "-3/4", "__add__ : numérateur nul avec - au dénominateur")
        # numérateur nul avec - au numérateur
        self.assertEqual(frac9.__add__(other9).__str__(), "-3/4", "__add__ : numérateur nul avec - au numérateur")





    def test___truediv__(self):
        frac0 = Fraction()
        frac1 = Fraction(1, 2)
        frac2 = Fraction(70, 20)
        frac3 = Fraction(1, -2)
        frac4 = Fraction(-1, 2)
        frac5 = Fraction(-1, -2)
        frac6 = Fraction(-1, 2)
        frac7 = Fraction(0, 10)
        frac8 = Fraction(1, 2)
        frac9 = Fraction(1, 2)
        frac10 = Fraction(0, 10)
        frac11 = Fraction(0, 10)

        other0 = Fraction()
        other1 = Fraction(3, 4)
        other2 = Fraction(220, 5)
        other3 = Fraction(3, 4)
        other4 = Fraction(3, 4)
        other5 = Fraction(-3, -4)
        other6 = Fraction(-3, -4)
        other7 = Fraction(3, 4)
        other8 = Fraction(0, 4)
        other9 = Fraction(0, -4)
        other10 = Fraction(3, -4)
        other11 = Fraction(-3, 4)

        # Par défaut
        self.assertRaises(ZeroDivisionError, frac0.__truediv__, other0)
        #  division basique
        self.assertEqual(frac1.__truediv__(other1).__str__(), "2/3", "__truediv__ : Division basique")
        #  division avec de grandes valeurs
        self.assertEqual(frac2.__truediv__(other2).__str__(), "7/88", "__truediv__ : Grande valeurs")
        #  dénominateur négatif
        self.assertEqual(frac3.__truediv__(other3).__str__(), "-2/3", "__truediv__ : Dénominateur négatif")
        #  numérateur négatif
        self.assertEqual(frac4.__truediv__(other4).__str__(), "-2/3", "__truediv__ : Numérateur négatif")
        # numérateur et dénominateur négatifs
        self.assertEqual(frac5.__truediv__(other5).__str__(), "2/3","__truediv__ : Numérateur et dénominateur négatifs")
        self.assertEqual(frac6.__truediv__(other6).__str__(), "-2/3","__truediv__ : Numérateur et dénominateur négatifs")
        # numérateur nul
        self.assertEqual(frac7.__truediv__(other7).__str__(), "0", "__truediv__ : Numérateur nul")
        # division par zéro RAISES
        self.assertRaises(ZeroDivisionError, frac8.__truediv__, other8)
        self.assertRaises(ZeroDivisionError, frac9.__truediv__, other9)
        # numérateur nul
        self.assertEqual(frac10.__truediv__(other10).__str__(), "0", "__truediv__ : Numérateur nul")
        self.assertEqual(frac11.__truediv__(other11).__str__(), "0", "__truediv__ : Numérateur nul")


    def test___eq__(self):
        frac0 = Fraction()
        frac1 = Fraction(1, 2)
        frac2 = Fraction(1,2 )
        frac3 = Fraction(1, 2)
        frac4 = Fraction(1, -2)
        frac5 = Fraction(-1, 2)
        frac6 = Fraction(-1, 2)
        frac7 = Fraction(-1, -2)
        frac8 = Fraction(0, 10)
        frac9 = Fraction(0, 10)
        frac10 = Fraction(0, 10)
        frac11= Fraction(0, 10)
        frac12= Fraction(0, 10)

        other0 = Fraction()
        other1 = Fraction(1, 2)
        other2 = Fraction(3, 4)
        other3 = Fraction(25, 50)
        other4 = Fraction(1, 2)
        other5 = Fraction(1, 2)
        other6 = Fraction(1, -2)
        other7 = Fraction(-1, -2)
        other8 = Fraction(1, 2)
        other9 = Fraction(-1, -10)
        other10 = Fraction(0, 2)
        other11 = Fraction(1, -10)
        other12 = Fraction(-1, 10)

        # Par défaut
        self.assertEqual(frac0.__eq__(other0), True, "__eq__ : par défaut")
        # Fraction basique
        self.assertEqual(frac1.__eq__(other1), True, "__eq__ : Fraction basique")
        # Fraction basique
        self.assertEqual(frac2.__eq__(other2), False, "__eq__ : Fraction basique")
        # Grandes valeurs
        self.assertEqual(frac3.__eq__(other3), True, "__eq__ : dénominateur négatif")
        # Numérateur et dénominateur négatifs
        self.assertEqual(frac4.__eq__(other4), False, "__eq__ : numérateur et dénominateur négatifs")
        # Numérateur et dénominateur négatifs
        self.assertEqual(frac5.__eq__(other5), False, "__eq__ : numérateur et dénominateur négatifs")
        # Normal avec numérateur = 0
        self.assertEqual(frac6.__eq__(other6), True, "__eq__ : normal numérateur = 0")
        # Numérateur = 0 et dénominateur négatif
        self.assertEqual(frac7.__eq__(other7), True, "__eq__ : numérateur = 0 et dénominateur négatif")
        # Deux zéros en numérateur
        self.assertEqual(frac8.__eq__(other8), False, "__eq__ : deux zéros en numérateur")
        # Deux zéros en numérateur
        self.assertEqual(frac9.__eq__(other9), False, "__eq__ : deux zéros en numérateur")
        # Deux zéros en numérateur
        self.assertEqual(frac10.__eq__(other10), True, "__eq__ : deux zéros en numérateur")
        # Deux zéros en numérateur
        self.assertEqual(frac11.__eq__(other11), False, "__eq__ : deux zéros en numérateur")
        # Deux zéros en numérateur
        self.assertEqual(frac12.__eq__(other12), False, "__eq__ : deux zéros en numérateur")



    def test_is_integer(self):
        frac0 = Fraction()
        frac1 = Fraction(4, 2)
        frac2 = Fraction(1, 2)
        frac3 = Fraction(50, 10)
        frac4 = Fraction(0, 10)
        frac5 = Fraction(0, -10)
        frac6 = Fraction(10, 10)
        frac7 = Fraction(-2, 1)
        frac8 = Fraction(1, -2)

        self.assertEqual(frac0.is_integer(), True, "is_integer : fraction 0/1")

        self.assertEqual(frac1.is_integer(), True, "is_integer : fraction 4/2")

        self.assertEqual(frac2.is_integer(), False, "is_integer : fraction 1/2")

        self.assertEqual(frac3.is_integer(), True, "is_integer : fraction 50/10")

        self.assertEqual(frac4.is_integer(), True, "is_integer : fraction 0/10")

        self.assertEqual(frac5.is_integer(), True, "is_integer : fraction 0/-10")

        self.assertEqual(frac6.is_integer(), True, "is_integer : fraction 10/10")

        self.assertEqual(frac7.is_integer(), True, "is_integer : fraction -2/1")

        self.assertEqual(frac8.is_integer(), False, "is_integer : fraction 1/-2")

    def test_is_proper(self):
        frac0 = Fraction()
        frac1 = Fraction(4, 2)
        frac2 = Fraction(1, 2)
        frac3 = Fraction(50, 10)
        frac4 = Fraction(0, 10)
        frac5 = Fraction(0, -10)
        frac6 = Fraction(10, 10)
        frac7 = Fraction(-2, 1)
        frac8 = Fraction(1, -2)

        self.assertEqual(frac0.is_proper(), True, "is_proper : fraction 0/1")

        self.assertEqual(frac1.is_proper(), False, "is_proper : fraction 4/2")

        self.assertEqual(frac2.is_proper(), True, "is_proper : fraction 1/2")

        self.assertEqual(frac3.is_proper(), False, "is_proper : fraction 50/10")

        self.assertEqual(frac4.is_proper(), True, "is_proper : fraction 0/10")

        self.assertEqual(frac5.is_proper(), True, "is_proper : fraction 0/-10")

        self.assertEqual(frac6.is_proper(), False, "is_proper : fraction 10/10")

        self.assertEqual(frac7.is_proper(), False, "is_proper : fraction -2/1")

        self.assertEqual(frac8.is_proper(), True, "is_proper : fraction 1/-2")


    def test_is_adjacent_to(self):
        frac0 = Fraction()
        frac1 = Fraction(1, 2)
        frac2 = Fraction(1, 2)
        frac3 = Fraction(1, 2)
        frac4 = Fraction(5, 5)
        frac5 = Fraction(5, 5)
        frac6 = Fraction(-1, 2)
        frac7 = Fraction(-1, 2)
        frac8 = Fraction(1, 2)

        other0 = Fraction()
        other1 = Fraction(3, 4)
        other2 = Fraction(1, 3)
        other3 = Fraction(2, 4)
        other4 = Fraction(10, 5)
        other5 = Fraction(0, 5)
        other6 = Fraction(2, 1)
        other7 = Fraction(0, 2)
        other8 = Fraction(-1, 2)


        self.assertEqual(frac0.is_adjacent_to(other0), False, "is_adjacent_to : par défaut")

        self.assertEqual(frac1.is_adjacent_to(other1), False, "is_adjacent_to : fraction basique")

        self.assertEqual(frac2.is_adjacent_to(other2), True, "is_adjacent_to :  fraction basique")

        self.assertEqual(frac3.is_adjacent_to(other3), False, "is_adjacent_to : fractions égales")

        self.assertEqual(frac4.is_adjacent_to(other4), True, "is_adjacent_to : fraction adj de 1")

        self.assertEqual(frac5.is_adjacent_to(other5), True, "is_adjacent_to : fraction adj de -1")

        self.assertEqual(frac6.is_adjacent_to(other6), False,"is_adjacent_to : fraction adj négative")

        self.assertEqual(frac7.is_adjacent_to(other7), True,"is_adjacent_to : fraction adj négative avec other nul")

        self.assertEqual(frac8.is_adjacent_to(other8), False,"is_adjacent_to : fractions de meme valeurs absolues")