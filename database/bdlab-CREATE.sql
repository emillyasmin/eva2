-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema bdlab
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema bdlab
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `bdlab` DEFAULT CHARACTER SET utf8 ;
USE `bdlab` ;

-- -----------------------------------------------------
-- Table `bdlab`.`Usuario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bdlab`.`Usuario` (
  `matricula` BIGINT NOT NULL,
  `nome` VARCHAR(200) NOT NULL,
  `email` VARCHAR(200) NOT NULL,
  `senha` VARCHAR(45) NOT NULL,
  `tipo` INT NOT NULL,
  PRIMARY KEY (`matricula`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `bdlab`.`Emprestimo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bdlab`.`Emprestimo` (
  `codigo` BIGINT NOT NULL AUTO_INCREMENT,
  `tipo` VARCHAR(45) NOT NULL,
  `dt_emp` DATE NOT NULL,
  `dt_devolucao` DATE NULL,
  `Usuario_matricula` BIGINT NOT NULL,
  `status` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`codigo`),
  INDEX `fk_Emprestimo_Usuario2_idx` (`Usuario_matricula` ASC) ,
  CONSTRAINT `fk_Emprestimo_Usuario2`
    FOREIGN KEY (`Usuario_matricula`)
    REFERENCES `bdlab`.`Usuario` (`matricula`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `bdlab`.`Material`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bdlab`.`Material` (
  `codigo` BIGINT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(100) NOT NULL,
  `tipo` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`codigo`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `bdlab`.`Item`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bdlab`.`Item` (
  `codigo` BIGINT NOT NULL AUTO_INCREMENT,
  `disponibilidade` VARCHAR(45) NOT NULL,
  `observacao` VARCHAR(250) NULL,
  `localizacao` VARCHAR(200) NULL,
  `Material_codigo` BIGINT NOT NULL,
  `Emprestimo_codigo` BIGINT NULL,
  PRIMARY KEY (`codigo`),
  INDEX `fk_Item_Emprestimo2_idx` (`Emprestimo_codigo` ASC) ,
  INDEX `fk_Item_Material2_idx` (`Material_codigo` ASC) ,
  CONSTRAINT `fk_Item_Emprestimo2`
    FOREIGN KEY (`Emprestimo_codigo`)
    REFERENCES `bdlab`.`Emprestimo` (`codigo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Item_Material2`
    FOREIGN KEY (`Material_codigo`)
    REFERENCES `bdlab`.`Material` (`codigo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `bdlab`.`Emprestimo_has_Item`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bdlab`.`Emprestimo_has_Item` (
  `Emprestimo_codigo` BIGINT NOT NULL,
  `Item_codigo` BIGINT NOT NULL,
  PRIMARY KEY (`Emprestimo_codigo`, `Item_codigo`),
  INDEX `fk_Emprestimo_has_Item_Item1_idx` (`Item_codigo` ASC) ,
  INDEX `fk_Emprestimo_has_Item_Emprestimo1_idx` (`Emprestimo_codigo` ASC) ,
  CONSTRAINT `fk_Emprestimo_has_Item_Emprestimo1`
    FOREIGN KEY (`Emprestimo_codigo`)
    REFERENCES `bdlab`.`Emprestimo` (`codigo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Emprestimo_has_Item_Item1`
    FOREIGN KEY (`Item_codigo`)
    REFERENCES `bdlab`.`Item` (`codigo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `bdlab`.`Usuario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bdlab`.`Usuario` (
  `matricula` BIGINT NOT NULL,
  `nome` VARCHAR(200) NOT NULL,
  `email` VARCHAR(200) NOT NULL,
  `senha` VARCHAR(45) NOT NULL,
  `tipo` INT NOT NULL,
  PRIMARY KEY (`matricula`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `bdlab`.`Emprestimo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bdlab`.`Emprestimo` (
  `codigo` BIGINT NOT NULL AUTO_INCREMENT,
  `tipo` VARCHAR(45) NOT NULL,
  `dt_emp` DATE NOT NULL,
  `dt_devolucao` DATE NULL,
  `Usuario_matricula` BIGINT NOT NULL,
  `status` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`codigo`),
  INDEX `fk_Emprestimo_Usuario2_idx` (`Usuario_matricula` ASC) ,
  CONSTRAINT `fk_Emprestimo_Usuario2`
    FOREIGN KEY (`Usuario_matricula`)
    REFERENCES `bdlab`.`Usuario` (`matricula`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `bdlab`.`Material`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bdlab`.`Material` (
  `codigo` BIGINT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(100) NOT NULL,
  `tipo` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`codigo`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `bdlab`.`Item`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bdlab`.`Item` (
  `codigo` BIGINT NOT NULL AUTO_INCREMENT,
  `disponibilidade` VARCHAR(45) NOT NULL,
  `observacao` VARCHAR(250) NULL,
  `localizacao` VARCHAR(200) NULL,
  `Material_codigo` BIGINT NOT NULL,
  `Emprestimo_codigo` BIGINT NULL,
  PRIMARY KEY (`codigo`),
  INDEX `fk_Item_Emprestimo2_idx` (`Emprestimo_codigo` ASC) ,
  INDEX `fk_Item_Material2_idx` (`Material_codigo` ASC) ,
  CONSTRAINT `fk_Item_Emprestimo2`
    FOREIGN KEY (`Emprestimo_codigo`)
    REFERENCES `bdlab`.`Emprestimo` (`codigo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Item_Material2`
    FOREIGN KEY (`Material_codigo`)
    REFERENCES `bdlab`.`Material` (`codigo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
