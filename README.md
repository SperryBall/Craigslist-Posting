# Setup Environment

1. Clone repo via command line and `cd` into it:
    * `git clone https://github.com/SperryBall/Craigslist-Posting.git`
    * `cd Craigslist-Posting`
2. Create virtual environment
    * `python3 -m venv env`
3. Activate Virtual Environment
    * `source env/bin/activate`
4. Install Python Packages in Virtual Environment
    * `pip install -r requirements.txt`
5. Execute the Python script
    * `python main.py`

# Resources

## Links

* [CraigsList Python Package](https://pypi.org/project/python-craigslist/)
* [CraigsList Documentation](https://bapi.craigslist.org/bulkpost-docs/v1/#/postings/v1-get-bulkpost2Zip2Area)

## API Docs

### Inside <channel> Element:

_**Note**: time-related attributes specified as "integer" should be expressed as POSIX timestamps._

##### Required:

* <cl:auth> Authentication information for this submission.
    * username - string - email address used to log into craigslist account / authenticate.
    * password - string - craigslist user password.
    * accountID - integer - A craigslist account number with sufficient block credit (or an invoiced account), where the username supplied is an authorized buyer for this accountID.


### Inside <item> Elements:

##### Required:

* `<title> `- string - The title of the post.
* `<description> `- string - The content (body) of the post.
* `<cl:category>` - string - The category where this will be posted. Contents should be a valid category abbreviation.
* `<cl:area>` - string - The area (city) where this will be posted. Contents should be a valid area abbreviation.
* `<cl:subarea>` - string - Subarea where this will be posted. Ad will be posted under this subarea as well as "all areas". Contents should be a valid subarea abbreviation. Note: Subarea is required only in areas that have subareas
* `<cl:replyEmail>` - string - Reply email address for this post.
    * privacy - How reply email should be displayed on the post.
        A - don't show any email address
        C - use anonymous craigslist email address
        P - publicly show the replyEmail address
    * outsideContactOK - 0, 1 If set to 0, will add text to post: it's NOT ok to contact this poster with services or other commercial interests.
    * otherContactInfo - string - Any alternate contact info text.
* `<cl:mapLocation>` - Information for creating map links
    * __city__ - string - City name, such as "New York"
    * __state__ - string - State postal abbreviation, such as "NY"
    * __postal__ - string - US, CA, or GB postal code (REQUIRED)
    * __crossStreet1__ - string - Cross street name
    * __crossStreet2__ - string - Other cross street name
    * __latitude__ - signed float - Latitude of item
    * __longitude__ - signed float - Longitude of item


_**Note**: Location information is required for all posts. Postal code is the minimum location information required and will determine an approximate geographic location of the post.
You should submit latitude and longitude attributes to set an exact geographic location for your post.
The geographic location is used to place the pin on craigslist maps and for measuring distances in range search._
