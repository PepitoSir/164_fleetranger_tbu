-- OM 2021.02.17
-- FICHIER MYSQL POUR FAIRE FONCTIONNER LES EXEMPLES
-- DE REQUETES MYSQL
-- Database: BURKHALTER_THOMAS_DEVA1A_FLEETRANGER_164_2024

-- Destruction de la BD si elle existe.
-- Pour être certain d'avoir la dernière version des données

DROP DATABASE IF EXISTS BURKHALTER_THOMAS_DEVA1A_FLEETRANGER_164_2024;

-- Création d'un nouvelle base de donnée

CREATE DATABASE IF NOT EXISTS BURKHALTER_THOMAS_DEVA1A_FLEETRANGER_164_2024;

-- Utilisation de cette base de donnée

USE BURKHALTER_THOMAS_DEVA1A_FLEETRANGER_164_2024;

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `FleetRanger`
--
-- Structure de la table `Assurance`
--

DROP TABLE IF EXISTS `Assurance`;
CREATE TABLE `Assurance` (
  `Id_Assurance` int(11) NOT NULL,
  `Compagnie` varchar(300) DEFAULT NULL,
  `NumPolice` int(11) DEFAULT NULL,
  `DateExpi` date DEFAULT NULL,
  `PrimeAnnuel` int(11) DEFAULT NULL,
  `Sinistre` varchar(300) DEFAULT NULL,
  `Id_camion` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;

--
-- Déchargement des données de la table `Assurance`
--

INSERT INTO `Assurance` (`Id_Assurance`, `Compagnie`, `NumPolice`, `DateExpi`, `PrimeAnnuel`, `Sinistre`, `Id_camion`) VALUES
(1, 'AXA', 12345, '2023-12-31', 1500, 'None', 1),
(2, 'Allianz', 67890, '2024-05-31', 2000, 'Accident mineur', 2),
(3, 'Generali', 11121, '2023-11-30', 1800, 'None', 3),
(4, 'SwissLife', 33333, '2025-04-15', 1700, 'None', 4),
(5, 'Zurich', 44444, '2023-08-20', 1600, 'Accident majeur', 5),
(6, 'AXA', 55555, '2024-02-28', 1550, 'None', 6),
(7, 'Allianz', 66666, '2023-07-10', 1900, 'None', 7),
(8, 'Generali', 77777, '2024-03-31', 1800, 'Accident mineur', 8),
(9, 'SwissLife', 88888, '2023-12-15', 1750, 'None', 9),
(10, 'Zurich', 99999, '2024-01-01', 1650, 'None', 10),
(11, 'AXA', 12345, '2023-12-31', 1500, 'None', 1),
(12, 'Allianz', 67890, '2024-05-31', 2000, 'Accident mineur', 2),
(13, 'Generali', 11121, '2023-11-30', 1800, 'None', 3),
(14, 'SwissLife', 33333, '2025-04-15', 1700, 'None', 4),
(15, 'Zurich', 44444, '2023-08-20', 1600, 'Accident majeur', 5),
(16, 'AXA', 55555, '2024-02-28', 1550, 'None', 6),
(17, 'Allianz', 66666, '2023-07-10', 1900, 'None', 7),
(18, 'Generali', 77777, '2024-03-31', 1800, 'Accident mineur', 8),
(19, 'SwissLife', 88888, '2023-12-15', 1750, 'None', 9),
(20, 'Zurich', 99999, '2024-01-01', 1650, 'None', 10),
(21, 'Zurich', 112233, '2023-11-30', 1600, 'None', 1),
(22, 'Helvetia', 223344, '2024-06-30', 1750, 'Accident mineur', 2),
(23, 'Swiss Life', 334455, '2023-09-30', 1500, 'None', 3),
(24, 'Bâloise', 445566, '2025-03-15', 1800, 'None', 4),
(25, 'Allianz Suisse', 556677, '2024-07-15', 1900, 'Accident majeur', 5),
(26, 'Vaudoise', 667788, '2024-02-28', 1650, 'None', 6),
(27, 'AXA Winterthur', 778899, '2023-08-10', 1700, 'None', 7),
(28, 'Mobiliar', 889900, '2024-04-20', 1850, 'Accident mineur', 8),
(29, 'Generali Suisse', 990011, '2023-11-15', 1600, 'None', 9),
(30, 'Sympany', 110022, '2024-05-01', 1500, 'None', 10);

-- --------------------------------------------------------

--
-- Structure de la table `camion`
--

DROP TABLE IF EXISTS `camion`;
CREATE TABLE `camion` (
  `Id_camion` int(11) NOT NULL,
  `VIN` varchar(255) DEFAULT NULL,
  `Marque` varchar(40) DEFAULT NULL,
  `Modele` varchar(40) DEFAULT NULL,
  `DateConstruction` date DEFAULT NULL,
  `AnneedAchat` date DEFAULT NULL,
  `KmTotaux` int(11) DEFAULT NULL,
  `Carburant` varchar(40) DEFAULT NULL,
  `Charge` int(11) DEFAULT NULL,
  `Hauteur` int(11) DEFAULT NULL,
  `Disponibilité` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;

--
-- Déchargement des données de la table `camion`
--

INSERT INTO `camion` (`Id_camion`, `VIN`, `Marque`, `Modele`, `DateConstruction`, `AnneedAchat`, `KmTotaux`, `Carburant`, `Charge`, `Hauteur`, `Disponibilité`) VALUES
(1, '123456789', 'Mercedes', 'Actros', '2015-06-12', '2015-06-15', 500000, 'Diesel', 20000, 4, 1),
(2, '987654321', 'Volvo', 'FH16', '2017-09-20', '2017-10-01', 300000, 'Diesel', 25000, 4, 1),
(3, '234567890', 'Scania', 'R450', '2018-03-25', '2018-04-01', 400000, 'Diesel', 22000, 3, 1),
(4, '345678901', 'MAN', 'TGX', '2016-04-15', '2016-05-01', 350000, 'Diesel', 23000, 4, 1),
(5, '456789012', 'DAF', 'XF', '2019-07-18', '2019-08-01', 280000, 'Diesel', 24000, 3, 1),
(6, '567890123', 'Iveco', 'Stralis', '2015-02-10', '2015-03-01', 420000, 'Diesel', 21000, 4, 1),
(7, '678901234', 'Renault', 'T', '2020-11-25', '2020-12-01', 100000, 'Diesel', 26000, 3, 1),
(8, '789012345', 'Kenworth', 'T680', '2021-08-30', '2021-09-01', 50000, 'Diesel', 28000, 4, 1),
(9, '890123456', 'Peterbilt', '579', '2018-05-10', '2018-06-01', 360000, 'Diesel', 27000, 3, 1),
(10, '901234567', 'Mack', 'Anthem', '2017-12-12', '2018-01-01', 390000, 'Diesel', 29000, 4, 1),
(11, '123456789', 'Mercedes', 'Actros', '2015-06-12', '2015-06-15', 500000, 'Diesel', 20000, 4, 1),
(12, '987654321', 'Volvo', 'FH16', '2017-09-20', '2017-10-01', 300000, 'Diesel', 25000, 4, 1),
(13, '234567890', 'Scania', 'R450', '2018-03-25', '2018-04-01', 400000, 'Diesel', 22000, 3, 1),
(14, '345678901', 'MAN', 'TGX', '2016-04-15', '2016-05-01', 350000, 'Diesel', 23000, 4, 1),
(15, '456789012', 'DAF', 'XF', '2019-07-18', '2019-08-01', 280000, 'Diesel', 24000, 3, 1),
(16, '567890123', 'Iveco', 'Stralis', '2015-02-10', '2015-03-01', 420000, 'Diesel', 21000, 4, 1),
(17, '678901234', 'Renault', 'T', '2020-11-25', '2020-12-01', 100000, 'Diesel', 26000, 3, 1),
(18, '789012345', 'Kenworth', 'T680', '2021-08-30', '2021-09-01', 50000, 'Diesel', 28000, 4, 1),
(19, '890123456', 'Peterbilt', '579', '2018-05-10', '2018-06-01', 360000, 'Diesel', 27000, 3, 1),
(20, '901234567', 'Mack', 'Anthem', '2017-12-12', '2018-01-01', 390000, 'Diesel', 29000, 4, 1),
(21, '987654310', 'Mercedes', 'Actros', '2016-01-10', '2016-02-01', 550000, 'Diesel', 24000, 4, 1),
(22, '123456798', 'Volvo', 'FH16', '2017-11-15', '2017-12-01', 320000, 'Diesel', 23000, 4, 1),
(23, '234567891', 'Scania', 'R500', '2018-05-20', '2018-06-01', 400000, 'Diesel', 21000, 4, 1),
(24, '345678902', 'MAN', 'TGX', '2019-04-22', '2019-05-01', 290000, 'Diesel', 20000, 3, 1),
(25, '456789013', 'DAF', 'XF', '2020-09-25', '2020-10-01', 180000, 'Diesel', 22000, 4, 1),
(26, '567890124', 'Iveco', 'Stralis', '2021-02-15', '2021-03-01', 100000, 'Diesel', 24000, 3, 1),
(27, '678901235', 'Renault', 'T', '2022-06-10', '2022-07-01', 50000, 'Diesel', 25000, 4, 1),
(28, '789012346', 'Kenworth', 'T700', '2021-09-05', '2021-10-01', 120000, 'Diesel', 26000, 3, 1),
(29, '890123457', 'Peterbilt', '389', '2023-01-12', '2023-02-01', 30000, 'Diesel', 27000, 4, 1),
(30, '901234568', 'Mack', 'Anthem', '2022-12-01', '2023-01-01', 50000, 'Diesel', 28000, 4, 1);

-- --------------------------------------------------------

--
-- Structure de la table `Chauffeur`
--

DROP TABLE IF EXISTS `Chauffeur`;
CREATE TABLE `Chauffeur` (
  `Id_Chauffeur` int(11) NOT NULL,
  `Nom` varchar(300) DEFAULT NULL,
  `Prénom` varchar(300) DEFAULT NULL,
  `CategoriePermis` varchar(300) DEFAULT NULL,
  `DateEngagement` date DEFAULT NULL,
  `Id_camion` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;

--
-- Déchargement des données de la table `Chauffeur`
--

INSERT INTO `Chauffeur` (`Id_Chauffeur`, `Nom`, `Prénom`, `CategoriePermis`, `DateEngagement`, `Id_camion`) VALUES
(1, 'Dupont', 'Jean', 'C', '2020-01-15', 1),
(2, 'Martin', 'Pierre', 'CE', '2019-06-10', 2),
(3, 'Durand', 'Michel', 'C1', '2018-11-25', 3),
(4, 'Bernard', 'Luc', 'C', '2021-03-10', 4),
(5, 'Thomas', 'René', 'CE', '2020-05-15', 5),
(6, 'Petit', 'Alex', 'C1', '2019-07-22', 6),
(7, 'Leroy', 'Paul', 'C', '2021-09-14', 7),
(8, 'Moreau', 'Henri', 'CE', '2018-10-05', 8),
(9, 'Simon', 'Louis', 'C1', '2017-11-20', 9),
(10, 'Laurent', 'Jacques', 'C', '2020-12-01', 10),
(11, 'Dupont', 'Jean', 'C', '2020-01-15', 1),
(12, 'Martin', 'Pierre', 'CE', '2019-06-10', 2),
(13, 'Durand', 'Michel', 'C1', '2018-11-25', 3),
(14, 'Bernard', 'Luc', 'C', '2021-03-10', 4),
(15, 'Thomas', 'René', 'CE', '2020-05-15', 5),
(16, 'Petit', 'Alex', 'C1', '2019-07-22', 6),
(17, 'Leroy', 'Paul', 'C', '2021-09-14', 7),
(18, 'Moreau', 'Henri', 'CE', '2018-10-05', 8),
(19, 'Simon', 'Louis', 'C1', '2017-11-20', 9),
(20, 'Laurent', 'Jacques', 'C', '2020-12-01', 10),
(21, 'Müller', 'Hans', 'C', '2020-02-15', 1),
(22, 'Meier', 'Fritz', 'CE', '2019-07-11', 2),
(23, 'Schneider', 'Urs', 'C1', '2018-12-26', 3),
(24, 'Weber', 'Reto', 'C', '2021-04-11', 4),
(25, 'Huber', 'Daniel', 'CE', '2020-06-16', 5),
(26, 'Steiner', 'Peter', 'C1', '2019-08-23', 6),
(27, 'Zürcher', 'Heinz', 'C', '2021-10-15', 7),
(28, 'Fischer', 'Martin', 'CE', '2018-11-06', 8),
(29, 'Keller', 'Christian', 'C1', '2017-12-21', 9),
(30, 'Bachmann', 'Thomas', 'C', '2020-11-02', 10);

-- --------------------------------------------------------

--
-- Structure de la table `Expertise`
--

DROP TABLE IF EXISTS `Expertise`;
CREATE TABLE `Expertise` (
  `Id_Expertise` int(11) NOT NULL,
  `Date` date DEFAULT NULL,
  `Resultat` varchar(300) DEFAULT NULL,
  `Id_camion` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;

--
-- Déchargement des données de la table `Expertise`
--

INSERT INTO `Expertise` (`Id_Expertise`, `Date`, `Resultat`, `Id_camion`) VALUES
(1, '2022-07-15', '2022-07-15', 1),
(2, '2021-08-20', '2021-08-20', 2),
(3, '2023-03-05', '2023-03-05', 3),
(4, '2020-10-10', '2020-10-10', 4),
(5, '2019-09-25', '2019-09-25', 5),
(6, '2021-12-15', '2021-12-15', 6),
(7, '2022-11-20', '2022-11-20', 7),
(8, '2023-05-10', '2023-05-10', 8),
(9, '2020-01-05', '2020-01-05', 9),
(10, '2021-02-15', '2021-02-15', 10),
(11, '2022-07-15', '2022-07-15', 1),
(12, '2021-08-20', '2021-08-20', 2),
(13, '2023-03-05', '2023-03-05', 3),
(14, '2020-10-10', '2020-10-10', 4),
(15, '2019-09-25', '2019-09-25', 5),
(16, '2021-12-15', '2021-12-15', 6),
(17, '2022-11-20', '2022-11-20', 7),
(18, '2023-05-10', '2023-05-10', 8),
(19, '2020-01-05', '2020-01-05', 9),
(20, '2021-02-15', '2021-02-15', 10),
(21, '2022-06-20', 'Valid', 1),
(22, '2021-07-25', 'Valid', 2),
(23, '2023-01-10', 'Valid', 3),
(24, '2020-11-15', 'Valid', 4),
(25, '2019-10-30', 'Valid', 5),
(26, '2021-12-20', 'Valid', 6),
(27, '2022-10-25', 'Valid', 7),
(28, '2023-04-15', 'Valid', 8),
(29, '2020-02-10', 'Valid', 9),
(30, '2021-03-20', 'Valid', 10);

-- --------------------------------------------------------

--
-- Structure de la table `Leasing`
--

DROP TABLE IF EXISTS `Leasing`;
CREATE TABLE `Leasing` (
  `Id_Leasing` int(11) NOT NULL,
  `Type_de_contrat` varchar(40) DEFAULT NULL,
  `SocieteDeLeasing` varchar(40) DEFAULT NULL,
  `DateDebut` date DEFAULT NULL,
  `DateFin` date DEFAULT NULL,
  `Montant` int(11) DEFAULT NULL,
  `Id_camion` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;

--
-- Déchargement des données de la table `Leasing`
--

INSERT INTO `Leasing` (`Id_Leasing`, `Type_de_contrat`, `SocieteDeLeasing`, `DateDebut`, `DateFin`, `Montant`, `Id_camion`) VALUES
(1, 'Full Service', 'LeasePlan', '2020-01-01', '2024-01-01', 5000, 1),
(2, 'Finance Lease', 'Arval', '2019-06-01', '2023-06-01', 4500, 2),
(3, 'Operating Lease', 'ALD Automotive', '2021-01-01', '2025-01-01', 5500, 3),
(4, 'Full Service', 'LeasePlan', '2020-07-01', '2024-07-01', 5200, 4),
(5, 'Finance Lease', 'Arval', '2019-08-01', '2023-08-01', 4600, 5),
(6, 'Operating Lease', 'ALD Automotive', '2021-03-01', '2025-03-01', 5700, 6),
(7, 'Full Service', 'LeasePlan', '2020-10-01', '2024-10-01', 5300, 7),
(8, 'Finance Lease', 'Arval', '2019-11-01', '2023-11-01', 4800, 8),
(9, 'Operating Lease', 'ALD Automotive', '2021-05-01', '2025-05-01', 5800, 9),
(10, 'Full Service', 'LeasePlan', '2020-12-01', '2024-12-01', 5400, 10),
(11, 'Full Service', 'Swisslease', '2020-02-01', '2024-02-01', 5000, 1),
(12, 'Finance Lease', 'Autoleasing Suisse', '2019-07-01', '2023-07-01', 4500, 2),
(13, 'Operating Lease', 'Fleetline', '2021-02-01', '2025-02-01', 5500, 3),
(14, 'Full Service', 'Swisslease', '2020-08-01', '2024-08-01', 5200, 4),
(15, 'Finance Lease', 'Autoleasing Suisse', '2019-09-01', '2023-09-01', 4600, 5),
(16, 'Operating Lease', 'Fleetline', '2021-04-01', '2025-04-01', 5700, 6),
(17, 'Full Service', 'Swisslease', '2020-11-01', '2024-11-01', 5300, 7),
(18, 'Finance Lease', 'Autoleasing Suisse', '2019-12-01', '2023-12-01', 4800, 8),
(19, 'Operating Lease', 'Fleetline', '2021-06-01', '2025-06-01', 5800, 9),
(20, 'Full Service', 'Swisslease', '2020-01-01', '2024-01-01', 5400, 10);

-- --------------------------------------------------------

--
-- Structure de la table `Service`
--

DROP TABLE IF EXISTS `Service`;
CREATE TABLE `Service` (
  `Id_Service` int(11) NOT NULL,
  `Date` date DEFAULT NULL,
  `Description` varchar(300) DEFAULT NULL,
  `KmLastService` int(11) DEFAULT NULL,
  `KmNextService` int(11) DEFAULT NULL,
  `Service` varchar(300) DEFAULT NULL,
  `Nettoyage` date DEFAULT NULL,
  `ChangementPneu` date DEFAULT NULL,
  `Id_Expertise` int(11) DEFAULT NULL,
  `Id_camion` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;

--
-- Déchargement des données de la table `Service`
--

INSERT INTO `Service` (`Id_Service`, `Date`, `Description`, `KmLastService`, `KmNextService`, `Service`, `Nettoyage`, `ChangementPneu`, `Id_Expertise`, `Id_camion`) VALUES
(1, '2022-01-15', 'Vidange', 450000, 500000, 'Complet', '2022-01-16', '2022-01-17', 1, 1),
(2, '2021-07-20', 'Révision', 250000, 300000, 'Partiel', '2021-07-21', '2021-07-22', 2, 2),
(3, '2023-04-05', 'Réparation', 380000, 420000, 'Complet', '2023-04-06', '2023-04-07', 3, 3),
(4, '2022-03-10', 'Maintenance', 340000, 390000, 'Partiel', '2022-03-11', '2022-03-12', 4, 4),
(5, '2021-05-15', 'Inspection', 280000, 330000, 'Complet', '2021-05-16', '2021-05-17', 5, 5),
(6, '2020-08-20', 'Révision', 300000, 350000, 'Partiel', '2020-08-21', '2020-08-22', 6, 6),
(7, '2023-01-25', 'Réparation', 410000, 450000, 'Complet', '2023-01-26', '2023-01-27', 7, 7),
(8, '2019-10-05', 'Maintenance', 320000, 370000, 'Partiel', '2019-10-06', '2019-10-07', 8, 8),
(9, '2020-12-15', 'Inspection', 290000, 340000, 'Complet', '2020-12-16', '2020-12-17', 9, 9),
(10, '2021-04-01', 'Vidange', 360000, 410000, 'Partiel', '2021-04-02', '2021-04-03', 10, 10),
(11, '2022-02-15', 'Vidange', 480000, 530000, 'Complet', '2022-02-16', '2022-02-17', 1, 1),
(12, '2021-08-25', 'Révision', 270000, 320000, 'Partiel', '2021-08-26', '2021-08-27', 2, 2),
(13, '2023-05-10', 'Réparation', 410000, 460000, 'Complet', '2023-05-11', '2023-05-12', 3, 3),
(14, '2022-04-15', 'Maintenance', 360000, 410000, 'Partiel', '2022-04-16', '2022-04-17', 4, 4),
(15, '2021-06-20', 'Inspection', 310000, 360000, 'Complet', '2021-06-21', '2021-06-22', 5, 5),
(16, '2020-09-25', 'Révision', 330000, 380000, 'Partiel', '2020-09-26', '2020-09-27', 6, 6),
(17, '2023-02-01', 'Réparation', 430000, 480000, 'Complet', '2023-02-02', '2023-02-03', 7, 7),
(18, '2019-11-15', 'Maintenance', 350000, 400000, 'Partiel', '2019-11-16', '2019-11-17', 8, 8),
(19, '2020-12-25', 'Inspection', 320000, 370000, 'Complet', '2020-12-26', '2020-12-27', 9, 9),
(20, '2021-05-10', 'Vidange', 380000, 430000, 'Partiel', '2021-05-11', '2021-05-12', 10, 10);

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `Assurance`
--
ALTER TABLE `Assurance`
  ADD PRIMARY KEY (`Id_Assurance`),
  ADD KEY `Id_camion` (`Id_camion`);

--
-- Index pour la table `camion`
--
ALTER TABLE `camion`
  ADD PRIMARY KEY (`Id_camion`);

--
-- Index pour la table `Chauffeur`
--
ALTER TABLE `Chauffeur`
  ADD PRIMARY KEY (`Id_Chauffeur`),
  ADD KEY `Id_camion` (`Id_camion`);

--
-- Index pour la table `Expertise`
--
ALTER TABLE `Expertise`
  ADD PRIMARY KEY (`Id_Expertise`),
  ADD KEY `Id_camion` (`Id_camion`);

--
-- Index pour la table `Leasing`
--
ALTER TABLE `Leasing`
  ADD PRIMARY KEY (`Id_Leasing`),
  ADD KEY `Id_camion` (`Id_camion`);

--
-- Index pour la table `Service`
--
ALTER TABLE `Service`
  ADD PRIMARY KEY (`Id_Service`),
  ADD KEY `Id_camion` (`Id_camion`),
  ADD KEY `Id_Expertise` (`Id_Expertise`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `Assurance`
--
ALTER TABLE `Assurance`
  MODIFY `Id_Assurance` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;

--
-- AUTO_INCREMENT pour la table `camion`
--
ALTER TABLE `camion`
  MODIFY `Id_camion` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;

--
-- AUTO_INCREMENT pour la table `Chauffeur`
--
ALTER TABLE `Chauffeur`
  MODIFY `Id_Chauffeur` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;

--
-- AUTO_INCREMENT pour la table `Expertise`
--
ALTER TABLE `Expertise`
  MODIFY `Id_Expertise` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;

--
-- AUTO_INCREMENT pour la table `Leasing`
--
ALTER TABLE `Leasing`
  MODIFY `Id_Leasing` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT pour la table `Service`
--
ALTER TABLE `Service`
  MODIFY `Id_Service` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `Assurance`
--
ALTER TABLE `Assurance`
  ADD CONSTRAINT `assurance` FOREIGN KEY (`Id_camion`) REFERENCES `camion` (`Id_camion`);

--
-- Contraintes pour la table `Chauffeur`
--
ALTER TABLE `Chauffeur`
  ADD CONSTRAINT `chauffeur` FOREIGN KEY (`Id_camion`) REFERENCES `camion` (`Id_camion`);

--
-- Contraintes pour la table `Expertise`
--
ALTER TABLE `Expertise`
  ADD CONSTRAINT `expertise` FOREIGN KEY (`Id_camion`) REFERENCES `camion` (`Id_camion`);

--
-- Contraintes pour la table `Leasing`
--
ALTER TABLE `Leasing`
  ADD CONSTRAINT `leasing` FOREIGN KEY (`Id_camion`) REFERENCES `camion` (`Id_camion`);

--
-- Contraintes pour la table `Service`
--
ALTER TABLE `Service`
  ADD CONSTRAINT `service_camion` FOREIGN KEY (`Id_camion`) REFERENCES `camion` (`Id_camion`),
  ADD CONSTRAINT `service_expertise` FOREIGN KEY (`Id_Expertise`) REFERENCES `Expertise` (`Id_Expertise`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
