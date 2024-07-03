from urllib import parse


TOKEN= "MTI1NzY2MTg0NzE1OTQ0MzU1MQ.GFZ1Cc.QMBkTVp6AT1rGmdvU0wi1-Pl02vfT7_flBgemM"
CLIENT_SECRET = "DTGc22fZtzYDwUpd4-IzjV1TlHyBuUTw"
REDIRECT_URI = "http://127.0.0.1:5000/oauth/callback"
OAUTH_URL = f"https://discord.com/oauth2/authorize?client_id=1257661847159443551&response_type=code&redirect_uri={parse.quote(REDIRECT_URI)}&scope=identify"