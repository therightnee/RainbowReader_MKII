'''
DATA NESTING SCHEME IS AS FOLLOWS
Complete Link Set -> Category -> Feed
Category (i.e. news_links, tech_links) is a tuple
Feed is an object containing the RSS Source (publisher of content) and RSS Feed (URL)
'''
##Initialize Objects

class Feed (object):

    def __init__(self, source, location):
        self.source = source
        self.location = location

    def __iter__(self):
    	return self

###Store all the urls here
###DO NOT USE A SINGLE DICTIONARY BECAUSE ORDER WILL BE LOST
###Previous structure was list(dict(), dict()) to maintain order
###Also to allow search based on a common key 'source' and locate'
###This was changed tfo a tuple with objects inside that tuple
###All tuples will be group inside main.py and then processed from there

#NEWS LINKS
#News Lens
n1 = Feed("關鍵評論網", "https://feeds.feedburner.com/TheNewsLens")
#Aggregate - VOX, Quartz
n2 = Feed("Aggregate","http://rssmix.com/u/8207097/rss.xml")
#Audit - Politifact, FactCheck
n3 = Feed("Audit","http://www.rssmix.com/u/3844183/rss.xml")
#Libertarian Thinktank
n4 = Feed("CATO","https://www.cato.org/rss/recent-opeds")
#Left Thinktank
n5 = Feed("CAP","http://feeds.feedburner.com/americanprogress/ydxq")
#Aljazeera
n6 = Feed("AJ","http://www.aljazeera.com/xml/rss/all.xml")
#Center Left Thinktank
n7 = Feed("Brookings","http://webfeeds.brookings.edu/brookingsrss/topfeeds/latestfrombrookings?format=xml")
#English World - Reuters World, BBC
n8 = Feed("English World","https://feed.rssunify.com/5dbdad68b12e0/rss.xml")
#RFI Appredndre
n9 = Feed("RFI","https://savoirs.rfi.fr/fr/apprendre-perfectionner-le-francais/rss")
#538 Political Analysis
n10 = Feed("538","http://fivethirtyeight.com/politics/feed/")

news_links = (n1,n2,n3,n4,n5,n6,n7,n8,n9,n10)

#TECH LINKS
t1 = Feed("Engadget", "https://www.engadget.com/rss.xml")
t2 = Feed("Verge","http://www.theverge.com/rss/frontpage")
t3 = Feed("Ars","http://feeds.arstechnica.com/arstechnica/index")
t4 = Feed("Toms","https://www.tomshardware.com/feeds/all")
t5 = Feed("Hacker News","https://news.ycombinator.com/rss")
#Web Design - CSS Tricks, Smashing Mag, Vandelay, Web Design Tuts+
t6 = Feed("Web Design","http://rssmix.com/u/3844652/rss.xml")
t7 = Feed("GTM ","http://feeds.greentechmedia.com/GreentechMedia")
t8 = Feed("Fast Co","http://feeds.fastcompany.com/fastcompany/headlines")
t9 = Feed("Core 77", "http://feeds.feedburner.com/core77/blog" )

tech_links = (t1,t2,t3,t4,t5,t6,t7,t8,t9)

#BUSINESS LINKS
b1 = Feed("TC","http://feeds.feedburner.com/TechCrunch/")
b2 = Feed("Wisebread","http://feeds.killeraces.com/wisebread")
#Crypto - Coindesk, CoinTelegraph
b3 = Feed("Crypto","http://www.rssmix.com/u/8264685/rss.xml")
b4 = Feed("Economist","https://www.economist.com/finance-and-economics/rss.xml")
b5 = Feed("HBR","http://feeds.harvardbusiness.org/harvardbusiness?fo")
b6 = Feed("Business Insider","https://www.businessinsider.com/rss")
b7 = Feed("Inc.com","https://www.inc.com/rss/")
b8 = Feed("FiTi", "http://business.financialpost.com/category/news/economy/feed")
b9 = Feed("Alpha", "http://seekingalpha.com/listing/most-popular-articles.xml")

biz_links = (b1,b2,b3,b4,b5,b6,b7,b8,b9)

#RELIGIOUS LINKS
r1 = Feed("GCC", "http://feeds.feedburner.com/tgcblog")
r2 = Feed("Boundless","http://feeds.feedburner.com/boundlessline/blog?format=xml")
r3 = Feed("Biologos","https://wp.biologos.org/feed/")
r4 = Feed("CT","http://feeds.christianitytoday.com/christianitytoday/ctmag/")
r5 = Feed("CC", "https://www.christiancentury.org/feed")
r6 = Feed("SoJo","http://feeds.sojo.net/sojourners/blog")

religious_links = (r1,r2,r3,r4,r5,r6)

#SPORTS LINKS
s1 = Feed("ESPN", "http://sports.espn.go.com/espn/rss/news")
s2 = Feed("Deadspin","https://deadspin.com/rss")
s3 = Feed("538","http://fivethirtyeight.com/sports/feed/")
s4 = Feed("Great Goals","http://www.101greatgoals.com/feed/")
s5 = Feed("FBS","http://feeds.feedburner.com/fbschedulescom?format=xml")
s6 = Feed("RCS","http://www.realclearsports.com/index.xml")

sport_links = (s1,s2,s3,s4,s5,s6)

#LEISURE LINKS
#Autos - Autoblog, TTAC
l1 = Feed("Autos","http://www.rssmix.com/u/8264704/rss.xml")
#DIY - MAKE, Hack-a-day
l2 = Feed("DIY","http://rssmix.com/u/3844663/rss.xml")
#SF Focus - SF Eater, 7x7
l3 = Feed("SF","http://www.rssmix.com/u/8264703/rss.xml")
l4 = Feed("Curbly","https://www.curbly.com/site_index.rss")
#Travel - Eat Your World, Out of Town, View from the Wing
l5 = Feed("Travel","http://www.rssmix.com/u/8193110/rss.xml")
l6 = Feed("Kitchn","http://feeds.thekitchn.com/apartmenttherapy/thekitchn?format=xml")
#Culinary - Smitten Kitchen, Bright Eyed Baker
l7 = Feed("Culinary","http://www.rssmix.com/u/3845568/rss.xml")
l8 = Feed("Serious Eats","http://feeds.feedburner.com/seriouseatsfeaturesvideos")

leisure_links = (l1,l2,l3,l4,l5,l6,l7,l8)

#MUSIC LINKS
m1 = Feed("EMPT", "http://www.etmusiquepourtous.com/feed/")
m2 = Feed("FNT","http://feeds.feedburner.com/freshnewtracks/iyTb")
m3 = Feed("Your EDM","http://www.youredm.com/free-download/feed/")
m4 = Feed("DA","http://www.dancingastronaut.com/music/feed/")
m5 = Feed("Earmilk","http://feeds2.feedburner.com/earmilk")
m6 = Feed("TSiS","https://thissongissick.com/feed/")
m7 = Feed("EDM Sauce","https://www.edmsauce.com/feed/")

music_links = (m1,m2,m3,m4,m5,m6,m7)
