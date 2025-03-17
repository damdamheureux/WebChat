-- phpMyAdmin SQL Dump
-- version 5.2.2
-- https://www.phpmyadmin.net/
--
-- Host: 82.65.174.2:15800
-- Generation Time: Mar 01, 2025 at 01:29 PM
-- Server version: 8.4.4
-- PHP Version: 8.3.17

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `default`
--

-- --------------------------------------------------------

--
-- Table structure for table `accverif`
--

CREATE TABLE `accverif` (
  `id` int NOT NULL,
  `userid` int NOT NULL,
  `token` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `messages`
--

CREATE TABLE `messages` (
  `id` int NOT NULL,
  `author` int DEFAULT NULL,
  `body` varchar(255) NOT NULL,
  `timestamp` datetime DEFAULT NULL,
  `roomID` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `messages`
--

INSERT INTO `messages` (`id`, `author`, `body`, `timestamp`, `roomID`) VALUES
(57, 3, '🙂‍↕️', '2025-03-01 10:42:31', 6),
(58, 99, 'Ceci est un message système', '2025-03-01 10:42:52', 6),
(59, 3, '.', '2025-03-01 10:43:03', 6),
(60, 1, 'Merci ', '2025-03-01 10:43:17', 6);

-- --------------------------------------------------------

--
-- Table structure for table `rooms`
--

CREATE TABLE `rooms` (
  `roomid` int NOT NULL,
  `creatorID` int NOT NULL,
  `roomname` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `rooms`
--

INSERT INTO `rooms` (`roomid`, `creatorID`, `roomname`) VALUES
(1, 3, 'CACA'),
(4, 3, 'Piscine du mois de mai'),
(5, 3, 'Final Test'),
(6, 1, 'Océan brem'),
(7, 3, 'Ada Lovelace\'s room'),
(8, 3, 'Encore un test'),
(9, 3, 'caca'),
(10, 3, 'Le js'),
(11, 3, '....'),
(12, 3, 'Salle 12'),
(13, 3, 'Nouvelle salle j\'ai tout delete');

-- --------------------------------------------------------

--
-- Table structure for table `roomusers`
--

CREATE TABLE `roomusers` (
  `id` int NOT NULL,
  `roomID` int NOT NULL,
  `userid` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `roomusers`
--

INSERT INTO `roomusers` (`id`, `roomID`, `userid`) VALUES
(23, 7, 99),
(25, 8, 99),
(27, 9, 99),
(29, 10, 99),
(31, 11, 99),
(33, 12, 99),
(35, 13, 99),
(36, 12, 3),
(37, 12, 3),
(38, 13, 3),
(40, 11, 3),
(41, 10, 3),
(42, 9, 3),
(43, 10, 3),
(44, 12, 3);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int NOT NULL,
  `nom` text,
  `prenom` text,
  `email` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `inscription` date DEFAULT NULL,
  `group` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT 'user',
  `password` varchar(35) DEFAULT NULL,
  `verified` tinyint(1) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `nom`, `prenom`, `email`, `inscription`, `group`, `password`, `verified`) VALUES
(1, 'Dupont', 'Alice', 'alice.dupont@example.com', NULL, 'user', 'A1!c3_Dp2025', 1),
(2, 'Martin', 'Thomas', 'thomas.martin@example.com', NULL, 'user', 'T0m@S_Mt2025', 1),
(3, 'Lovelace', 'Ada', 'ada.lovelace@acme.com', NULL, 'admin', 'L0v€l@ce', 1),
(99, 'Système', 'Message', '¨¨', NULL, 'admin', NULL, 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `accverif`
--
ALTER TABLE `accverif`
  ADD PRIMARY KEY (`id`),
  ADD KEY `FK_AuthorID` (`userid`);

--
-- Indexes for table `messages`
--
ALTER TABLE `messages`
  ADD PRIMARY KEY (`id`),
  ADD KEY `messages_rooms_roomid_fk` (`roomID`),
  ADD KEY `messages_users_id_fk` (`author`);

--
-- Indexes for table `rooms`
--
ALTER TABLE `rooms`
  ADD PRIMARY KEY (`roomid`),
  ADD KEY `fk_userowner` (`creatorID`);

--
-- Indexes for table `roomusers`
--
ALTER TABLE `roomusers`
  ADD PRIMARY KEY (`id`),
  ADD KEY `roomusers_users_id_fk` (`userid`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email_2` (`email`),
  ADD KEY `email` (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `accverif`
--
ALTER TABLE `accverif`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `messages`
--
ALTER TABLE `messages`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=61;

--
-- AUTO_INCREMENT for table `rooms`
--
ALTER TABLE `rooms`
  MODIFY `roomid` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `roomusers`
--
ALTER TABLE `roomusers`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=45;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=102;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `messages`
--
ALTER TABLE `messages`
  ADD CONSTRAINT `messages_users_id_fk` FOREIGN KEY (`author`) REFERENCES `users` (`id`);

--
-- Constraints for table `roomusers`
--
ALTER TABLE `roomusers`
  ADD CONSTRAINT `roomusers_users_id_fk` FOREIGN KEY (`userid`) REFERENCES `users` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
