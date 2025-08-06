from fastapi import FastAPI, HTTPException
import dataprocessing

df=dataprocessing.dataprocess()

app=FastAPI()
@app.get("/data")
def getdata():
    return df.to_dict(orient="records")

@app.get("/search")
def searchtitle(value):
    titles=df["title"]
    flag=None
    for t, v in titles.items():
        if v == value:
            flag = t
            break

    if flag is None:
        raise HTTPException(status_code=404, detail=f"Value {value} not found.")
    result=df.loc[flag].to_dict()
    return result