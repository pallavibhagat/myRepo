import csv

def main():

	with open('info.csv') as f:
		f_tsv = csv.reader(f, delimiter='\t')
		for row in f_tsv:
			print row

if __name__ == "__main__":
	main()
