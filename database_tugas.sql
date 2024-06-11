-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 11, 2024 at 11:17 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.1.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `database_tugas`
--

-- --------------------------------------------------------

--
-- Table structure for table `kelompok_12`
--

CREATE TABLE `kelompok_12` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `kota` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `kelompok_12`
--

INSERT INTO `kelompok_12` (`id`, `name`, `kota`) VALUES
(1, 'M Riziq S A', 'Sukabumi'),
(2, 'Naufal ', 'Bogor'),
(3, 'Risyad', 'Bogor'),
(4, 'Angga', 'Bandung'),
(5, 'Alim', 'Jakarta'),
(6, 'Tia', 'Bandung');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `kelompok_12`
--
ALTER TABLE `kelompok_12`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `kelompok_12`
--
ALTER TABLE `kelompok_12`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
