-- 1. Sélectionner tous les camions
SELECT * FROM camion;

-- 2. Sélectionner tous les chauffeurs
SELECT * FROM Chauffeur;

-- 3. Sélectionner toutes les assurances
SELECT * FROM Assurance;

-- 4. Sélectionner toutes les expertises
SELECT * FROM Expertise;

-- 5. Sélectionner tous les contrats de leasing
SELECT * FROM Leasing;

-- 6. Sélectionner tous les services
SELECT * FROM Service;

-- 7. Sélectionner les camions de marque 'Mercedes'
SELECT * FROM camion WHERE Marque = 'Mercedes';

-- 8. Sélectionner les assurances avec une prime annuelle supérieure à 1600
SELECT * FROM Assurance WHERE PrimeAnnuel > 1600;

-- 9. Sélectionner les chauffeurs ayant un permis de catégorie 'CE'
SELECT * FROM Chauffeur WHERE CategoriePermis = 'CE';

-- 10. Sélectionner les expertises avec un résultat 'Valid'
SELECT * FROM Expertise WHERE Resultat = 'Valid';

-- 11. Sélectionner les contrats de leasing de type 'Full Service'
SELECT * FROM Leasing WHERE Type_de_contrat = 'Full Service';

-- 12. Sélectionner les services avec un kilométrage du dernier service supérieur à 400000
SELECT * FROM Service WHERE KmLastService > 400000;

-- 13. Sélectionner les camions avec leurs chauffeurs
SELECT c.*, ch.* FROM camion c
JOIN Chauffeur ch ON c.Id_camion = ch.Id_camion;

-- 14. Sélectionner les camions avec leurs assurances
SELECT c.*, a.* FROM camion c
JOIN Assurance a ON c.Id_camion = a.Id_camion;

-- 15. Sélectionner les camions avec leurs expertises
SELECT c.*, e.* FROM camion c
JOIN Expertise e ON c.Id_camion = e.Id_camion;

-- 16. Sélectionner les camions avec leurs contrats de leasing
SELECT c.*, l.* FROM camion c
JOIN Leasing l ON c.Id_camion = l.Id_camion;

-- 17. Sélectionner les camions avec leurs services
SELECT c.*, s.* FROM camion c
JOIN Service s ON c.Id_camion = s.Id_camion;

-- 18. Compter le nombre de camions par marque
SELECT Marque, COUNT(*) as Nb_Camions FROM camion GROUP BY Marque;

-- 19. Calculer la prime annuelle moyenne des assurances par compagnie
SELECT Compagnie, AVG(PrimeAnnuel) as Prime_Moyenne FROM Assurance GROUP BY Compagnie;

-- 20. Compter le nombre de chauffeurs par catégorie de permis
SELECT CategoriePermis, COUNT(*) as Nb_Chauffeurs FROM Chauffeur GROUP BY CategoriePermis;

-- 21. Compter le nombre d'expertises par résultat
SELECT Resultat, COUNT(*) as Nb_Expertises FROM Expertise GROUP BY Resultat;

-- 22. Calculer le montant total des contrats de leasing par société de leasing
SELECT SocieteDeLeasing, SUM(Montant) as Montant_Total FROM Leasing GROUP BY SocieteDeLeasing;

-- 23. Compter le nombre de services par type de service
SELECT Service, COUNT(*) as Nb_Services FROM Service GROUP BY Service;

-- 24. Insérer un nouveau camion
INSERT INTO camion (VIN, Marque, Modele, DateConstruction, AnneedAchat, KmTotaux, Carburant, Charge, Hauteur, Disponibilité) 
VALUES ('111222333', 'Tesla', 'Semi', '2023-01-01', '2023-02-01', 10000, 'Electric', 25000, 4, 1);

-- 25. Insérer une nouvelle assurance
INSERT INTO Assurance (Compagnie, NumPolice, DateExpi, PrimeAnnuel, Sinistre, Id_camion) 
VALUES ('AXA', 99988, '2025-01-01', 2000, 'None', 1);

-- 26. Insérer un nouveau chauffeur
INSERT INTO Chauffeur (Nom, Prénom, CategoriePermis, DateEngagement, Id_camion) 
VALUES ('Rossi', 'Mario', 'C', '2023-05-15', 1);

-- 27. Insérer une nouvelle expertise
INSERT INTO Expertise (Date, Resultat, Id_camion) 
VALUES ('2023-12-01', 'Valid', 1);

-- 28. Insérer un nouveau contrat de leasing
INSERT INTO Leasing (Type_de_contrat, SocieteDeLeasing, DateDebut, DateFin, Montant, Id_camion) 
VALUES ('Finance Lease', 'ALD Automotive', '2023-01-01', '2027-01-01', 6000, 1);

-- 29. Insérer un nouveau service
INSERT INTO Service (Date, Description, KmLastService, KmNextService, Service, Nettoyage, ChangementPneu, Id_Expertise, Id_camion) 
VALUES ('2023-06-15', 'Maintenance', 550000, 600000, 'Complet', '2023-06-16', '2023-06-17', 1, 1);

-- 30. Mettre à jour la prime annuelle d'une assurance
UPDATE Assurance SET PrimeAnnuel = 2100 WHERE Id_Assurance = 1;

-- 31. Mettre à jour le kilométrage total d'un camion
UPDATE camion SET KmTotaux = 510000 WHERE Id_camion = 1;

