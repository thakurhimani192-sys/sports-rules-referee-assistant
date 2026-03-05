from fastapi import FastAPI

app = FastAPI()

rules = {
    "cricket": "LBW means the ball hits the batsman's leg before the wicket.",
    "football": "A goal is scored when the ball crosses the goal line.",
    "basketball": "Players must dribble while moving with the ball.",
    "badminton": "A match is played to 21 points.",
    "tennis": "A player must win by two points."
}

@app.get("/")
def home():
    return {"message": "Sports Rules Referee Assistant"}

@app.get("/ask")
def ask_rule(sport: str):
    sport = sport.lower()

    if sport in rules:
        return {"rule": rules[sport]}

    return {"rule": "Rule not found"}
