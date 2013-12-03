#rom numpy import *
#rom sklearn.datasets import load_svmlight_file
#rom sklearn.datasets import dump_svmlight_file
#mport scipy.sparse

class GrowingList(list):
	def __setitem__(self, index, value):
		if index >= len(self):
			self.extend([0] * (index + 1 - len(self)))
		list.__setitem__(self, index, value)

class SimpleModule:
	def __init__(self):
		self.table = None

	#Reads the training data, creates the array, outputs a file
	def train(self):
		clicklist = GrowingList()
		clicklist[1] = 0 #initializes it, doesn't like to play nice w/o it 
		training_file = "train"#"data/trailhead20k" #"../data/train"
		
		#while training_chunk in read_in_chunks(open(training_file)):
#		split_chunk = training_chunk.split("\n")
		
		urldomainmap = [(0, 0)] * 10 
		for line in open(training_file):
			element = line.split("\t") 

			# Update URL Domain Map if we get a new query
			if (element[2] == "Q"):
				#starting with 6...
				for i in range(10):
					[url, domain] = element[i + 6].split(",")
					#print("URL: " + url + ", Domain: " + domain)
					urldomainmap[i] = (url, domain)

			# Enter module specific data here. 
			if (element[2] == "C"):
				# Debugging variable
				found = False 
				#print(str(element[4]))

				#Find the relevant domain name.
				for (url, domain) in urldomainmap:
					#Iterate.
					#print("TEST: " + url +" against: " + element[4])
					if (int(url) == int(element[4])):
						#print("what")
						try:
							clicklist[int(domain)] += 1
						except:
							clicklist[int(domain)] = 1
						found = True

				#if not(found):
				#	print "Found error in URL Domain Map at ", element[0]
				#else: 
				#	print "Nothing wrong :D"

		# Output that file.
		self.table = clicklist

		f = open("simple_module.model", 'w+')
		f.write("\n".join(str(n) for n in clicklist))
		f.close()

		#dump_svmlight_file(clicklist, clicklist, "simple_module.model", False)
		return 0

	#Grabs the output file, stores it within a local variable
	def load_data(self):
		temptable = GrowingList()
		i = 0
		for num in open("simple_module.model"):
			temptable[i] = int(num)
			i += 1
		
		self.table = temptable

	#by page id I mean index, i'll make it configurable
	#Takes in a list of 10 (+) pageIds and ranks them.
	def classify(self, query):	
		query_score = [0] * 10

		for i in range(10):
			query_score[i] = self.table[query[i]]

		sorted_list = [i[0] for i in sorted(enumerate(myList), key=lambda x:x[1])]

		new_rank = [0] * 10
		for j in range(10):
			new_rank[j] = query[sorted_list[j]]
		
		return new_rank


simplemodule = SimpleModule()
simplemodule.train()