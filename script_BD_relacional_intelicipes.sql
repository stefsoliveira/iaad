create schema BD_INTELICIPES;
use BD_INTELICIPES;

create table RECIPE(
	id INT(32),
	name_recipe VARCHAR(64),
	minutes INT(32),
	n_steps INT(32),
	n_ingredients INT(32),
	description_recipe VARCHAR(800),
	PRIMARY KEY(id));

create table INTERACTION(
	user_id  INT(32),
	recipe_id  INT(32),
	date  DATE,
	rating  INT(32),
	review VARCHAR(800),
	PRIMARY KEY(user_id));

create table RECIPE_NUTRITION(
	recipe_id  INT(32),
	calories FLOAT(32),
	total_fat FLOAT(32),
	sugar FLOAT(32),
	sodium FLOAT(32),
	protein FLOAT(32),
	saturated_fat FLOAT(32),
	PRIMARY KEY(recipe_id));

create table RECIPE_CLASSIFICATION(
	recipe_id INT(32),
	classification_id INT(32),
	classification_group VARCHAR(32),
	PRIMARY KEY(recipe_id));

alter table INTERACTION ADD FOREIGN KEY(recipe_id) REFERENCES RECIPE(id);
alter table RECIPE_NUTRITION ADD FOREIGN KEY(recipe_id) REFERENCES RECIPE(id);
alter table RECIPE_CLASSIFICATION ADD FOREIGN KEY(recipe_id) REFERENCES RECIPE(id);
