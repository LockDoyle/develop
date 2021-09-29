
#self ⇒ instance自身
class test():
	def __init__(self):
		self.strA = 'test'
		
	def main(self):
		self.math()

	def math(self):
		a:int
		b:int

		a = 2
		b = 3

		print(a * b)
		print(self.strA)
		
t=test() # ()がないと、暗黙的にselfが引数に設定されない test()が正解
t.main()