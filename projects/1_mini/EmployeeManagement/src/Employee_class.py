
class Employee:

	def __init__(self, full_name: str, age: int, sex: str, nickname=''):  # type hinting with default arg?
		self.first, self.middle, self.last = self.parse_name(full_name)
		self.age = int(age)
		self.sex = self.get_sex(sex)
		self.title = self.get_title(self.sex)
		self.nickname = nickname


	@staticmethod
	def parse_name(full_name: str):
		names_lst = [''] * 3
		for i, name_entry in enumerate(full_name.split(' ')):
			names_lst[i] = name_entry

		num_entries = i + 1

		if num_entries == 2:
			names_lst[1:] = names_lst[1:][::-1]  # A better way of reversing?

		return(names_lst)


	@staticmethod
	def get_sex(sex: str):
		'''
		Male -> M
		Female -> F
		'''

		# DRY it!
		if sex in ['Male', 'male', 'M', 'm']:
			sex = 'M'
		elif sex in ['Female', 'female, F', 'f']:
			sex = 'F'

		return(sex)

	@staticmethod
	def get_title(sex: str):
		'''
		M -> Mr.
		F -> Mrs.
		'''
		# Any way to check to use get_sex without removing staticmethod?
		title = {'M': 'Mr.', 'F': 'Mrs'}.get(sex)

		return(title)


	@property
	def full_name(self):
		names_lst = [self.first, self.middle, self.last]
		names_lst = list(filter(lambda x: x!= '', names_lst))

		full_name = ' '.join(names_lst)
		return(full_name)

	@property
	def formal_name(self):
		frml_name = f'{self.title} '
		if (self.middle == '') and (self.last == ''):
			frml_name += self.first
		elif (self.middle == ''):
			frml_name += f'{self.first[0]}. {self.last}'
		else:
			frml_name += f'{self.first[0]}.{self.middle[0]}. {self.last}'

		return(frml_name)



	def introduce(self):

		msg = f'Hello I am {self.first}! '
		msg += f'Formally I am addressed as {self.formal_name}. '
		msg += f'But you can call me, '
		msg += f'{self.nickname}!' if self.nickname != '' \
			   else f'well {self.first} only cuz I don\'t have a nickname!'

		print(msg)

		if self.nickname == '':
			if input('Do you wish to give me a nickname? (y/n)\t') in ('y', 'yes'):
				self.nickname = input('Enter nickname.\t')


	def get_attr_str(self, attrs: list):
		attr_lst = []
		for attr_name in attrs:
			attr = self.__getattribute__(attr_name)

			if type(attr) is str:
				attr_val = f"'{attr}'"
			else:
				attr_val = f"{attr}"


			attr_lst.append(f"{attr_name}={attr_val}")

		attr_str = ', '.join(attr_lst)

		return(attr_str)


	def __repr__(self):
		return(f"Employee({self.get_attr_str(('full_name', 'age', 'sex', 'nickname'))})")



if __name__ == '__main__':
	emp = Employee('Abhishek Bhatia', 25, 'M')
