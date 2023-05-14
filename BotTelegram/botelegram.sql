-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Creato il: Apr 26, 2023 alle 11:32
-- Versione del server: 10.4.27-MariaDB
-- Versione PHP: 8.0.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `botelegram`
--

-- --------------------------------------------------------

--
-- Struttura della tabella `impianti`
--

CREATE TABLE `impianti` (
  `idImpianto` int(11) NOT NULL,
  `Gestore` varchar(20) NOT NULL,
  `Bandiera` varchar(12) NOT NULL,
  `TipoImpianto` varchar(12) NOT NULL,
  `NomeImpianto` varchar(12) NOT NULL,
  `Indirizzo` varchar(30) NOT NULL,
  `Comune` varchar(12) NOT NULL,
  `Provincia` varchar(2) NOT NULL,
  `Latitudine` float NOT NULL,
  `Longitudine` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struttura della tabella `prezzi`
--

CREATE TABLE `prezzi` (
  `idImp` int(11) NOT NULL,
  `descCarburante` varchar(12) NOT NULL,
  `prezzo` float NOT NULL,
  `isSelf` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struttura della tabella `utente`
--

CREATE TABLE `utente` (
  `id` int(11) NOT NULL,
  `user` varchar(11) NOT NULL,
  `serbatoio` int(11) NOT NULL,
  `tipo` varchar(16) NOT NULL,
  `chatID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Indici per le tabelle scaricate
--

--
-- Indici per le tabelle `impianti`
--
ALTER TABLE `impianti`
  ADD PRIMARY KEY (`idImpianto`);

--
-- Indici per le tabelle `prezzi`
--
ALTER TABLE `prezzi`
  ADD KEY `benzinaiID` (`idImp`);

--
-- Indici per le tabelle `utente`
--
ALTER TABLE `utente`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT per le tabelle scaricate
--

--
-- AUTO_INCREMENT per la tabella `impianti`
--
ALTER TABLE `impianti`
  MODIFY `idImpianto` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT per la tabella `utente`
--
ALTER TABLE `utente`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Limiti per le tabelle scaricate
--

--
-- Limiti per la tabella `prezzi`
--
ALTER TABLE `prezzi`
  ADD CONSTRAINT `benzinaiID` FOREIGN KEY (`idImp`) REFERENCES `impianti` (`idImpianto`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
