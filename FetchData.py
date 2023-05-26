from flask import Flask, request, redirect
import requests
# import json


app = Flask(__name__)

# your Spotify app credentials
client_id = '<client_id>'
client_secret = '<client_secret>'
redirect_uri = 'http://localhost:8888/callback'


@app.route('/')
def login():
    # redirect to Spotify's authorization page
    auth_url = f'https://accounts.spotify.com/' \
               f'authorize?response_type=code&client_' \
               f'id=5619e3b88bde4a808ccba8f2794ffd3f&redirect_uri=http://localhost:8888/callback'
    return redirect(auth_url)


@app.route('/callback')
def callback():
    # get authorization code
    code = request.args.get('code')

    # request access token from Spotify
    auth_response = requests.post(
        'https://accounts.spotify.com/api/token',
        data={
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': redirect_uri,
            'client_id': '5619e3b88bde4a808ccba8f2794ffd3f',
            'client_secret': '502da0dde7954a879629264089b89530'
        })

    auth_response_data = auth_response.json()
    access_token = auth_response_data['access_token']

    # access authorized Spotify data
    track_id = "77Ft1RJngppZlq59B6uP0z"
    track_analysis = get_track_analysis(track_id, access_token)

    return track_analysis


def get_track_analysis(track_id, token):
    url = f"https://api.spotify.com/v1/audio-analysis/{track_id}"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"Failed to get track analysis: {response.json()}")
        return None

    # Get the response JSON data
    data = response.json()

    # Extract bars and beats
    bars = data.get('bars', [])
    beats = data.get('beats', [])

    return {'bars': bars, 'beats': beats}

#    Write JSON data to a file
#    try:
#        print("Attempting to write file...")
#        with open('/Users/joungway/Desktop/track_analysis.json', 'w') as outfile:
#            json.dump(response.json(), outfile)
#        print("File written successfully.")
#    except Exception as e:
#        print("An error occurred:", e)


if __name__ == "__main__":
    app.run(port=8888)
