'''
DATA NESTING SCHEME IS AS FOLLOWS
Complete Link Set -> Category -> Feed
Category (i.e. news_links, tech_links) is a tuple
Feed is an object containing the RSS Source (publisher of content) and RSS Feed (URL)
'''
##Initialize Objects

class Feed (object):

    def __init__(self, category, source):
        self.category = category
        self.source = source

    def __iter__(self):
    	return self

###Store all the urls here
###DO NOT USE A SINGLE DICTIONARY BECAUSE ORDER WILL BE LOST
###Previous structure was list(dict(), dict()) to maintain order
###Also to allow search based on a common key 'source' and locate'
###This was changed to a tuple with objects inside that tuple
###All tuples will be group inside main.py and then processed from there

#NEWS LINKS
#News Lens
n1 = Feed("關鍵評論網", ["https://feeds.feedburner.com/TheNewsLens"])
#Aggregate - VOX, Quartz
n2 = Feed("Aggregate",["https://www.vox.com/rss/index.xml", 
                       "https://rss.politico.com/politics-news.xml", 
                       "https://www.axios.com/feeds/feed.rss"])
#Audit - Politifact, FactCheck
n3 = Feed("Audit",["https://www.politifact.com/rss/all/", "https://www.factcheck.org/feed/"])
#Libertarian Thinktank
n4 = Feed("CATO",["https://www.cato.org/rss/recent-opeds"])
#European Center for Foreign Relations Thinktank
n5 = Feed("ECFR",["https://ecfr.eu/feed/"])
#Center Left Thinktanks - 
#Brookings Newsletter - https://kill-the-newsletter.com/feeds/860g6qecsg9tkj5qmzg1
#CAP Newsletter - https://kill-the-newsletter.com/feeds/ygmz0fe20utrdsnlz01w
n6 = Feed("B&CAP",["https://kill-the-newsletter.com/feeds/860g6qecsg9tkj5qmzg1.xml",
                  "https://kill-the-newsletter.com/feeds/ygmz0fe20utrdsnlz01w.xml"])
#538 Pew Research
n7 = Feed("Pew",["https://www.pewresearch.org/publications/feed/"])
#English World - Reuters World, BBC, Aljazeera
n8 = Feed("World",["https://www.reutersagency.com/feed/?taxonomy=best-regions&post_type=best",
                           "https://feeds.bbci.co.uk/news/world/rss.xml#",
                           "http://www.aljazeera.com/xml/rss/all.xml"])
#RFI
n9 = Feed("RFI",["https://www.rfi.fr/fr/rss"])

news_links = (n1,n2,n3,n4,n5,n6,n7,n8,n9)

#TECH LINKS
# Engadget, Toms Hardware
t1 = Feed("CE", ["https://www.engadget.com/rss.xml",
                 "https://www.tomshardware.com/feeds/all"])
t2 = Feed("Verge",["https://www.theverge.com/rss/index.xml"])
t3 = Feed("Ars",["http://feeds.arstechnica.com/arstechnica/index"])
t4 = Feed("RCE",["https://www.realcleareducation.com/index.xml"])
t5 = Feed("Hacker News",["https://news.ycombinator.com/rss"])
#Web Design - CSS Tricks, Smashing Mag
t6 = Feed("Web Design",["https://css-tricks.com/feed" ,
                        "https://www.smashingmagazine.com/feed"])
t7 = Feed("E&E ",["https://www.eenews.net/articles/feed/"])
t8 = Feed("City",["https://www.route-fifty.com/rss/all/"])
t9 = Feed("Design", ["http://feeds.fastcompany.com/fastcompany/headlines",
                        "http://feeds.feedburner.com/core77/blog"])

tech_links = (t1,t2,t3,t4,t5,t6,t7,t8,t9)

#BUSINESS LINKS
b1 = Feed("TC",["https://techcrunch.com/feed"])
b2 = Feed("VB",["https://venturebeat.com/feed"])
#Crypto - Coindesk, CoinTelegraph
b3 = Feed("Crypto",["https://www.coindesk.com/arc/outboundfeeds/rss/" ,
                    "https://cointelegraph.com/rss"])
