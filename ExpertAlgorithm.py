#initialize all of the different tests
from SimpleClicks import SimpleClicksModule

simplemodule = SimpleClicksModule()
simplemodule.load_data()

#create output file
output = open("reranked", 'w+')
output.write("SessionID,URLID\n\n")

#parse the test file
urldomainmap = [(0, 0)] * 10
for line in open("test"):
	element = line.split("\t")

	# this is a test query
	if (element[2] == 'T'):
		queryId = element[0]

		for i in range(10):
			[url, domain] = element[i + 6].split(",")
			urldomainmap[i] = (url, domain)

		#rerank the urls w/ the modules
		simple_rerank = simplemodule.classify(urldomainmap)
		#other_reranks...

		#weigh each of the different tests
		#we don't have other tests
		weighted_ranks = simple_rerank #something
	
		#output ranking into file
		for j in range(10):
			output.write(queryId + "," + weighted_ranks[j] + "\n")

#submit that file
#something