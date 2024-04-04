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
  `Id_Assurance` int(255) NOT NULL,
  `Compagnie` varchar(300) DEFAULT NULL,
  `NumPolice` int(255) DEFAULT NULL,
  `DateExpi` date DEFAULT NULL,
  `PrimeAnnuel` int(255) DEFAULT NULL,
  `Sinistre` varchar(300) DEFAULT NULL,
  `Id_camion` int(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `camion`
--

DROP TABLE IF EXISTS `camion`;
CREATE TABLE `camion` (
  `Id_camion` int(255) NOT NULL,
  `VIN` int(255) DEFAULT NULL,
  `Marque` varchar(40) DEFAULT NULL,
  `Modele` varchar(40) DEFAULT NULL,
  `DateConstruction` date DEFAULT NULL,
  `AnneedAchat` date DEFAULT NULL,
  `KmTotaux` int(255) DEFAULT NULL,
  `Carburant` varchar(40) DEFAULT NULL,
  `Charge` int(255) DEFAULT NULL,
  `Hauteur` int(255) DEFAULT NULL,
  `Disponibilité` tinyint(127) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `Chauffeur`
--

DROP TABLE IF EXISTS `Chauffeur`;
CREATE TABLE `Chauffeur` (
  `Id_Chauffeur` int(255) NOT NULL,
  `Nom` varchar(300) DEFAULT NULL,
  `Prénom` varchar(300) DEFAULT NULL,
  `CategoriePermis` varchar(300) DEFAULT NULL,
  `DateEngagement` date DEFAULT NULL,
  `Id_camion` int(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `Expertise`
--

DROP TABLE IF EXISTS `Expertise`;
CREATE TABLE `Expertise` (
  `Id_Expertise` int(255) NOT NULL,
  `Date` date DEFAULT NULL,
  `Resultat` date DEFAULT NULL,
  `Id_camion` int(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `Leasing`
--

DROP TABLE IF EXISTS `Leasing`;
CREATE TABLE `Leasing` (
  `Id_Leasing` int(255) NOT NULL,
  `Type de contrat` varchar(40) DEFAULT NULL,
  `SocieteDeLeasing` varchar(40) DEFAULT NULL,
  `DateDebut` date DEFAULT NULL,
  `DateFin` date DEFAULT NULL,
  `Montant` int(255) DEFAULT NULL,
  `Id_camion` int(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `Service`
--

DROP TABLE IF EXISTS `Service`;
CREATE TABLE `Service` (
  `Id_Service` int(255) NOT NULL,
  `Date` date DEFAULT NULL,
  `Description` varchar(300) DEFAULT NULL,
  `KmLastService` int(255) DEFAULT NULL,
  `KmNextService` int(255) DEFAULT NULL,
  `Service` varchar(300) DEFAULT NULL,
  `Nettoyage` date DEFAULT NULL,
  `ChangementPneu` date DEFAULT NULL,
  `Id_Expertise` int(255) DEFAULT NULL,
  `Id_camion` int(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

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
-- AUTO_INCREMENT pour la table `camion`
--
ALTER TABLE `camion`
  MODIFY `Id_camion` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT pour la table `Chauffeur`
--
ALTER TABLE `Chauffeur`
  MODIFY `Id_Chauffeur` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

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
  ADD CONSTRAINT `Leasing` FOREIGN KEY (`Id_camion`) REFERENCES `camion` (`Id_camion`);

--
-- Contraintes pour la table `Service`
--
ALTER TABLE `Service`
  ADD CONSTRAINT `camion` FOREIGN KEY (`Id_camion`) REFERENCES `camion` (`Id_camion`),
  ADD CONSTRAINT `expertise0` FOREIGN KEY (`Id_Expertise`) REFERENCES `Expertise` (`Id_Expertise`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
