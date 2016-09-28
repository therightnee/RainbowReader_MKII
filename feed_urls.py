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
#CSM
n1 = Feed("CSM", "http://rss.csmonitor.com/feeds/csm")
#Aggregate - VOX, Quartz
n2 = Feed("Aggregate","http://rssmix.com/u/8207097/rss.xml")
#Audit - Politifact, FactCheck
n3 = Feed("Audit","http://www.rssmix.com/u/3844183/rss.xml")
n4 = Feed("CATO","http://feeds.cato.org/CatoHomepageHeadlines")
n5 = Feed("CAP","http://feeds.feedburner.com/americanprogress/ydxq")
#Politico
n6 = Feed("RCP","http://feeds.feedburner.com/realclearpolitics/qlMj")
n7 = Feed("Brookings","http://webfeeds.brookings.edu/brookingsrss/topfeeds/latestfrombrookings?format=xml")
n8 = Feed("AP","http://hosted2.ap.org/atom/APDEFAULT/3d281c11a96b4ad082fe88aa0db04305")
#International - Reuters,BBC 
n9 = Feed("International","http://rssmix.com/u/8207098/rss.xml")
n10 = Feed("538","http://fivethirtyeight.com/politics/feed/")

news_links = (n1,n2,n3,n4,n5,n6,n7,n8,n9,n10)

#TECH LINKS
#Gadgets - Gizmodo, Engadget
t1 = Feed("Gadgets", "http://rssmix.com/u/3844649/rss.xml")
t2 = Feed("Verge","http://www.theverge.com/rss/frontpage")
t3 = Feed("Ars","http://feeds.arstechnica.com/arstechnica/index")
t4 = Feed("Toms","http://www.tomshardware.com/feeds/rss2/all.xml")
t5 = Feed("Hacker News","https://news.ycombinator.com/rss")
#Web Design - CSS Tricks, Smashing Mag, Vandelay, Web Design Tuts+
t6 = Feed("Web Design","http://rssmix.com/u/3844652/rss.xml")
t7 = Feed("GTM ","http://feeds.greentechmedia.com/GreentechMedia")
t8 = Feed("Fast Co","http://feeds.fastcompany.com/fastcompany/headlines")
t9 = Feed("Core 77", "http://feeds.feedburner.com/core77/blog" )

tech_links = (t1,t2,t3,t4,t5,t6,t7,t8,t9)

#BUSINESS LINKS
b1 = Feed("Forbes","http://www.forbes.com/most-popular/feed/")
b2 = Feed("Wisebread","http://feeds.killeraces.com/wisebread")
b3 = Feed("538","http://fivethirtyeight.com/economics/feed/")
b4 = Feed("Fi Post","http://business.financialpost.com/category/investing/feed")
b5 = Feed("HBR","http://feeds.harvardbusiness.org/harvardbusiness?fo")
b6 = Feed("1RR","http://feeds.feedburner.com/americanprogress/ydxq")
b7 = Feed("Business Insider","http://www.businessinsider.com/rss")
b8 = Feed("Inc.com","http://feeds.inc.com/home/updates")
b9 = Feed("FiTi", "http://business.financialpost.com/category/news/economy/feed")
b10 = Feed("Alpha", "http://seekingalpha.com/listing/most-popular-articles.xml")

biz_links = (b1,b2,b3,b4,b5,b6,b7,b8,b9,b10)

#RELIGIOUS LINKS
r1 = Feed("GCC", "http://feeds.feedburner.com/tgcblog")
r2 = Feed("Boundless","http://feeds.feedburner.com/boundlessline/blog?format=xml")
r3 = Feed("Biologos","http://biologos.org/blogs/feed")
r4 = Feed("TGA","http://feeds.feedburner.com/TheGodArticle")
r5 = Feed("CT","http://feeds.christianitytoday.com/christianitytoday/ctmag/")
r6 = Feed("Desiring", "http://rss.desiringgod.org/")

religious_links = (r1,r2,r3,r4,r5,r6)

#SPORTS LINKS
s1 = Feed("ESPN", "http://sports.espn.go.com/espn/rss/news")
s2 = Feed("Deadspin","http://feeds.gawker.com/deadspin/full")
s3 = Feed("538","http://fivethirtyeight.com/sports/feed/")
s4 = Feed("Great Goals","http://www.101greatgoals.com/feed/")
s5 = Feed("FBS","http://feeds.feedburner.com/fbschedulescom?format=xml")
s6 = Feed("RCS","http://www.realclearsports.com/index.xml")

sport_links = (s1,s2,s3,s4,s5,s6)

#LEISURE LINKS
#Autos - Jalopnik, Autoblog, TTAC
l1 = Feed("Autos","http://www.rssmix.com/u/8193109/rss.xml")
#DIY - MAKE, Hack-a-day
l2 = Feed("DIY","http://rssmix.com/u/3844663/rss.xml")
l3 = Feed("Lifehacker","http://feeds.gawker.com/lifehacker/full#_ga=1.188949803.1289611229.1464145212")
l4 = Feed("Curbly","http://feeds.curbly.com/c/35111/f/649129/index.rss")
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
m6 = Feed("TSiS","http://thissongissick.com/feeds/feed")
m7 = Feed("Hype Machine","http://hypem.com/feed/popular/3day/1/feed.xml")

music_links = (m1,m2,m3,m4,m5,m6,m7)
