import pandas as pd
pd.set_option('display.float_format', lambda x: '%.3f' % x)


df5000credits = pd.read_csv('../5000/tmdb_5000_credits.csv')
df5000movies = pd.read_csv('../5000/tmdb_5000_movies.csv')
df6820movies = pd.read_csv('../6820/movies.csv',low_memory=False)
df45000credits = pd.read_csv('../45000/credits.csv')
df45000keywords = pd.read_csv('../45000/keywords.csv')
df45000links_small = pd.read_csv('../45000/links_small.csv')
df45000links = pd.read_csv('../45000/links.csv')
df45000movies_metadata = pd.read_csv('../45000/movies_metadata.csv')
df45000ratings_small = pd.read_csv('../45000/ratings_small.csv')
df45000ratings = pd.read_csv('../45000/ratings.csv')