import json
import urllib.parse
import urllib.request
import sys
import TBpost_tweet
import time


riot_apikey = 'RGAPI-3299e09a-995a-46c5-84bf-ed414e5ca73e'

base_match_url_john = 'https://na1.api.riotgames.com/lol/match/v3/matchlists/by-account/229679480/recent'
base_url_john = base_match_url_john + '?' + urllib.parse.urlencode([('api_key', riot_apikey)])

base_match_url_john2 = 'https://na1.api.riotgames.com/lol/match/v3/matchlists/by-account/43475381/recent'
base_url_john2 = base_match_url_john2 + '?' + urllib.parse.urlencode([('api_key', riot_apikey)])

base_match_url_chiang = 'https://na1.api.riotgames.com/lol/match/v3/matchlists/by-account/48663455/recent'
base_url_chiang = base_match_url_chiang + '?' + urllib.parse.urlencode([('api_key', riot_apikey)])

def riot_games_error():
    print('Unable to get summoner match list data')
    sys.exit()

def get_json(url: str):
    '''
    turns a given url into a python-readable dictionary using
    the json library
    '''
    try:
        response = urllib.request.urlopen(url)
        json_text = response.read().decode(encoding = 'utf-8')

        return json.loads(json_text)
    except:
        riot_games_error()
    finally:
        if response != None:
            response.close()
            
def get_match(matchlist_json):
    specific_match_url = 'https://na1.api.riotgames.com/lol/match/v3/matches/'
    first_match = matchlist_json['matches'][0]
    match_url = specific_match_url + str(first_match['gameId']) + '?' + urllib.parse.urlencode([('api_key', riot_apikey)])
    return get_json(match_url)

def get_win_lose(matchlist_json):
    first_match = matchlist_json['matches'][0]
    first_match_championid = first_match['champion']
    match_json = get_match(matchlist_json)
    for player in match_json['participants']:
        if player['championId'] == first_match_championid:
            teamId = player['teamId']
            break
    for team in match_json['teams']:
        if teamId == team['teamId']:
            return team['win']
        
def get_participantId(matchlist_json):
    first_match = matchlist_json['matches'][0]
    first_match_championid = first_match['champion']
    match_json = get_match(matchlist_json)
    for player in match_json['participants']:
        if player['championId'] == first_match_championid:
            pId = player['participantId']
            break
    return pId

def getDeaths(matchlist_json):
    match_json = get_match(matchlist_json)
    partId = get_participantId(matchlist_json)
    player = match_json['participants'][partId - 1]
    deaths = player['stats']['deaths']
    return deaths

def post_tweet(name: str, win_or_loss: str, deaths):
    if win_or_loss == "Win":
        TBpost_tweet.post('Holy shit ' + name + ' actually won a game. However, he died ' + str(deaths) + ' times.')
    else:
        TBpost_tweet.post('Lmao '+ name+ ' lost. He died ' + str(deaths) + ' times. Trash.')
        
def game_is_recent(matchlist_json):
    game = matchlist_json['matches'][0]
    timeOfGame = game['timestamp']
    
    currtime = int(time.time()) * 1000
    tenMintoMills = 600000
    
    if (currtime - timeOfGame) <= tenMintoMills:
        return True
    return False
        
def execute():
    john_matchlist_json = get_json(base_url_john)
    if game_is_recent(john_matchlist_json):
        john_winOrLose = get_win_lose(john_matchlist_json)
        john_deaths = getDeaths(john_matchlist_json)
        post_tweet('John', john_winOrLose, john_deaths)
     
    john2_matchlist_json = get_json(base_url_john2)
    if game_is_recent(john2_matchlist_json):
        john2_winOrLose = get_win_lose(john2_matchlist_json)
        john2_deaths = getDeaths(john2_matchlist_json)
        post_tweet('John', john2_winOrLose, john2_deaths)
    
    chiang_matchlist_json = get_json(base_url_chiang)
    if game_is_recent(chiang_matchlist_json):
        chiang_winOrLose = get_win_lose(chiang_matchlist_json)
        chiang_deaths = getDeaths(chiang_matchlist_json)
        post_tweet('Chiang', chiang_winOrLose, chiang_deaths)
    

    
            

