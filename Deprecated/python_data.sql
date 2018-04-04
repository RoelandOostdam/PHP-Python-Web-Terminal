-- phpMyAdmin SQL Dump
-- version 4.7.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Gegenereerd op: 02 okt 2017 om 19:07
-- Serverversie: 10.1.25-MariaDB
-- PHP-versie: 5.6.31

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `python_data`
--

-- --------------------------------------------------------

--
-- Tabelstructuur voor tabel `python_config`
--

CREATE TABLE `python_config` (
  `response_time` int(11) NOT NULL DEFAULT '1000'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Gegevens worden geëxporteerd voor tabel `python_config`
--

INSERT INTO `python_config` (`response_time`) VALUES
(100);

-- --------------------------------------------------------

--
-- Tabelstructuur voor tabel `python_data`
--

CREATE TABLE `python_data` (
  `process_id` int(11) NOT NULL,
  `process_name` varchar(50) NOT NULL,
  `process_status` varchar(50) NOT NULL,
  `process_update` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Tabelstructuur voor tabel `python_master_console`
--

CREATE TABLE `python_master_console` (
  `id` int(11) NOT NULL,
  `console_time` datetime NOT NULL,
  `console_line` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Tabelstructuur voor tabel `python_remote_handler`
--

CREATE TABLE `python_remote_handler` (
  `thread` int(11) NOT NULL,
  `process_name` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indexen voor geëxporteerde tabellen
--

--
-- Indexen voor tabel `python_config`
--
ALTER TABLE `python_config`
  ADD PRIMARY KEY (`response_time`);

--
-- Indexen voor tabel `python_data`
--
ALTER TABLE `python_data`
  ADD PRIMARY KEY (`process_id`);

--
-- Indexen voor tabel `python_master_console`
--
ALTER TABLE `python_master_console`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT voor geëxporteerde tabellen
--

--
-- AUTO_INCREMENT voor een tabel `python_data`
--
ALTER TABLE `python_data`
  MODIFY `process_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT voor een tabel `python_master_console`
--
ALTER TABLE `python_master_console`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
