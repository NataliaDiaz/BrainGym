import json

docid_to_title = json.loads('{"28099931907": {"content": {"title": "Zika dollars and Internet fight in play as government shutdown looms"}}, "28108959337": {"content": {"title": "Leaders express renewed optimism about flood relief as Congress aims to avoid a government shutdown"}}, "28110814722": {"content": {"title": "Senate passes stopgap spending bill, $1.1B to fight Zika"}}, "28101422554": {"content": {"title": "Senate blocks bill to avert shutdown as De..."}}, "28099132063": {"content": {"title": "Senate Dems threaten shutdown over Flint aid"}}, "28101167069": {"content": {"title": "Zika dollars, internet fight in play as government shutdown looms"}}, "28102817621": {"content": {"title": "House leaders reach deal on Flint aid, potentially averting shutdown"}}, "28108039075": {"content": {"title": "Deal reached to keep US government running, help Flint"}}, "28098698025": {"content": {"title": "Defeat of Republicans\\u2019 stop-gap spending bill brings federal government closer to a shutdown"}}, "28097027782": {"content": {"title": "Will Democrats force a government shutdown over Flint relief funds?"}}, "28111131355": {"content": {"title": "Lawmakers strike deal to avoid shutdown"}}, "28110856451": {"content": {"title": "Louisiana flood aid, $500 million, survives Senate budget fight"}}, "28106625838": {"content": {"title": "Pelosi aide says deal with Speaker Ryan covers Flint aid"}}, "28099931906": {"content": {"title": "Zika dollars  and Internet fight in play as government shutdown  looms"}}, "28096859458": {"content": {"title": "Are Democrats pushing the federal government toward a shutdown?"}}, "28110814723": {"content": {"title": "Senate passes stopgap spending bill, $1.1B to fight Zika"}}, "28093906031": {"content": {"title": "will democrats force a federal shutdown over Flint relief funds?"}}, "28108873175": {"content": {"title": "Senate Democrats accept deal on Flint aid, potentially averting shutdown"}}, "28103573587": {"content": {"title": "ALEXANDER : Senate Democrats\\u2019 Election Politics Are Putting Babies at Risk"}}, "28096849799": {"content": {"title": "Democrats poised to block stopgap funding bill over Flint"}}, "28098943696": {"content": {"title": "Senate blocks stopgap bill to prevent shutdown this weekend"}}, "28110942840": {"content": {"title": "Senate Passes Short-Term Government Funding Measure"}}, "28107038234": {"content": {"title": "House aides: Deal reached to help Flint, keep US gov\'t open"}}, "28084509076": {"content": {"title": "Week ahead: Spending fight shifts from Zika to Flint"}}, "28089633072": {"content": {"title": "Flint water aid spending bill\'s sticking point"}}, "28099749478": {"content": {"title": "Government shutdown looms due to partisan clash over Flint aid"}}, "28099468922": {"content": {"title": "Funding bill rejected as shutdown nears"}}, "28107540657": {"content": null}, "28098940419": {"content": {"title": ""}}, "28110838282": {"content": {"title": "Senate approves deal to keep government open, combat Zika"}}, "28093943889": {"content": {"title": "Democrats press talks as showdown vote looms on funding bill"}}, "28099506681": {"content": {"title": "Republicans ready new bid to avoid shutdown"}}, "28084188573": {"content": {"title": "Zika: Congressional showdown coming this week"}}, "28109130960": {"content": {"title": "McConnell: Let\\u2019s Keep Working Together to Pass Critical Resources"}}, "28097129455": {"content": {"title": "McConnell: We Cannot Afford to Wait Any Longer on Providing Critical Resources"}}, "28110653655": {"content": {"title": "Deal averts federal shutdown, ignores Cruz\' Internet \'giveaway\'"}}, "28110819318": {"content": {"title": "Senate passes spending bill after separate Flint aid deal"}}, "28106754872": {"content": {"title": "Democrats: Deal reached to help Flint, keep US gov\'t open"}}, "28093906030": {"content": {"title": "Will Democrats force a federal shutdown over Flint relief funds?"}}, "28108257314": {"content": {"title": "US Senate Again Blocks Bill That Includes Zika Funding"}}, "28097690131": {"content": {"title": "Cornyn: Democrats Pushing Country Towards Shutdown for Political Gain"}}, "28096854777": {"content": {"title": "Flint aid at center of funding standoff in Congress"}}, "28100917473": {"content": {"title": "A government shutdown is looming because of a clash over aid for Flint, Michigan"}}, "28099198548": {"content": {"title": "Senate Dems block gov\'t funding bill over Flint aid"}}, "28110814724": {"content": {"title": "Senate passes stopgap spending bill, $1.1B to fight Zika"}}, "28110749186": {"content": {"title": "Senate advances bill to avert government shutdown after Flint deal struck"}}, "28110001860": {"content": {"title": "Congress set to avert government shutdown, offer Zika relief"}}, "28109184578": {"content": {"title": "Deal reached to keep U.S. government running, help Flint"}}, "28100566138": {"content": {"title": "Democrats poised to block stopgap funding bill over Flint"}}, "28085937302": {"content": {"title": "FOUR DAYS UNTIL NEXT REPUBLICAN GOVERNMENT SHUTDOWN"}}, "28108954857": {"content": {"title": "Congress nears deal to keep government open"}}, "28098853699": {"content": {"title": "Senate Democrats Block Republican Stopgap From Advancing"}}, "28110991149": {"content": {"title": "Senate passes bill to avoid government shutdown"}}, "28098130400": {"content": {"title": "Congress weighs plan to dodge shutdown"}}}')


