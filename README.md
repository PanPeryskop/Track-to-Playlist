# Track to Playlist

Track to Playlist is a Python application that generates a playlist based on a single track. The application uses the Spotify API to search for similar tracks and add them to a new playlist.

## Features

- Generate a playlist based on a single track
- The playlist contains tracks similar to the seed track
- The playlist is created in the user's Spotify account

## Before you install

Before you can use Track to Playlist, you need to create a Spotify Developer application to get your `client_id`, `client_secret`, and `redirect_uri`. Here's how you can do it:

1. Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/).
2. Log in with your Spotify account.
3. Click on 'Create an App'.
4. Fill in the 'Name', 'Description' and redirect_uri (I recommend using http://localhost:3000/) for your new app, then click 'Create'.
5. On the next page, you will see your `client_id` and `client_secret`. You will need these to authenticate your application.
6. Click on 'Edit Settings'.
7. In the 'Redirect URIs' field, enter the URI where you want Spotify to redirect you after a successful login. This must be a valid URI. For local applications, you can use `http://localhost:8000/callback/`.
8. Click 'Save'.

## Installation

1. Go to the release section of this repository. [Current release.](https://github.com/PanPeryskop/Track-to-Playlist/releases/tag/v1.0)
2. Click on **Track-to-Playlist.zip**. Download will start automatically.
3. Extract the zip file.
4. Open the extracted folder and run `Track-to-Playlist.exe`.

## Usage

1. Run the `Track-to-Playlist.exe` to start the application.
2. The application will ask you to enter your `client_id`, `client_secret`, and `redirect_uri`. Enter the values from the Spotify Developer Dashboard.
3. The application will ask you to enter the URL of the track you want to base your playlist on.
4. The application will then generate a playlist based on the track and add it to your Spotify account.
5. Once the playlist is created, a message will be displayed confirming the successful creation of the playlist along with the playlist URL.

# Warning
 When first launched, the application may require a restart after entering data from the spotify dashboard

Enjoy your music!