Plugin Name: "Dyson compressor"
Plugin Label: "dysonCompress"
Plugin Unique ID: 1403
Maker: "Steve Harris <steve@plugin.org.uk>"
Copyright: "GPL"
Must Run Real-Time: No
Has activate() Function: Yes
Has deactivate() Function: No
Has run_adding() Function: Yes
Environment: Normal or Hard Real-Time
Ports:	"Peak limit (dB)" input, control, -30 to 0, default 0
	"Release time (s)" input, control, 0 to 1, default 0.25
	"Fast compression ratio" input, control, 0 to 1, default 0.5
	"Compression ratio" input, control, 0 to 1, default 0.5
	"Input" input, audio
	"Output" output, audio