def get_unique_w(docid_to_title):
	"""
	function that identifies all the unique words across all the `content.title` fields in `docid_to_title`
	"""
	vocabulary = []
	for docid, fields in docid_to_title.iteritems():
		content = fields["content"]
		if content:
			title = content["title"]
			unique_words = list(title.split())
			#print "Doc ID and words: ", docid, " : ", unique_words
			for w in unique_words:
				vocabulary.append(w.upper())

	vocabulary = set(vocabulary)
	print "Unique words: ",len(vocabulary)
	return vocabulary

print "\n\n\nget_unique_w:\n", get_unique_w(docid_to_title)
#######################


def get_bigrams2count(docid2title):
	bigrams2count = {}
	for docid, fields in docid2title.iteritems():
		content = fields["content"]
		if content:
			title = content["title"]
			words = list(title.split())
			words = [x.upper() for x in words]
			#print "Doc ID and words: ", docid, " : ", unique_words
			for index in range(len(words)-1):
				bigrams2count[(words[index], words[index+1])] = bigrams2count.get((words[index], words[index+1]), 0) + 1
	print len(bigrams2count)," unique bigrams",
	return bigrams2count

def most_freq_bigrams(docid2title, k):
	"""
	function that computes the k most frequent bigrams across all the `content.title` fields in `docid_to_title`.
	"""
	bigramsDict = get_bigrams2count(docid2title)
	# get a list with the keys sorted by value (count)
	sortedDict = sorted(bigramsDict, key= lambda x: bigramsDict[x] , reverse = True) # decremental
	print "Highest counts: ", set(bigramsDict.values())
	print "sortedDict by count: ",sortedDict[:k], bigramsDict
	return sortedDict[:k]

print "\n\n\n\n most_freq_bigrams: \n", most_freq_bigrams(docid_to_title, 5)
#######################



def find_duplicate_titles(docid2title):
	"""
	Find all the duplicate titles in `content.title` fields in `docid_to_title`.
	"""
	titles = set()
	duplicate_titles = set()
	for docid, fields in docid_to_title.iteritems():
		content = fields["content"]
		if content:
			title = content["title"]
			if title in titles:
				duplicate_titles.add(title)
			else:
				titles.add(title)
	#print "All repeated titles: ",duplicate_titles
	return duplicate_titles

print "\n\n\n\nfind_duplicate_titles \n",find_duplicate_titles(docid_to_title)
