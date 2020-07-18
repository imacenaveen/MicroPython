# MicroPython
git clone "paste url"
git add "filename for new/modified file created in local"
git commit -m "Some message"
git push

git pull # to update local folder with git repo

To find the port of usb devices in Linux, type below commands in terminal

for sysdevpath in $(find /sys/bus/usb/devices/usb*/ -name dev); do
    (
        syspath="${sysdevpath%/dev}"
        devname="$(udevadm info -q name -p $syspath)"
        [[ "$devname" == "bus/"* ]] && continue
        eval "$(udevadm info -q property --export -p $syspath)"
        [[ -z "$ID_SERIAL" ]] && continue
        echo "/dev/$devname - $ID_SERIAL"
    )
done

# Testing git branch
# drone fix
old ip - 10.3.125.107 - password-1990
new Ip - '192.168.43.125'
# TO Launch a file in micropy terminal
exec(open('main.py').read())
os.remove('file.py')

# enter file name to download from esp
