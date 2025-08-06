def dataprocess():
    import json
    import pandas as pd

    with open("playlist[76][36][48][6][49][41][28][85][7][90][20].json","r") as file:
        playlist=json.load(file)

        df=pd.DataFrame(playlist).T.T
        df.reset_index(inplace=True)

        sel_keys=["id","title","danceability","energy","mode","acousticness","tempo","duration_ms","num_sections","num_segments"]
        eg_table={a: playlist[a] for a in sel_keys}

        egdf=pd.DataFrame(eg_table).T.T
        egdf.reset_index(inplace=True)

        df.to_csv("playlist.csv",index=False)
        egdf.to_csv("egtable.csv",index=False)

    return df