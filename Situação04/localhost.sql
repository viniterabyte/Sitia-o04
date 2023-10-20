-- phpMyAdmin SQL Dump
-- version 4.5.4.1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: 20-Out-2023 às 00:16
-- Versão do servidor: 5.7.11
-- PHP Version: 5.6.18

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `bd_situacao04`
--
CREATE DATABASE IF NOT EXISTS `bd_situacao04` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `bd_situacao04`;

-- --------------------------------------------------------

--
-- Estrutura da tabela `tb_financas`
--

CREATE TABLE `tb_financas` (
  `id_fin` int(11) NOT NULL,
  `tipo_mov` varchar(50) NOT NULL,
  `descriçao` varchar(50) NOT NULL,
  `valor` int(11) NOT NULL,
  `categoria` varchar(45) NOT NULL,
  `data_mov` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `tb_financas`
--

INSERT INTO `tb_financas` (`id_fin`, `tipo_mov`, `descriçao`, `valor`, `categoria`, `data_mov`) VALUES
(1, 'asid', 'sadias', 23, 'cada', '2021-12-12'),
(2, 'asid', 'sadias', 23, 'cada', '2021-12-12'),
(3, 'as1', 'asd', 12, 'Real', '2000-01-01');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `tb_financas`
--
ALTER TABLE `tb_financas`
  ADD PRIMARY KEY (`id_fin`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `tb_financas`
--
ALTER TABLE `tb_financas`
  MODIFY `id_fin` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
