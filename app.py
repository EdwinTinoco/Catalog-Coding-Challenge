from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Coding challenge LiveAuctioneers</h1>"

catalog = [
    {
      "catalogId": 159748,
      "title": "Luxury Designer Watches",
      "startDate": "2020-05-05 14:00:00"
    },
    {
      "catalogId": 159612,
      "title": "Authentic Ukrainian Oil Paintings",
      "startDate": "2020-05-05 15:00:00"
    },
    {
      "catalogId": 159949,
      "title": "HAZLET ESTATE PHASE 3",
      "startDate": "2020-05-05 16:00:00"
    },
    {
      "catalogId": 158305,
      "title": "Louisville Legacy Home Premium Auction",
      "startDate": "2020-05-05 16:30:00"
    },
    {
      "catalogId": 159675,
      "title": "16th-20th Century Antiquarian Maps",
      "startDate": "2020-05-05 17:00:00"
    },
    {
      "catalogId": 159620,
      "title": "Viking, Ancient, & Medieval Jewelry",
      "startDate": "2020-05-05 17:00:00"
    },
    {
      "catalogId": 160390,
      "title": "Exceptional Loose Gemstones",
      "startDate": "2020-05-05 18:00:00"
    },
    {
      "catalogId": 159025,
      "title": "Fine Arts and Antiques Auction",
      "startDate": "2020-05-05 18:30:00"
    },
    {
      "catalogId": 159969,
      "title": "$1 Start.. Omega, Emerald, Chopard, Bullion",
      "startDate": "2020-05-06 00:00:00"
    },
    {
      "catalogId": 159650,
      "title": "Luxury Designer Certified Jewelry & Hublot",
      "startDate": "2020-05-06 00:00:00"
    },
    {
      "catalogId": 157212,
      "title": "British Coins & Tokens formed by Marvin Le...",
      "startDate": "2020-05-06 04:00:00"
    },
    {
      "catalogId": 159064,
      "title": "Asian Art Sale",
      "startDate": "2020-05-06 07:00:00"
    },
    {
      "catalogId": 159388,
      "title": "Fine Art, Furniture and Decorative Art",
      "startDate": "2020-05-06 08:00:00"
    },
    {
      "catalogId": 159385,
      "title": "FINE ART, DECORATIVE ART AND MODERN DESIGN",
      "startDate": "2020-05-06 13:00:00"
    },
    {
      "catalogId": 160168,
      "title": "Colossal Gold & Silver Fine Jewelry Auction",
      "startDate": "2020-03-30 00:00:00"
    },
    {
      "catalogId": 160163,
      "title": "Massive Gold & Silver Fine Jewelry Auction",
      "startDate": "2020-03-30 00:00:00"
    },
    {
      "catalogId": 160245,
      "title": "CERTIFIED & NONE CERT LIVE LIQUIDATIONS 30",
      "startDate": "2020-03-30 00:00:00"
    },
    {
      "catalogId": 160118,
      "title": "Books and Works on Paper",
      "startDate": "2020-03-30 05:00:00"
    },
    {
      "catalogId": 158596,
      "title": "Vintage Luxury Rolex & Modern Jewelry Auction",
      "startDate": "2020-03-30 06:00:00"
    },
    {
      "catalogId": 160214,
      "title": "Jewelry & Sterling Silver Auction",
      "startDate": "2020-03-30 07:00:00"
    },
    {
      "catalogId": 160088,
      "title": "GovernmentAuction.com Land/Assets Liquidation",
      "startDate": "2020-03-30 08:00:00"
    },
    {
      "catalogId": 159061,
      "title": "Manuscripts, Paintings, Watercolor & Books",
      "startDate": "2020-03-30 08:00:00"
    },
    {
      "catalogId": 159807,
      "title": "Certified Genuine Jewelry-Watch! Huge Sale",
      "startDate": "2020-03-30 10:00:00"
    },
    {
      "catalogId": 160393,
      "title": "No Reserve Antique Maps and Prints",
      "startDate": "2020-03-30 10:00:00"
    },
    {
      "catalogId": 159870,
      "title": "TRIBAL ARTS ORIENTALIA & CONTINENTAL ANTIQUES",
      "startDate": "2020-03-30 10:00:00"
    },
    {
      "catalogId": 158696,
      "title": "New Inventory Auction pt.1",
      "startDate": "2020-03-30 12:15:00"
    },
    {
      "catalogId": 159603,
      "title": "VALENTINES DAY GIFT AUCTION",
      "startDate": "2020-03-30 15:00:00"
    },
    {
      "catalogId": 160093,
      "title": "Thursday Night Auction 1-30-20",
      "startDate": "2020-03-30 15:00:00"
    },
    {
      "catalogId": 159607,
      "title": "2020 Magnificent Sale",
      "startDate": "2020-03-30 15:00:00"
    },
    {
      "catalogId": 160392,
      "title": "Lakeland Antique Bazaar S52",
      "startDate": "2020-03-30 18:00:00"
    },
    {
      "catalogId": 160227,
      "title": "GovernmentAuction.com Cities Counties, States",
      "startDate": "2020-03-31 09:00:00"
    },
    {
      "catalogId": 160047,
      "title": "Vintage Fur Estate Sale!",
      "startDate": "2020-03-31 09:00:00"
    },
    {
      "catalogId": 159332,
      "title": "ANCIENT JEWELLERY, ANTIQUITIES AND COINS",
      "startDate": "2020-05-01 04:00:00"
    },
    {
      "catalogId": 160063,
      "title": "U-3 Under 3k euros Art Auction",
      "startDate": "2020-05-01 06:00:00"
    },
    {
      "catalogId": 159679,
      "title": "Gun & Military Auction",
      "startDate": "2020-05-01 07:30:00"
    },
    {
      "catalogId": 159951,
      "title": "Fine Art, Antiques & Collectibles Auction",
      "startDate": "2020-05-01 08:00:00"
    },
    {
      "catalogId": 160398,
      "title": "Saturday's Diamond Jewelry, Watches, Art Deco",
      "startDate": "2020-05-01 09:00:00"
    },
    {
      "catalogId": 158549,
      "title": "World War II German/US Military Collection",
      "startDate": "2020-05-01 10:00:00"
    },
    {
      "catalogId": 160408,
      "title": "LTD ED PRINTS ORIGINAL ART DEALER LIQUIDATES",
      "startDate": "2020-05-01 18:00:00"
    },
    {
      "catalogId": 160522,
      "title": "Natural Crystals, Minerals, Specimens & More",
      "startDate": "2020-05-02 18:00:00"
    },
    {
      "catalogId": 159831,
      "title": "Certified Jewelry DAY 25",
      "startDate": "2020-05-03 00:00:00"
    },
    {
      "catalogId": 159635,
      "title": "MID-CENTURY DESIGN - ART - COLLECTIBLES",
      "startDate": "2020-05-03 14:00:00"
    },
    {
      "catalogId": 160186,
      "title": "Painting and Sculpture",
      "startDate": "2020-05-04 09:00:00"
    },
    {
      "catalogId": 159487,
      "title": "Colorful Glass - Spectrum of Color",
      "startDate": "2020-05-04 16:30:00"
    },
    {
      "catalogId": 160107,
      "title": "Wednesday Night Auction 3-6-20",
      "startDate": "2020-05-06 15:00:00"
    },
    {
      "catalogId": 160079,
      "title": "Collectibles, Jewelry and MORE!",
      "startDate": "2020-05-05 15:00:00"
    },
    {
      "catalogId": 160113,
      "title": "Vintage Cartier and Tiffany Jewelry",
      "startDate": "2020-05-05 18:00:00"
    },
    {
      "catalogId": 160440,
      "title": "Design Lab",
      "startDate": "2020-05-06 06:00:00"
    },
    {
      "catalogId": 160211,
      "title": "6, 2020 Discovery Auction",
      "startDate": "2020-05-06 07:00:00"
    },
    {
      "catalogId": 160296,
      "title": "Autograph Auction",
      "startDate": "2020-05-06 10:00:00"
    },
    {
      "catalogId": 160194,
      "title": "Jewellery",
      "startDate": "2020-05-06 10:00:00"
    },
    {
      "catalogId": 160109,
      "title": "It's A Bid Of A Sale!",
      "startDate": "2020-05-06 11:00:00"
    },
    {
      "catalogId": 160386,
      "title": "ANTIQUE PHOTOGRAPHY Remembering Not To Forget",
      "startDate": "2020-05-06 12:00:00"
    },
    {
      "catalogId": 160185,
      "title": "Vintage Modern Fashion, Burberry, ZARA #V88Z",
      "startDate": "2020-05-06 14:00:00"
    },
    {
      "catalogId": 160345,
      "title": "JEWELRY | SILVER | ANTIQUES | FINE ARTS",
      "startDate": "2020-05-06 14:00:00"
    },
    {
      "catalogId": 157691,
      "title": "ART ANTIQUES COLLECTIBLES RUGS & JEWELRY",
      "startDate": "2020-05-06 15:00:00"
    },
    {
      "catalogId": 158430,
      "title": "FEB 6th Antique & Vintage rugs",
      "startDate": "2020-05-06 15:00:00"
    },
    {
      "catalogId": 160521,
      "title": "Ancient Coins, Judaica & Militaria",
      "startDate": "2020-05-06 18:00:00"
    },
    {
      "catalogId": 154648,
      "title": "HISTORY COLLECTION",
      "startDate": "2020-05-06 18:30:00"
    },
    {
      "catalogId": 160254,
      "title": "High End Certified Valentines Liquidation 07",
      "startDate": "2020-05-07 06:00:00"
    },
    {
      "catalogId": 160391,
      "title": "Winter 2020 Fine Estates 2/7/2020",
      "startDate": "2020-05-07 07:00:00"
    },
    {
      "catalogId": 159420,
      "title": "Fine Art From the Masters and Street Artists",
      "startDate": "2020-05-07 16:00:00"
    },
    {
      "catalogId": 159919,
      "title": "07 Bronze Sculpture Online Auction",
      "startDate": "2020-05-07 17:30:00"
    },
    {
      "catalogId": 157886,
      "title": "Chinese Porcelain, Painting and Collectables",
      "startDate": "2020-05-07 19:00:00"
    },
    {
      "catalogId": 159880,
      "title": "Chinese Ceramics and Works of Art - Feb 2020",
      "startDate": "2020-05-08 07:00:00"
    },
    {
      "catalogId": 160191,
      "title": "Paintings, Furniture, Decorative Arts & Rugs",
      "startDate": "2020-05-08 07:00:00"
    },
    {
      "catalogId": 159860,
      "title": "Winter Estates Auction, 8 & 9, 2020",
      "startDate": "2020-05-08 08:00:00"
    },
    {
      "catalogId": 160016,
      "title": "Historic Autographs-Coins-Currency-Americana",
      "startDate": "2020-05-08 09:00:00"
    },
    {
      "catalogId": 159334,
      "title": "Asian Works of Arts 02-08-2020",
      "startDate": "2020-05-08 11:30:00"
    },
    {
      "catalogId": 160484,
      "title": "One of A Kind Finds",
      "startDate": "2020-05-08 14:00:00"
    },
    {
      "catalogId": 157305,
      "title": "Chinese Antique, Art, & Estate Sale",
      "startDate": "2020-05-08 15:00:00"
    },
    {
      "catalogId": 160159,
      "title": "Asian Art Sale",
      "startDate": "2020-05-09 06:00:00"
    },
    {
      "catalogId": 160322,
      "title": "E223 | Important Art, Glass and Antiquities",
      "startDate": "2020-05-09 08:30:00"
    },
    {
      "catalogId": 159864,
      "title": "DAY 2 OF 6  - 250+ LOT COLLECTIBLE POTTERY",
      "startDate": "2020-05-09 09:30:00"
    },
    {
      "catalogId": 160420,
      "title": "$14M MIAMI MANSION PART 2",
      "startDate": "2020-05-09 10:00:00"
    },
    {
      "catalogId": 159944,
      "title": "Art Auction",
      "startDate": "2020-05-09 13:15:00"
    },
    {
      "catalogId": 160017,
      "title": "SIGNED Sports Memorabilia, 1 Owner",
      "startDate": "2020-05-09 14:00:00"
    },
    {
      "catalogId": 160472,
      "title": "E227 | Extremely Rare British Masterpieces",
      "startDate": "2020-05-09 14:30:00"
    },
    {
      "catalogId": 159725,
      "title": "Antiques and Artwork Feb 9 Auction",
      "startDate": "2020-05-09 17:00:00"
    },
    {
      "catalogId": 160193,
      "title": "Antique Auction session 1/4",
      "startDate": "2020-05-10 10:00:00"
    },
    {
      "catalogId": 160265,
      "title": "Antique and African Art auction session 2/4",
      "startDate": "2020-05-11 12:00:00"
    },
    {
      "catalogId": 160378,
      "title": "Fine Art, Glass, and Antiques",
      "startDate": "2020-05-12 10:00:00"
    },
    {
      "catalogId": 160040,
      "title": "Coins and Historical Medals (Day 2)",
      "startDate": "2020-05-13 02:00:00"
    },
    {
      "catalogId": 160267,
      "title": "Auction small antiques, session 4/4",
      "startDate": "2020-05-13 10:00:00"
    },
    {
      "catalogId": 158390,
      "title": "$10 Unreserved Fine Antique Auction",
      "startDate": "2020-05-14 06:00:00"
    },
    {
      "catalogId": 159294,
      "title": "Asian art Product",
      "startDate": "2020-05-15 07:00:00"
    },
    {
      "catalogId": 158472,
      "title": "Fine Art, Antiques & Asian Art Auction",
      "startDate": "2020-05-15 15:00:00"
    },
    {
      "catalogId": 159915,
      "title": "Native American Artifact Auction",
      "startDate": "2020-05-16 08:00:00"
    },
    {
      "catalogId": 159611,
      "title": "Rare Certified Edwardian Fine Jewelry & Gems",
      "startDate": "2020-05-18 12:00:00"
    },
    {
      "catalogId": 160361,
      "title": "DESIGN | FRENCH | ITALIAN | AMERICAN",
      "startDate": "2020-05-22 08:00:00"
    },
    {
      "catalogId": 160134,
      "title": "Premier Fine Art",
      "startDate": "2020-05-22 10:00:00"
    },
    {
      "catalogId": 159185,
      "title": "Quality 2020 Antiques & Decoratives Sale",
      "startDate": "2020-05-22 11:00:00"
    },
    {
      "catalogId": 158094,
      "title": "Boutiquelux Auctions 2020",
      "startDate": "2020-05-22 11:00:00"
    },
    {
      "catalogId": 160120,
      "title": "RARE BOOKS With NO RESERVE NO BUYERS PREMIUM!",
      "startDate": "2020-05-23 14:00:00"
    },
    {
      "catalogId": 160284,
      "title": "Estate Auction On Line ONLY!",
      "startDate": "2020-05-23 15:00:00"
    },
    {
      "catalogId": 159730,
      "title": "TimeLine Auctions Antiquities Sale - Day 2",
      "startDate": "2020-05-26 01:00:00"
    },
    {
      "catalogId": 159733,
      "title": "TimeLine Auctions Antiquities Sale - Day 4",
      "startDate": "2020-05-28 01:00:00"
    },
    {
      "catalogId": 159734,
      "title": "TimeLine Auctions Antiquities Sale - Day 5",
      "startDate": "2020-05-29 01:00:00"
    },
    {
      "catalogId": 160365,
      "title": "Fine Arts and Antiques Online Only Auction",
      "startDate": "2020-05-29 11:00:00"
    },
    {
      "catalogId": 160057,
      "title": "Connoisseur Classic Treasures",
      "startDate": "2020-05-07 11:00:00"
    }
  ]


@app.route('/catalog', methods=['GET'])
def get_all_catalog():
    return jsonify(catalog)


@app.route('/catalog/<id>', methods=['GET'])
def get_single_catalog(id):
    for item in catalog:
        if item['catalogId'] == id:
            result = item

    return jsonify(result)

@app.route('/catalog/startdate/<str>', methods=["GET"])
def get_catalog_by_startdate(str):

    for item in catalog:
        if item['startDate'] == str:
            result = item

    return jsonify(result)



if __name__ == '__main__':
    app.run(debug=True)
