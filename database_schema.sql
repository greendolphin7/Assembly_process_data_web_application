-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema projectdata
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema projectdata
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `projectdata` DEFAULT CHARACTER SET utf8 ;
USE `projectdata` ;

-- -----------------------------------------------------
-- Table `projectdata`.`product_history`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `projectdata`.`product_history` (
  `product_key` VARCHAR(45) NOT NULL,
  `product_code` VARCHAR(45) NULL DEFAULT NULL,
  `product_timestamp` DATETIME NULL DEFAULT NULL,
  PRIMARY KEY (`product_key`),
  INDEX `product_code` (`product_code` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `projectdata`.`machine`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `projectdata`.`machine` (
  `machine_code` VARCHAR(45) NOT NULL,
  `product_key` VARCHAR(45) NOT NULL,
  `start_time` DATETIME NOT NULL,
  `end_time` DATETIME NOT NULL,
  `makespan` FLOAT NOT NULL,
  `process_time` FLOAT NOT NULL,
  `machine_data` FLOAT NOT NULL,
  `machine_data_code` VARCHAR(45) NOT NULL,
  INDEX `product_key` (`product_key` ASC) VISIBLE,
  INDEX `machine_ibfk_2_idx` (`machine_code` ASC) VISIBLE,
  CONSTRAINT `machine_ibfk_1`
    FOREIGN KEY (`product_key`)
    REFERENCES `projectdata`.`product_history` (`product_key`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `projectdata`.`machine_master`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `projectdata`.`machine_master` (
  `machine_code` VARCHAR(45) NOT NULL,
  `machine_class` VARCHAR(45) NOT NULL,
  `machine_assembly` VARCHAR(45) NOT NULL,
  `machine_process_time` VARCHAR(45) NOT NULL,
  `machine_data_code` VARCHAR(45) NOT NULL)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `projectdata`.`master`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `projectdata`.`master` (
  `p_code` VARCHAR(10) NOT NULL,
  `p_class` VARCHAR(45) NOT NULL,
  `p_num` VARCHAR(45) NOT NULL,
  `m_code` VARCHAR(45) NULL DEFAULT NULL,
  `m_class` VARCHAR(45) NULL DEFAULT NULL,
  `m_assembly` VARCHAR(45) NULL DEFAULT NULL,
  `m_data_code` VARCHAR(45) NULL DEFAULT NULL,
  `m_process_time` VARCHAR(45) NULL DEFAULT NULL,
  `p_quality` VARCHAR(10) NULL DEFAULT NULL,
  `p_target_l` VARCHAR(45) NULL DEFAULT NULL,
  `p_target_w` VARCHAR(45) NULL DEFAULT NULL,
  `p_target_h` VARCHAR(45) NULL DEFAULT NULL)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `projectdata`.`product_master`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `projectdata`.`product_master` (
  `product_code` VARCHAR(45) NOT NULL,
  `product_name` VARCHAR(45) NOT NULL,
  `product_class` VARCHAR(45) NOT NULL,
  `product_num` VARCHAR(45) NOT NULL,
  `product_target_l` VARCHAR(45) NULL DEFAULT NULL,
  `product_target_w` VARCHAR(45) NULL DEFAULT NULL,
  `product_targer_h` VARCHAR(45) NULL DEFAULT NULL)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `projectdata`.`product_quality`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `projectdata`.`product_quality` (
  `product_key` VARCHAR(45) NULL DEFAULT NULL,
  `product_size_l` FLOAT NOT NULL,
  `product_size_w` FLOAT NOT NULL,
  `product_size_h` FLOAT NOT NULL,
  `product_test` VARCHAR(45) NULL DEFAULT NULL,
  `product_test_timestamp` DATETIME NOT NULL,
  INDEX `product_key` (`product_key` ASC) VISIBLE,
  CONSTRAINT `product_quality_ibfk_1`
    FOREIGN KEY (`product_key`)
    REFERENCES `projectdata`.`product_history` (`product_key`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
