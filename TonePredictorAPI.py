from fastapi import FastAPI
app = FastAPI()
@app.get('/tone')
def toneEstimator():
    tones = ["humerous","ironic","cynical"];
    return random.choice(tones)