-- phpMyAdmin SQL Dump
-- version 4.6.5.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Gegenereerd op: 28 mrt 2017 om 20:23
-- Serverversie: 10.1.21-MariaDB
-- PHP-versie: 5.6.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
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
-- Tabelstructuur voor tabel `python_data`
--

CREATE TABLE `python_data` (
  `process_id` int(11) NOT NULL,
  `process_name` varchar(50) NOT NULL,
  `process_status` varchar(50) NOT NULL,
  `process_update` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Gegevens worden geëxporteerd voor tabel `python_data`
--

INSERT INTO `python_data` (`process_id`, `process_name`, `process_status`, `process_update`) VALUES
(1, 'python_master_handler 0', 'waiting for command: 1', '2017-03-28 20:23:06');

-- --------------------------------------------------------

--
-- Tabelstructuur voor tabel `python_master_console`
--

CREATE TABLE `python_master_console` (
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
-- Indexen voor tabel `python_data`
--
ALTER TABLE `python_data`
  ADD PRIMARY KEY (`process_id`);

--
-- AUTO_INCREMENT voor geëxporteerde tabellen
--

--
-- AUTO_INCREMENT voor een tabel `python_data`
--
ALTER TABLE `python_data`
  MODIFY `process_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
