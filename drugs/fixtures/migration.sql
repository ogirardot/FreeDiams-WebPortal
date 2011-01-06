create database openreact;
	
	-- rename :
	alter table COMPOSITION rename drugs_composition;
	alter table DRUG_ROUTES rename drugs_drugroute;
	alter table PACKAGING rename drug_packaging;
	alter table ROUTE_SYNONYMS rename drugs_routesynonym;
	alter table DB_SCHEMA_VERSION rename drugs_dbschemaversion;
	alter table INFORMATIONS rename drugs_information;
	alter table ROUTES rename drugs_route;
	alter table SEARCH_ENGINES rename drugs_searchengine;
	alter table DRUGS rename drugs_drug;
	alter table LK_MOL_ATC rename drugs_lkmolatc;
	alter table ROUTE_ABBREV rename drugs_routeabbrev;     
	
	-- add primary keys :
	ALTER TABLE `drugs_composition` ADD ID INT UNSIGNED NOT NULL AUTO_INCREMENT,
	  ADD PRIMARY KEY (ID);
	ALTER TABLE `drugs_drugroute` ADD ID INT UNSIGNED NOT NULL AUTO_INCREMENT,
	  ADD PRIMARY KEY (ID);
	ALTER TABLE `drugs_dbschemaversion` ADD ID INT UNSIGNED NOT NULL AUTO_INCREMENT,
	  ADD PRIMARY KEY (ID);             
	ALTER TABLE `drugs_information` ADD ID INT UNSIGNED NOT NULL AUTO_INCREMENT,
	  ADD PRIMARY KEY (ID);
	ALTER TABLE `drugs_packaging` ADD ID INT UNSIGNED NOT NULL AUTO_INCREMENT,
	  ADD PRIMARY KEY (ID);
	ALTER TABLE `drugs_lk_mol_atc` ADD ID INT UNSIGNED NOT NULL AUTO_INCREMENT,
	  ADD PRIMARY KEY (ID);