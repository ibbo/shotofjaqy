from google.appengine.ext import db

class sojWave(db.Model):
    """Represents a wave that monitors the Shot of Jaq RSS feed"""
    waveID = db.StringProperty()
    waveletID = db.StringProperty()
    lastUpdated = db.StringProperty()

def addWave(waveID, waveletID, lastUpdated):
    """Adds a wave to monitor the Shot of Jaq RSS feed"""
    wave = getWave(waveID)

    if wave is None:
        wave = sojWave(waveID=waveID, waveletID=waveletID,
                lastUpdated=lastUpdated)
        wave.put()

    return wave

def getWave(waveID):
    """Gets the sojWave with the given waveID"""
    query = sojWave.gql('WHERE waveID = :1', waveID)
    results = query.fetch(1)

    if len(results) == 1:
        return results[0]
    else:
        return None
