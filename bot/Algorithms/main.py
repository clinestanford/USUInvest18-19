
from AlgoDriver import AlgoDriver
from Alpaca import Alpaca
from Config import ALPACA_CONFIG

def main():

	#Alpaca(key, secretKey, isPaper)
	alpaca = Alpaca(ALPACA_CONFIG['key'], ALPACA_CONFIG['secretKey'], True)

	algoDriver = AlgoDriver(alpaca)

	##### this is where you add/remove strategies

	# algoDriver.addStrategy(SimgpleMACD())



	#### done adding strategies

	algoDriver.buyAndSell()

	print(ALPACA_CONFIG['key'])

if __name__ == '__main__':
	main()