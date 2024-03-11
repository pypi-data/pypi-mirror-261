#!/usr/bin/bash

# Expose track_changed librespot events in a named pipe.

# Only expose track changed events.
if [ "$PLAYER_EVENT" != 'track_changed' ]; then
  exit 0
fi
# Need a named pipe.
if [ "$QBEE_LIBRESPOT_METADATA_PIPE" == '' ]; then
  exit 0
fi
# I must already be opened for reading.
if ! [ -p "$QBEE_LIBRESPOT_METADATA_PIPE" ] ; then
  exit 0
fi
artist=$(printf '%s' "$ARTISTS" | base64)
album=$(printf '%s' "$ALBUM" | base64)
title=$(printf '%s' "$NAME" | base64)
printf 'artist:%s,album:%s,title:%s\t' "$artist" "$album" "$title" > "$QBEE_LIBRESPOT_METADATA_PIPE"
