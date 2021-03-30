import requests
from bs4 import BeautifulSoup
import pandas
import argparse
import connect


parser=argparse.ArgumentParser()
parser.add_argument("--max_page_num",help="Enter the numbers to pages to be checked: ", type=int)
parser.add_argument("--dbname",help="Enter the numbers to pages to be checked: ", type=int)
args=parser.parse_args()

oyo_url="https://www.oyorooms.com/hotels-in-bangalore/?page="
page_num=args.max_num_page
scrape=[]
connect.connect(args.dbname)

for i in range(1,page_num):
  req=requests.get(oyo_url+str(i))
  cont=req.content

  soup= BeautifulSoup(cont,"html.parser")
  hotels_list=soup.find_all("dive",{"class":"hotelCardListing"})
  

  for h in hotels_list:
    hotel_dict=[]
    hotel_dict["name"]= h.find("h3",{"class":"ListingHotelDescription__hotelName"}).text
    hotel_dict["address"]=h.find("span",{"itemdrop":"streetAddress"}).text
    hotel_dict["price"]= h.find("span",{"class":"listingPrice__finalPrice"}).text
    
    other_info= h.find("div",{"class":"amenityWrapper"}).text
    amenity_list=[]
    for amenity in other_info.find_all("div",{"class":"amenityWrapper__amenity"}):
      amenity_list.append(amenity.find("span",{"class":"d-body-sm"}).text.strip())

    hotel_dict["amenity"]=', '.join(amenity_list[:-1])
    scrape.append(hotel_dict)
    connect.insert_into_table(args.dbname, tuple(hotel_dict.values()))

    
    try:
      hotel_dict["rating"]= h.find("span",{"class":"hotelRating__ratingSummary"}).text
    except AttributeError:
      hotel_dict["rating"]= None

dataframe=pandas.DataFrame(scrape)
dataframe.to_csv("oyo.csv") 
connect.get_hotel_info(args.dbname)