-- 32. Mettre à jour la date d'engagement d'un chauffeur
UPDATE Chauffeur SET DateEngagement = '2023-06-01' WHERE Id_Chauffeur = 1;

-- 33. Mettre à jour le résultat d'une expertise
UPDATE Expertise SET Resultat = 'Invalid' WHERE Id_Expertise = 1;

-- 34. Mettre à jour la société de leasing d'un contrat
UPDATE Leasing SET SocieteDeLeasing = 'NewLease' WHERE Id_Leasing = 1;

-- 35. Mettre à jour la description d'un service
UPDATE Service SET Description = 'Réparation majeure' WHERE Id_Service = 1;

-- 36. Supprimer une assurance
DELETE FROM Assurance WHERE Id_Assurance = 1;

-- 37. Supprimer un camion
DELETE FROM camion WHERE Id_camion = 1;

-- 38. Supprimer un chauffeur
DELETE FROM Chauffeur WHERE Id_Chauffeur = 1;

-- 39. Supprimer une expertise
DELETE FROM Expertise WHERE Id_Expertise = 1;

-- 40. Supprimer un contrat de leasing
DELETE FROM Leasing WHERE Id_Leasing = 1;

-- 41. Supprimer un service
DELETE FROM Service WHERE Id_Service = 1;

-- 42. Sélectionner les camions avec leurs chauffeurs et leurs assurances
SELECT c.*, ch.*, a.* FROM camion c
JOIN Chauffeur ch ON c.Id_camion = ch.Id_camion
JOIN Assurance a ON c.Id_camion = a.Id_camion;

-- 43. Sélectionner les camions ayant plus de 400000 km et dont la prime annuelle d'assurance est supérieure à 1600
SELECT c.*, a.* FROM camion c
JOIN Assurance a ON c.Id_camion = a.Id_camion
WHERE c.KmTotaux > 400000 AND a.PrimeAnnuel > 1600;

-- 44. Sélectionner les camions avec leurs expertises et les services associés à ces expertises
SELECT c.*, e.*, s.* FROM camion c
JOIN Expertise e ON c.Id_camion = e.Id_camion
JOIN Service s ON e.Id_Expertise = s.Id_Expertise;

-- 45. Sélectionner les camions avec leurs contrats de leasing et leurs chauffeurs
SELECT c.*, l.*, ch.* FROM camion c
JOIN Leasing l ON c.Id_camion = l.Id_camion
JOIN Chauffeur ch ON c.Id_camion = ch.Id_camion;

-- 46. Sélectionner les camions, leurs assurances, et les expertises pour lesquelles les résultats sont 'Valid'
SELECT c.*, a.*, e.* FROM camion c
JOIN Assurance a ON c.Id_camion = a.Id_camion
JOIN Expertise e ON c.Id_camion = e.Id_camion
WHERE e.Resultat = 'Valid';

-- 47. Sélectionner les camions avec leurs chauffeurs et les services effectués au cours de l'année 2023
SELECT c.*, ch.*, s.* FROM camion c
JOIN Chauffeur ch ON c.Id_camion = ch.Id_camion
JOIN Service s ON c.Id_camion = s.Id_camion
WHERE YEAR(s.Date) = 2023;

-- 48. Calculer le kilométrage total moyen des camions par marque
SELECT Marque, AVG(KmTotaux) as Km_Moyen FROM camion GROUP BY Marque;

-- 49. Compter le nombre de services effectués par camion
SELECT Id_camion, COUNT(*) as Nb_Services FROM Service GROUP BY Id_camion;

-- 50. Calculer le montant total des contrats de leasing par type de contrat
SELECT Type_de_contrat, SUM(Montant) as Montant_Total FROM Leasing GROUP BY Type_de_contrat;

-- 51. Calculer le nombre total de chauffeurs par date d'engagement
SELECT DateEngagement, COUNT(*) as Nb_Chauffeurs FROM Chauffeur GROUP BY DateEngagement;

-- 52. Calculer la prime annuelle totale des assurances par sinistre
SELECT Sinistre, SUM(PrimeAnnuel) as Prime_Total FROM Assurance GROUP BY Sinistre;

-- 53. Calculer le montant total des services par type de service
SELECT Service, SUM(KmLastService) as Km_Total FROM Service GROUP BY Service;

-- 54. Sélectionner les chauffeurs et les camions avec le type de carburant 'Diesel'
SELECT ch.*, c.* FROM Chauffeur ch
JOIN camion c ON ch.Id_camion = c.Id_camion
WHERE c.Carburant = 'Diesel';

-- 55. Sélectionner les camions avec le plus haut kilométrage total
SELECT * FROM camion ORDER BY KmTotaux DESC LIMIT 1;

-- 56. Sélectionner les chauffeurs ayant les plus anciens dates d'engagement
SELECT * FROM Chauffeur ORDER BY DateEngagement ASC LIMIT 5;

-- 57. Sélectionner les expertises les plus récentes
SELECT * FROM Expertise ORDER BY Date DESC LIMIT 5;

-- 58. Sélectionner les contrats de leasing les plus coûteux
SELECT * FROM Leasing ORDER BY Montant DESC LIMIT 5;

-- 59. Sélectionner les services les plus récents
SELECT * FROM Service ORDER BY Date DESC LIMIT 5;





