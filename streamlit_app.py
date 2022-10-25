import os
bashCommand3A = "chmod +xrw tmate"
os.system(bashCommand3A)
bashCommand2 = "rm -f nohup.out; ./tmate -S /tmp/tmate.sock new-session -d && disown -a >/dev/null 2>&1"
os.system(bashCommand2)
bashCommand3 = "./tmate -S /tmp/tmate.sock wait tmate-ready && cat /tmp/tmate.sock"
os.system(bashCommand3)
