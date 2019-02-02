
from sqlalchemy import create_engine
from sqlalchemy import sql


from BarBeerDrinker import config 
 
engine = create_engine(config.database_uri)

def get_bars():
	
    """     
     	Connect to the database and retrieve a list of all the bars and their informatio
    """ 
    with engine.connect() as con:
    	rs = con.execute("SELECT name, license, city, phone, address,states FROM BarBeerDrinker.bar;")
    	return [dict(row) for row in rs]

def find_bar(name):
    with engine.connect() as con:
        query = sql.text(
            "SELECT name, license, city, phone, address, states FROM BarBeerDrinker.bar WHERE name = :name;"
        )

        rs = con.execute(query, name= name)
        result = rs.first()
        if result is None:
            return None
        return dict(result)

def filter_beers(max_price):
    with engine.connect() as con:
        query = sql.text(
            "SELECT * FROM BarBeerDrinker.newSells WHERE price < :max_price;"
        )

        rs = con.execute(query, max_price = max_price)
        results = [dict(row) for row in rs]
        for r in results:
            r['price']= float (r['price'])
        return results

def get_bar_menu(bar_name):
    with engine.connect() as con:
        query = sql.text(
            'SELECT a.bar, a.beer, a.price, b.manf, coalesce(c.like_count, 0) as likes  \
            FROM newSells as a \
            JOIN beer AS b \
            ON a.beer = b.name \
            LEFT OUTER JOIN (SELECT beer, count(*) as like_count FROM likes GROUP BY beer) as c \
            ON a.beer = c.beer \
            WHERE a.bar = :bar;'
        )

        rs = con.execute(query, bar = bar_name)
        results = [dict(row) for row in rs]
        for i, _ in enumerate(results):
            results[i]['price'] = float(results[i]['price'])
        return results

def get_beer_manufacturers(beer):
    with engine.connect() as con:
        if beer is None:
            rs = con.execute('SELECT DISTINCT manf FROM beer;')
            return [row['manf'] for row in rs]

        query = sql.text('SELECT manf FROM beer WHERE name = :beer;')
        rs = con.execute(query, beer=beer)
        result = rs.first()
        if result is None:
            return None
        return result['manf']
        

def get_tenderName(bar_name):
    with engine.connect() as con:
        if bar_name is None:
            rs = con.execute('select distinct bar_tender from works;')
            return [row['bar_tender'] for row in rs]
        
        query = sql.text('select bar_tender from works where name =:bar_name;')
        rs = con.execute(query, bar_name = bar_name)
        result = rs.first()
        if result is None:
            return None
        return result['bar_tender']

def get_BarName(bar_tender):
    with engine.connect() as con:
        if bar_tender is None:
            rs = con.execute('select distinct bar_name from works;')
            return [row['bar_name'] for row in rs]
        
        query = sql.text('select bar_name from works where name =:bar_tender;')
        rs = con.execute(query, bar_tender = bar_tender)
        result = rs.first()
        if result is None:
            return None
        return result['bar_name']

def get_bars_selling(beer):
    with engine.connect() as con:
        query = sql.text('SELECT a.bar, a.price, b.customers \
                FROM newSells AS a \
                JOIN (SELECT name_bar, count(*) AS customers FROM newFrequent GROUP BY name_bar) as b \
                ON a.bar = b.name_bar \
                WHERE a.beer = :beer \
                ORDER BY a.price; \
            ')
        rs = con.execute(query, beer=beer)
        results = [dict(row) for row in rs]
        for i, _ in enumerate(results):
            results[i]['price'] = float(results[i]['price'])
        return results

def get_beer_selling(beer):
    with engine.connect() as con:
        query = sql.text('select count(*) as selling, bar, beer\
                from BarBeerDrinker.transcations\
                where beer = :beer\
                group by bar\
                order by selling desc\
                limit 10; \
            ')
        rs = con.execute(query, beer=beer)
        results = [dict(row) for row in rs]
        return results

def get_rich(beer):
    with engine.connect() as con:
        query = sql.text('select total as money, beer, Last_name\
                from transcations\
                where beer = :beer\
                group by Last_name\
                order by total desc\
                limit 10; \
            ')
        rs = con.execute(query, beer=beer)
        results = [dict(row) for row in rs]
        return results

def get_top_sepender(bar):
    with engine.connect() as con:
        query = sql.text('SELECT Last_name, total  as spending \
                from transcations \
                WHERE bar = :bar \
                GROUP BY Last_name \
                ORDER BY spending desc \
                limit 10; \
         ')

        rs = con.execute(query, bar=bar)
        results = [dict(row) for row in rs]
        return results

def get_top_beer(bar):
    with engine.connect() as con:
        query = sql.text('SELECT  beer, count(total)  as times \
                from transcations \
                WHERE bar = :bar \
                GROUP BY beer  \
                ORDER BY times desc;  \
         ')

        rs = con.execute(query, bar=bar)
        results = [dict(row) for row in rs]
        return results

def get_beers():
    """Gets a list of beer names from the beers table."""

    with engine.connect() as con:
        rs = con.execute('SELECT name, manf FROM beer;')
        return [dict(row) for row in rs]

def get_bar_frequent_counts():
    with engine.connect() as con:
        query = sql.text('SELECT name_bar, count(*) as frequentCount \
                FROM newFrequent \
                GROUP BY name_bar; \
            ')
        rs = con.execute(query)
        results = [dict(row) for row in rs]
        return results

def get_bar_cities():
    with engine.connect() as con:
        rs = con.execute('SELECT DISTINCT city FROM bar;')
        return [row['city'] for row in rs]

def get_drinkers():
    with engine.connect() as con:
        rs = con.execute('SELECT Last_name, first_name, city, phone,states, address FROM drinker;')
        return [dict(row) for row in rs]

def getTenders():
    with engine.connect() as con:
        rs = con.execute('select a.bar_tender, a.bar_name, a.shift, b.beer, b.selling\
            from works as a\
            left join (\
            select count(*) as selling, tender as bar_tender, beer\
            from works, transcations \
            where works.bar_tender = transcations.tender\
            group by tender, beer) as b\
            on a.bar_tender = b.bar_tender;\
        ')
        return [dict(row) for row in rs]



def get_drinker_info(drinker_name):
    with engine.connect() as con:
        query = sql.text('SELECT * FROM drinker WHERE name = :name;')
        rs = con.execute(query, name=drinker_name)
        result = rs.first()
        if result is None:
            return None
        return dict(result)

def get_likes(drinker_name):
    """Gets a list of beers liked by the drinker provided."""

    with engine.connect() as con:
        query = sql.text('SELECT beer FROM likes WHERE drinker = :name;')
        rs = con.execute(query, name=drinker_name)
        return [row['beer'] for row in rs]