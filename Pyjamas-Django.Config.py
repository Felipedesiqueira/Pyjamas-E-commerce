#1. (And possibly the largest pain in the ass...) Learn how to find out how to programmatically see
#if each service is already installed, etc.  This is really stupid since a handler for each service
#will likely have to be created.  Look into standardized folders, maybe Unix keeps all their shit in
#one place.  Maybe it would be better to just install it in the appropriate place.
#Should run this script as sudo.  Make warning to run as sudo if exceptions get fired.
#	A) Is libcommondjango installed and wtf is it called?
#	B) Is Django installed?
#	C) Is Apache2 installed?
#		a) Does Apache2 have a Django ready configuration? (Sidenote, personal configuration datab
#		ase could help here

#2. Create download/install mechanism for each mechanism (RPM/APT) and then specify to specific ser
#vices.  I suppose if we think about it this way with the services being "pluggable" others will
#extend.


#3. Ability to uninstall installed services would also be really nice.

#4. Create auto-config for each framework, start with django.

