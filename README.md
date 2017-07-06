# Alsa Plugin Framework

Ever want to connect audio plugins to alsa sinks?  Well this makes doing that way easier.  

Q: What's the point of connecting audio plugins to alsa sinks?

1. A lot of movies have a high dynamic range.  You could slap a limiter or compressor on one of your sinks to reduce that dynamic range requiring less manual volume adjustment during playback.

## Example Usage

We create our alsa chain in `audio_settings.json`.  This file contains two components.  The `order` field whereby you list the plugins you want (order matters).  Then every other key corresponds to a plugin supported in the `plugins` folder.  In the following example you have `hpf` which stands for high pass filter.  
```
{
  "order": ["hpf", "Eq10"],
  "hpf": {
    "info": "High Pass Filter",
    "alsa_alias": "hpf",
    "settings": {
      "frequency_cutoff": "80"
    },
    "template_path": "/home/pi/audioConfigs/plugins/hpf/hpf.template"
  },
```

The `settings` field allows you to edit the cutoff frequency.  

After you have input the desired settings run `effected.sh` to generate the new alsa config and copy it into your home directory.  You will then need to restart alsa for the changes to take effect.

## Add support for a new LADSPA plugin

Create a new folder in `plugins` with the name of the ladspa plugin as the folder name.  Then place a file called `pluginname.template` there.  This template folder contains the alsa template for this plugin.  For example, for hpf we have:

Replace all instances of hpf with your plugin name.  Replace controls field with the controls documented for the LADSPA plugin you're adding.
```
pcm.hpf {
	type ladspa
	slave.pcm $NEXT
	path "/usr/lib/ladspa";
	plugins [{
		label hpf
		input {
			controls [ frequency_cutoff ]
		}
	}]
}
```
Now add an entry to `audio_settings.json` and you're good to go.