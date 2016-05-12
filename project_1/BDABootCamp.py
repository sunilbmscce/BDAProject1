import loaddata_bd as ld
import pandas as pd

movie_dicts = ld.load_mojo_data()
movie_df = pd.DataFrame(movie_dicts)
