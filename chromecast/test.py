from __future__ import print_function
import time
import pychromecast

chromecasts = pychromecast.get_chromecasts()
# cast_list = [item.device.friendly_name for item in casts]
# print (cast_list)

cast = next(item for item in chromecasts if item.device.friendly_name == "Chromecast 2 Gen")
cast.wait()
print (cast.device)
print (cast.status)
# print (cast.status.display_name)
mc = cast.media_controller
mc.block_until_active()
print (mc.status)
"""
dict(player_state=u'PLAYING',
     volume_level=1,
     images=[MediaImage(url=u'https://6.viki.io/image/3a7fb0bcd9a04932a70ebb85d1f0a9bb.jpeg?x=b&s=540x302&e=t&q=g',
                        height=0,
                        width=0)],
     media_custom_data={u'uuid': u'com.viki.android_E6553_5e4008df-d19a-4214-98e2-08f1eaff3589',
                        u'resourceId': u'1117695v',
                        u'video_id': u'1117695v',
                        u'subtitleState': True,
                        u'appVer': u'4.14.0',
                        u'appId': u'100005a',
                        u'srclang': u'en',
                        u'country': u'China'},
     duration=2648.682,
     current_time=817.82,
     playback_rate=1,
     title=u'Episode 1 - Across the Ocean to See You',
     media_session_id=1,
     volume_muted=False,
     supports_skip_forward=False,
     track=None,
     season=None,
     idle_reason=None,
     stream_type=u'BUFFERED',
     supports_stream_mute=True,
     supports_stream_volume=True,
     content_type=u'videos/mp4',
     metadata_type=0,
     subtitle_tracks=[
        {u'name': u'ar', u'language': u'ar', u'subtype': u'SUBTITLES', u'trackContentType': u'text/vtt', u'trackId': 0,
         u'trackContentId': u'https://api.viki.io/v4/videos/1117695v/subtitles/ar.vtt?app=100005a&t=1505660029&sig=4fa0be0bae8628b246f5d764642ed1f1cdeddbdd',
         u'type': u'TEXT'}],
     album_name=None,
     series_title=None,
     album_artist=None,
     media_metadata={u'metadataType': 0,
                     u'subtitle': u'Casting to Chromecast 2 Gen 1',
                     u'title': u'Episode 1 - Across the Ocean to See You',
                     u'imageUrl': u'https://6.viki.io/image/3a7fb0bcd9a04932a70ebb85d1f0a9bb.jpeg?x=b&s=540x302&e=t&q=g',
                     u'resource_id': u'1117695v',
                     u'images': [{u'url': u'https://6.viki.io/image/3a7fb0bcd9a04932a70ebb85d1f0a9bb.jpeg?x=b&s=540x302&e=t&q=g',
                                  u'width': 0,
                                  u'height': 0}],
                     u'ep': 1,
                     u'container_id': u'33665c'},
     episode=None,
     artist=None,
     supported_media_commands=15,
     supports_seek=True,
     current_subtitle_tracks=[2],
     content_id=u'https://v.viki.io/1117695v/1117695v_360p_1704021452.mp4?e=1505663628&h=aa140548605e9c4e504dd3a3a684cc9a',
     supports_skip_backward=False,
     supports_pause=True) >
"""
