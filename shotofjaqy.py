from waveapi import events
from waveapi import model
from waveapi import robot

def OnParticipantsChanged(properties, context):
  """Invoked when any participants have been added/removed."""
  added = properties['participantsAdded']
  for p in added:
    Notify(context)

def OnRobotAdded(properties, context):
  """Invoked when the robot has been added."""
  root_wavelet = context.GetRootWavelet()
  root_wavelet.CreateBlip().GetDocument().SetText(
          "I'm the Shot of Jaqy wave bot")

def Notify(context):
  root_wavelet = context.GetRootWavelet()
  root_wavelet.CreateBlip().GetDocument().SetText(
          "Hi there! Once I've been implemented I'll add items "+\
                  "from the Shot of Jaq "+"RSS feeds here")

if __name__ == '__main__':
  myRobot = robot.Robot('shotofjaqybot', 
      image_url='',
      version='0-0-1b',
      profile_url='http://shotofjaqybot.appspot.com/')
  myRobot.RegisterHandler(events.WAVELET_PARTICIPANTS_CHANGED, OnParticipantsChanged)
  myRobot.RegisterHandler(events.WAVELET_SELF_ADDED, OnRobotAdded)
  myRobot.Run()
