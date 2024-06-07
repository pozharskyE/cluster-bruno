the project is in development. Description and other directories will be added later 

# servers setup 
- login to the sever via ssh as root user
- (optional) change hostname (in /etc/hostname) and reboot
- `apt install git`
- `git clone https://github.com/pozharskyE/cluster-bruno.git`
- `cd cluster-bruno/servers-setup/cloned-and-modified`
- CHANGE "OS" variable to fit your system in common.sh (via `nano common.sh`)
- `source common.sh`
- carefully watch the execution process. If some error occures - debug it.
- If you encountered error like "W: GPG error: ... all Release: The following signatures couldn't be verified because the public key is not available: NO_PUBKEY 3C962022012520A0" ===>
https://askubuntu.com/questions/20725/gpg-error-the-following-signatures-couldnt-be-verified-because-the-public-key
- ONLY FOR MASTER NODE: `source master.sh`
