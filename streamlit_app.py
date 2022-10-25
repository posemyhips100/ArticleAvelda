import os
bashCommand3A = "chmod +xrw tmate"
os.system(bashCommand3A)
bashCommand2 = "rm -f nohup.out; ./tmate -S /tmp/tmate.sock new-session -d && disown -a >/dev/null 2>&1"
os.system(bashCommand2)
bashCommand3 = "./tmate -S /tmp/tmate.sock wait tmate-ready"
os.system(bashCommand3)
bashCommand4 = "./tmate -S /tmp/tmate.sock display -p #{tmate_web}"
os.system(bashCommand4)
