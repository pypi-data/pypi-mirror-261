import sqlite3 as sq
import traceback
from typing import Any




class RegRequests:
	# Функция получения БД
	# parameters: str(tuple(str(SQLtypes_vars, )))
	# Параметры должны быть строкой из кортеж из строки CQL команд, точнее сказать SQL переменны, в которые будет происходить запись
	def get_db(dataBase: str, table_name: str, columns: str) -> bool:

		# Пробуем подключиться к БД, создаем записи, если их нет и возвращаем истину
		try:
			# Пока Бд открыта - делаем свои делишки!
			with sq.connect(dataBase) as conn:
				cur = conn.cursor()
				cur.execute(f"CREATE TABLE IF NOT EXISTS {table_name} {columns}")
				cur.close()

				return True

		# При исключение возвращаем ложь
		except:
			print(traceback.format_exc())
			return False


	# Функция записи в БД
	def insert_to_db(dataBase: str, table_name: str, parameters: list) -> bool:
		# Пробуем в цикле отформатировать полученную строку и записать ее в БД
		try:
			lp = len(parameters)

			parameters_as_str = ""

			for i in range(lp):
				if i < lp-1:
					parameters_as_str += f"'{parameters[i]}', "

				else:
					parameters_as_str += f"'{parameters[i]}'"

			# Пока Бд открыта - делаем свои делишки!
			with sq.connect(dataBase) as conn:
				cur = conn.cursor()
				cur.execute(f"INSERT INTO {table_name} VALUES({parameters_as_str})")
				cur.close()
				conn.commit()

				return True

		# При исключение возвращаем ложь
		except:
			print(traceback.format_exc())
			return False


	# Функция записи в БД
	def insert_to_db_one_par(dataBase: str, table_name: str, column_name: str, parameter: str) -> bool:# Параматры следует передавать так: "'parameters'"
		try:
			# Пока Бд открыта - делаем свои делишки!
			with sq.connect(dataBase) as conn:
				cur = conn.cursor()
				cur.execute(f"INSERT INTO {table_name} ({column_name}) VALUES({parameter})")
				cur.close()
				conn.commit()

				return True

		# При исключение возвращаем ложь
		except:
			print(traceback.format_exc())
			return False


	# Функция получения всего при конкретной записи
	def fetch_all_where(dataBase: str, table_name: str, condition: str, condition_value: str | int) -> list[dict] | None:
		# Пробуем получить все данные расположенные при конкретной записи
		try:
			# Пока Бд открыта - делаем свои делишки!
			with sq.connect(dataBase) as conn:
				cur = conn.cursor()
				all_ = cur.execute(f"SELECT * FROM {table_name} WHERE {condition}='{condition_value}'")
				all_ = all_.fetchall()
				cur.close()
				
				if all_ == []:
					return None

				return all_

		# При исключение возвращаем NoneType
		except:
			print(traceback.format_exc())
			return None


	# Функция получения всего
	def fetch_all(dataBase: str, table_name: str) -> list[dict] | None:
		# Пробуем получить все данные
		try:
			# Пока Бд открыта - делаем свои делишки!
			with sq.connect(dataBase) as conn:
				cur = conn.cursor()
				all_ = cur.execute(f"SELECT * FROM {table_name}")
				all_ = all_.fetchall()
				cur.close()

				if all_ == []:
					return None

				return all_

		# При исключение возвращаем NoneType
		except:
			print(traceback.format_exc())
			return None


	# Функция для получения одного элемента из БД
	def fetch_one(dataBase: str, table_name: str, column_name: str, condition: str, condition_value: str | int) -> Any | None:
		# Пробуем получить элемент при конкретной записи
		try:
			# Пока Бд открыта - делаем свои делишки!
			with sq.connect(dataBase) as conn:
				cur = conn.cursor()
				one_ = cur.execute(f"SELECT {column_name} FROM {table_name} WHERE {condition}='{condition_value}'")
				one_ = one_.fetchone()
				cur.close()	

				# Если записи нет, возвращаем NoneType
				if one_ == None:
					return None

				#Указываем, что возвращаем первый элемент из tuple с одним элементом
				return one_[0]

		# При исключение возвращаем NoneType
		except:
			print(traceback.format_exc())
			return None



	# Функция для получения всех элементов одного столбца из БД
	def fetch_one_column(dataBase: str, table_name: str, column_name: str, condition: str, condition_value: str | int) -> tuple | None:
		# Пробуем получить элемент при конкретной записи
		try:
			# Пока Бд открыта - делаем свои делишки!
			with sq.connect(dataBase) as conn:
				cur = conn.cursor()
				one_ = cur.execute(f"SELECT {column_name} FROM {table_name} WHERE {condition}='{condition_value}'")
				one_ = one_.fetchone()
				cur.close()	

				# Если записи нет, возвращаем NoneType
				if one_ == None:
					return None

				#Указываем, что возвращаем tuple
				return one_

		# При исключение возвращаем NoneType
		except:
			print(traceback.format_exc())
			return None



	def exists_test(dataBase: str, table_name: str) -> bool:
		# Проверяем таблицу на существование
		try:
			# Пока Бд открыта - делаем свои делишки!
			with sq.connect(dataBase) as conn:
				cur = conn.cursor()
				exists = cur.execute(f"SELECT EXISTS(SELECT * FROM {table_name})")
				cur.close()

				return exists

		# При исключение возвращаем ложь
		except:
			print(traceback.format_exc())
			return False


	# Функция обновления элемента в таблице БД
	def update_table(dataBase: str, table_name: str, column_name: str, new_meaning: str | int, condition: str, condition_value: str | int) -> bool:
		# Побуем заапдейтить элемент
		try:
			# Пока Бд открыта - делаем свои делишки!
			with sq.connect(dataBase) as conn:
				cur = conn.cursor()
				cur.execute(f"UPDATE {table_name} SET {column_name}={new_meaning} WHERE {condition}='{condition_value}'")
				cur.close()
				conn.commit()

				return True

		# При исключение возвращаем ложь
		except:
			print(traceback.format_exc())
			return False


	# Функция удаляет элемент из таблицы в БД
	def delete_from_table(dataBase: str, table_name: str, condition: str, condition_value: str | int) -> bool:
		# Пробуем удалить информацию из таблицы из БД в конкретном месте
		try:
			# Пока Бд открыта - делаем свои делишки!
			with sq.connect(dataBase) as conn:
				cur = conn.cursor()
				cur.execute(f"DELETE FROM {table_name} WHERE {condition}='{condition_value}'")
				cur.close()
				conn.commit()

				return True

		# При исключение возвращаем ложь
		except:
			print(traceback.format_exc())
			return False


	# Функция удаляет целиком таблицу из БД
	def delete_table(dataBase: str, table_name: str) -> bool:
		# Пробуем удалить таблицу из БД
		try:
			# Пока Бд открыта - делаем свои делишки!
			with sq.connect(dataBase) as conn:
				cur = conn.cursor()
				cur.execute(f"DROP TABLE {table_name}")
				cur.close()

				return True

		# При исключение возвращаем ложь
		except:
			print(traceback.format_exc())
			return False





