# 有打*字號的為目前暫定標準(待確認合理性)
# TODO: 目前暫時在螢幕輸出，到時候應該要反饋給感測器閃燈
# 輸入檔案內容一行為一次拍擊，感測器輸出數值以空白分隔（其實空行沒關係xD）
import math
z_standard = -1
def str_to_list(force_string):
	#####################
	# input : string    #
	# output : int list #
	#####################
	try:
		force_list = force_string.split()
		return [int(force) for force in force_list]
	except:
		return []

class force_data():
	####################################
	# varable:                         #
	#     mean      : mean             #
	#     sigma2    : variance         #
	#     data_list : list of int list #
	# function:                        #
	#     __init__ :                   #
	#         input : string list      #
	#     add_init_data :              #
	#         input : string list      #
	#         return : none            #
	#         rewrite : mean, sigma2   #
	####################################
	def __init__(self, init_list):
		# 考慮力道，單一次拍擊時間
		# 力道部份：
		# TODO: 到時候請醫生拍擊最小的合格力道，並將其視為常態分佈，以平均值估算最初正確的力道分界
		# * 以6/1下午那筆測試資料來做（假設大約84%的力道正確，即Z分數>-1則認為正確）
		# 拍擊時間：
		# * 拍擊時間使感測器顯示2~3次數值
		self.mean = 0
		self.sigma2 = 0
		self.data_list = []
		for force_list in init_list:
			if self.add_init_data(force_list) == None:
				print("add data failed")

	def add_init_data(self,force_list):
		force = str_to_list(force_list)
		length = len(force)
		if length == 0:
			print(force,"string format error or empty string") # ....
			return None
		mean = 0
		for f in force:
			mean += f
		mean /= length
		size = len(self.data_list)
		square_sum = (self.sigma2 + self.mean ** 2) * size + mean ** 2
		self.mean = (size * self.mean + mean) / (size + 1)
		self.sigma2 = square_sum / (size + 1) - self.mean ** 2
		self.data_list.append(force)
		return True

def check_data(force_list):
	#######################################
	# input: int list                     #
	# return: none                        #
	# rewrite: none                       #
	# print: whether about force and time #
	#######################################
	length=len(force_list)
	if length == 0:
		return None
	print(force_list)
	if length < 2:
		print("	too short")
	elif length > 3:
		print("	too long")
	mean = 0
	for force in force_list:
		mean += force
	mean /= length
	z_score = (mean-data.mean) / math.sqrt(data.sigma2)
	if z_score > z_standard:
		print("	force OK")
	else:
		print("	QQ")

if __name__=='__main__':
	datafile = open('force_data.txt'); # 丟同一個資料夾喔owo
	data_list = datafile.readlines()
	data = force_data(data_list)
	datafile.close()
	while 1:
		try:
			test=input('data: ') # TODO: connect App (?
			check_data(str_to_list(test))
		except:
			pass

# 我是彩蛋(X)
def meow():
	print('''
          #    #
         #     #
       ##### #####
         #     #      #   # ###
####     #     #       # #  #  #
#  #                    #   #  #
#  #    #########      # #  #  #
####    #   #   #     #   # ###
        #########
        #   #   #
        #########
''')
#meow()