b4 = Feed("Economist",["https://www.economist.com/finance-and-economics/rss.xml"])
b5 = Feed("HBR",["http://feeds.harvardbusiness.org/harvardbusiness?fo"])
b6 = Feed("Bloomberg",["https://news.google.com/rss/search?q=when:24h+allinurl:bloomberg.com&hl=en-US&gl=US&ceid=US:en"])
b7 = Feed("RCM",["https://www.realclearmarkets.com/index.xml"])
b8 = Feed("FiTi",["http://business.financialpost.com/category/news/economy/feed"])
b9 = Feed("Alpha",["http://seekingalpha.com/listing/most-popular-articles.xml"])

biz_links = (b1,b2,b3,b4,b5,b6,b7,b8,b9)

#RELIGIOUS LINKS
r1 = Feed("GCC",["https://www.thegospelcoalition.org/rss"])
r2 = Feed("RCR",["https://www.realclearreligion.org/index.xml"])
r3 = Feed("Biologos",["https://wp.biologos.org/feed/"])
r4 = Feed("CT",["https://www.christianitytoday.com/feed"])
r5 = Feed("PE",["https://blog.practicalethics.ox.ac.uk/feed"])
r6 = Feed("SoJo",["http://feeds.sojo.net/sojourners/blog"])
r7 = Feed("DN", ["https://dailynous.com/feed/"])

religious_links = (r1,r2,r3,r4,r5,r6,r7)

#SPORTS LINKS
s1 = Feed("ESPN",["http://sports.espn.go.com/espn/rss/news"])
s2 = Feed("Deadspin",["https://deadspin.com/rss"])
s3 = Feed("TSN",["https://www.sportingnews.com/us/rss"])
s4 = Feed("The Athletic",["https://theathletic.com/feeds/rss/news/"])
s5 = Feed("FBS",["http://feeds.feedburner.com/fbschedulescom?format=xml"])
s6 = Feed("NYT",["https://rss.nytimes.com/services/xml/rss/nyt/Sports.xml"])
s7 = Feed("Cycling",["https://www.bicycleretailer.com/rss",
                    "https://www.bikeradar.com/news/feed/"])

sport_links = (s1,s2,s3,s4,s5,s6,s7)

#LEISURE LINKS
#Autos - Autoblog, TTAC
l1 = Feed("Autos",["https://www.autoblog.com/rss.xml",
                   "https://www.thetruthaboutcars.com/rss/feed/all"])
#DIY - Hack-a-day, MAKE
l2 = Feed("DIY",["https://hackaday.com/feed" ,
                 "https://makezine.com/category/technology/feed"])
#SF Focus - SF Eater, 7x7
l3 = Feed("SF",["https://www.7x7.com/feed"])
l4 = Feed("Curbly",["https://www.curbly.com/site_index.rss"])
#Substack
l5 = Feed("Substack",["https://www.readmovements.com/feed",
                      "https://www.newsletter.rideflywheel.com/feed",
                      "https://micromobility.substack.com/feed",
                      "https://read.followingthefootprints.com/feed"])
l6 = Feed("Kitchn",["http://feeds.thekitchn.com/apartmenttherapy/thekitchn?format=xml"])
#Culinary - Smitten Kitchen, Bright Eyed Baker
l7 = Feed("Culinary",["http://feeds.feedburner.com/smittenkitchen",
                      "https://www.browneyedbaker.com/feed"])
l8 = Feed("Serious Eats",["http://feeds.feedburner.com/seriouseatsfeaturesvideos"])

leisure_links = (l1,l2,l3,l4,l5,l6,l7,l8)

#MUSIC LINKS
m1 = Feed("Pitchfork",["https://pitchfork.com/feed/feed-news/rss"])
m2 = Feed("FNT",["http://feeds.feedburner.com/freshnewtracks/iyTb"])
m3 = Feed("DA",["http://www.dancingastronaut.com/music/feed/"])
m4 = Feed("Earmilk",["http://feeds2.feedburner.com/earmilk"])
m5 = Feed("TSiS",["https://thissongissick.com/feed/"])
m6 = Feed("EDM Sauce",["https://www.edmsauce.com/feed/"])

music_links = (m1,m2,m3,m4,m5,m6)