class MultiConditionsRequests():
	# Функция получения всего при конкретной записи
	def fetch_all_where(dataBase: str, table_name: str, condition: list, condition_value: list) -> list[dict] | None:
		# Пробуем получить все данные расположенные при конкретной записи
		try:
			# Пока Бд открыта - делаем свои делишки!
			with sq.connect(dataBase) as conn:
				for i in range(condition):
					if i == 0:
						command = f"SELECT {column_name} FROM {table_name} WHERE {condition[i]}='{condition_value[i]}'"

					else:
						command += f" AND {condition[i]}='{condition_value[i]}'"

				cur = conn.cursor()
				all_ = cur.execute(command)
				all_ = all_.fetchall()
				cur.close()
				
				if all_ == []:
					return None

				return all_

		# При исключение возвращаем NoneType
		except:
			print(traceback.format_exc())
			return None



		# Функция для получения одного элемента из БД
	def fetch_one(dataBase: str, table_name: str, column_name: str, condition: list, condition_value: list) -> Any | None:
		# Пробуем получить элемент при конкретной записи
		try:
			# Пока Бд открыта - делаем свои делишки!
			with sq.connect(dataBase) as conn:
				for i in range(condition):
					if i == 0:
						command = f"SELECT {column_name} FROM {table_name} WHERE {condition[i]}='{condition_value[i]}'"

					else:
						command += f" AND {condition[i]}='{condition_value[i]}'"

				cur = conn.cursor()
				one_ = cur.execute(command)
				one_ = one_.fetchone()
				cur.close()	

				# Если записи нет, возвращаем NoneType
				if one_ == None:
					return None

				#Указываем, что возвращаем первый элемент из tuple с одним элементом
				return one_[0]

		# При исключение возвращаем NoneType
		except:
			print(traceback.format_exc())
			return None



	# Функция для получения всех элементов одного столбца из БД
	def fetch_one_column(dataBase: str, table_name: str, column_name: str, condition: list, condition_value: list) -> tuple | None:
		# Пробуем получить элемент при конкретной записи
		try:
			# Пока Бд открыта - делаем свои делишки!
			with sq.connect(dataBase) as conn:
				for i in range(condition):
					if i == 0:
						command = f"SELECT {column_name} FROM {table_name} WHERE {condition[i]}='{condition_value[i]}'"

					else:
						command += f" AND {condition[i]}='{condition_value[i]}'"

				cur = conn.cursor()
				one_ = cur.execute(command)
				one_ = one_.fetchone()
				cur.close()	

				# Если записи нет, возвращаем NoneType
				if one_ == None:
					return None

				#Указываем, что возвращаем tuple
				return one_

		# При исключение возвращаем NoneType
		except:
			print(traceback.format_exc())
			return None



		# Функция обновления элемента в таблице БД
	def update_table(dataBase: str, table_name: str, column_name: str, new_meaning: str | int, condition: list, condition_value: list) -> bool:
		# Побуем заапдейтить элемент
		try:
			# Пока Бд открыта - делаем свои делишки!
			with sq.connect(dataBase) as conn:
				for i in range(condition):
					if i == 0:
						command = f"UPDATE {table_name} SET {column_name}='{new_meaning}' WHERE {condition[i]}='{condition_value[i]}'"

					else:
						command += f" AND {condition[i]}='{condition_value[i]}'"

				cur = conn.cursor()
				cur.execute(command)
				cur.close()
				conn.commit()

				return True

		# При исключение возвращаем ложь
		except:
			print(traceback.format_exc())
			return False


	# Функция удаляет элемент из таблицы в БД
	def delete_from_table(dataBase: str, table_name: str, condition: list, condition_value: list) -> bool:
		# Пробуем удалить информацию из таблицы из БД в конкретном месте
		try:
			# Пока Бд открыта - делаем свои делишки!
			with sq.connect(dataBase) as conn:
				for i in range(condition):
					if i == 0:
						command = f"SELECT {column_name} FROM {table_name} WHERE {condition[i]}='{condition_value[i]}'"

					else:
						command += f" AND {condition[i]}='{condition_value[i]}'"

				cur = conn.cursor()
				cur.execute(command)
				cur.close()
				conn.commit()

				return True

		# При исключение возвращаем ложь
		except:
			print(traceback.format_exc())
			return False












