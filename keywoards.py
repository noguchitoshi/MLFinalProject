# overall dictionary, <keyword, {dictionary of <domain id, count>}>
import ast




#rom numpy import *
#rom sklearn.datasets import load_svmlight_file
#rom sklearn.datasets import dump_svmlight_file
#mport scipy.sparse

class GrowingList(list):
	def __setitem__(self, index, value):
		if index >= len(self):
			self.extend([0] * (index + 1 - len(self)))
		list.__setitem__(self, index, value)

class KeywordsModule:
	def __init__(self):
		self.table = None

	#Reads the training data, creates the array, outputs a file
	def train(self):
		counts = dict()

		file_name = "data/trailhead1000"
		current_keywords = []
		urldomainmap = [(0, 0)] * 10 
		for line in open(file_name):
			element = line.split("\t")

			# Update URL Domain Map if we get a new query
			if (element[2] == "Q"):
				#starting with 6...
				current_keywords = element[5].split(",")
				for i in range(10):
					[url, domain] = element[i + 6].split(",")
					#print("URL: " + url + ", Domain: " + domain)
					urldomainmap[i] = (url, domain)

			# Enter module specific data here. 
			if (element[2] == "C"):
				# Debugging variable
				#print(str(element[4]))

				#Find the relevant domain name.
				for (url, domain) in urldomainmap:
					#Iterate.f
					#print("TEST: " + url +" against: " + element[4])
					if (int(url) == int(element[4])):
						#print("what")

						for word in current_keywords:
							# if the current keyword is not in the dictionary
							if not (word in counts.keys()):
								counts[word] = dict()

							temp = counts[word]

							# check if key exists for this particular domain
							if int(domain) in temp:
								temp[domain] += 1
							else:
								temp[domain] = 1

		f = open("keywords.model", 'w+')
		f.write(str(counts))
		f.close()
		self.table = counts		
		print counts

		string = str(counts)


		blahhh = ast.literal_eval(string)

		print "finished\n"
		return 0;

	#Grabs the output file, stores it within a local variable
	def load_data(self):
		i = 0
		for lines in open("keywords.model"):
			self.table = ast.literal_eval(lines)
			i += 1
		print i


	# urldomainquery = [(url, domain)] * 10, keywords = [] (list of keywords)
	# output = [(url, domain)] * 10 (RERANKED)
	def classify(self, keywords, urldomainquery):	
		query_score = [0] * 10

		for word in keywords:
			for i in range(10):
				# get the number of clicks for this particular keyword / domain
				temp_dict = self.table[word]
				query_score[i] = temp_dict[(urldomainquery[i][1])]		

		sorted_list = [i[0] for i in sorted(enumerate(query_score), key=lambda x:x[1])]

		new_rank = [0] * 10
		for j in range(10):
			new_rank[j] = urldomainquery[sorted_list[j]][0] #return URLs
		
		return new_rank

print "exit\n"
keywordmodule = KeywordsModule()
keywordmodule.load_data()
print keywordmodule.table