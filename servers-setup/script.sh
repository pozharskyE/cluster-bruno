# https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/create-cluster-kubeadm/

cd ~

wget https://github.com/containerd/containerd/releases/download/v1.7.18/containerd-1.7.18-linux-amd64.tar.gz
tar Cxzvf /usr/local containerd-1.7.18-linux-amd64.tar.gz 

wget https://github.com/opencontainers/runc/releases/download/v1.2.0-rc.1/runc.amd64
install -m 755 runc.amd64 /usr/local/sbin/runc

wget https://raw.githubusercontent.com/containerd/containerd/main/containerd.service -P /usr/local/lib/systemd/system/
systemctl daemon-reload
systemctl enable --now containerd


wget https://github.com/containernetworking/plugins/releases/download/v1.5.0/cni-plugins-linux-amd64-v1.5.0.tgz
mkdir -p /opt/cni/bin
tar Cxzvf /opt/cni/bin cni-plugins-linux-amd64-v1.5.0.tgz


sudo apt-get update
sudo apt-get install -y apt-transport-https ca-certificates curl gpg


sudo mkdir -p -m 755 /etc/apt/keyrings
curl -fsSL https://pkgs.k8s.io/core:/stable:/v1.29/deb/Release.key | sudo gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg

echo 'deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v1.29/deb/ /' | sudo tee /etc/apt/sources.list.d/kubernetes.list

sudo apt-get update
sudo apt-get install -y kubelet kubeadm kubectl
sudo apt-mark hold kubelet kubeadm kubectl
sudo systemctl enable --now kubelet

# turn on ip forwarding
echo 1 > /proc/sys/net/ipv4/ip_forward

modprobe br_netfilter
sysctl -w net.bridge.bridge-nf-call-iptables=1

