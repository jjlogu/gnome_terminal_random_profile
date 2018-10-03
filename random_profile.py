import subprocess as sp
import random as r

# Fetch all existing profiles
profiles=eval(sp.check_output(["gsettings","get","org.gnome.Terminal.ProfilesList","list"]).decode("utf8").strip())

# get a random profile
random_profile = r.choice(profiles)

# set the random profile as default
sp.check_output(["gsettings","set","org.gnome.Terminal.ProfilesList","default", random_profile])
