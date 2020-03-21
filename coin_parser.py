from selenium import webdriver
import csv
from datetime import datetime
from matplotlib import pyplot as plt
# matplotlib.pyplot import
def get_coin_price():
	coins=[]
	price_of_coins=[]
	column_list = ["한글","영문", "현재가", "전일대비", "거래량"]
	now = datetime.now()
	time_list = [str("{}월{}일".format(now.month, now.day)), str(now.hour)+"시", str(now.minute)+"분", str(now.second)+"초"]
	today = str(datetime.now().day)
	nowtime = str(datetime.now().microsecond)
	with open('coin_'+today+nowtime+'.csv', 'w', -1, newline='')as coin:
		w = csv.writer(coin)
		w.writerow(time_list)
		w.writerow(column_list)

		URL = "https://www.gopax.co.kr"
		driver = webdriver.Chrome("C:\\Users\\woqls\\Desktop\\수업\\chromedriver_win32\\chromedriver.exe")
		driver.implicitly_wait(10)
		driver.get(URL)

		depth1 = driver.find_element_by_xpath("//*[@id=\"react\"]/div/div[1]/div[2]/div[2]/div[2]/table/tbody")
		depth2 = depth1.find_elements_by_tag_name("tr")
		for td in depth2:
			coin_row = td.text
			coin_row_list = coin_row.split("\n")
			w.writerow(coin_row_list)
			coins.append(coin_row_list[0]+" / "+coin_row_list[1])
			price_of_coins.append(coin_row_list[2])
			print("[{0} / {1}] PRICE : {2}, RATIO : {3}, VOULUMN : {4}".format(coin_row_list[0],coin_row_list[1],coin_row_list[2],coin_row_list[3],coin_row_list[4]))
	return coins, price_of_coins
def make_graph(coins, prices):
	width = 1/500 #width설정
	plt.bar(coins, prices, width, color = "blue") #막대그래프 그리기
	plt.ylabel("#prices")
	plt.xlabel("coins")
	plt.title("BLOCKCHAIN VIRTUAL BILLS")
	plt.show()
def main():
	coins, price_of_coins = get_coin_price()
	#make_graph(coins, price_of_coins)
if __name__ == '__main__':
	main()

