-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema arbortrary
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema arbortrary
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `arbortrary` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `arbortrary` ;

-- -----------------------------------------------------
-- Table `arbortrary`.`users`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `arbortrary`.`users` ;

CREATE TABLE IF NOT EXISTS `arbortrary`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) CHARACTER SET 'utf8mb3' NULL DEFAULT NULL,
  `last_name` VARCHAR(45) CHARACTER SET 'utf8mb3' NULL DEFAULT NULL,
  `email` VARCHAR(100) CHARACTER SET 'utf8mb3' NULL DEFAULT NULL,
  `password` VARCHAR(45) CHARACTER SET 'utf8mb3' NULL DEFAULT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 2
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `arbortrary`.`trees`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `arbortrary`.`trees` ;

CREATE TABLE IF NOT EXISTS `arbortrary`.`trees` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `species` VARCHAR(45) CHARACTER SET 'utf8mb3' NULL DEFAULT NULL,
  `location` VARCHAR(45) CHARACTER SET 'utf8mb3' NULL DEFAULT NULL,
  `reason` VARCHAR(45) CHARACTER SET 'utf8mb3' NULL DEFAULT NULL,
  `date_planted` DATETIME NULL DEFAULT NULL,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_trees_users_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_trees_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `arbortrary`.`users` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
