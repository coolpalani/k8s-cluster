# KUBERNETES IN A BOX - THREE NODE DEPLOYMENT

Deploy kubernetes on the fly, the project creates a ``master node and two minions nodes``,
it uses **Vagrant** with **KVM** as infrastecture provider (IaaS) and **Ansible** as configuration manager
to automatically have a ready and functional **kubernetes cluster** in less than 10 minutes.

## 1. Pre-requisites

* Localhost machine with Linux distribution or OS Mac
* KVM
* Vagrant 1.8.1 or higher
* Ansible 2.2.1 or higher

## 2. Prepare your localhost environment

The first thing is check that you localhost support virtualization, just type 
``egrep -c '(vmx|svm)' /proc/cpuinfo`` if the result is ``0``, your locahost does not support it, 
in other case ``> 0``, means you locahost support virtualization, but also must be ensured it is enable 
in the BIOS. Once it is assured procced to install ``kvm`` (https://www.linux-kvm.org/page/Downloads).

Next to complete the environment and reproduce the ``kubernetes cluster``, 
with the use of ``Vagrant`` just install it (https://www.vagrantup.com/) on your Laptop and must be 
installed ``Ansible`` also (http://docs.ansible.com/ansible/latest/intro_installation.html).

Finally we need a ``Public RSA Key`` to inject in the ``Kubernetes Cluster`` nodes, therefore if you have already 
one fine, it is going to be used later, otherwise proceed to ``Generate SSH Keys`` in your localhost
(https://www.cyberciti.biz/faq/linux-unix-generating-ssh-keys/)

## 3. Setup you kubernetes cluster

* In the laptop just clone the repository   
   ``git clone https://github.com/jvalderrama/k8s-cluster.git``

* Go inside the folder k8s-cluster  
   ``cd k8s-cluster``

* Set your ``Publis RSA Key`` in the script ``scripts/prepare_cluster.py``

* Start up the ``Kubernetes Cluster``  
   ``vagrant up``

That's all ...

## 4. Check your Kubernetes Cluster

Now check the entire cluster with the next tips

* Go to minion-1 node and check nodes  
  ``vagrant ssh minion-1``  
  ``kubectl -s http://10.0.0.39:8080 get nodes`` it must show the two minions nodes ready and working

* Go to minion-2 node and check nodes  
  ``vagrant ssh minion-2``  
  ``kubectl config set-cluster test-cluster --server=http://10.10.10.51:8080``  
  ``kubectl config set-context test-cluster --cluster=test-cluster``  
  ``kubectl config use-context test-cluster``  
  ``kubectl get nodes`` it must show the two minions nodes ready and working

* Go to master node and check nodes  
  ``vagrant ssh master``  
  ``kubectl cluster-info``  

The above command must be show someting similar to:  
   
>Kubernetes master is running at http://localhost:8080   
>KubeDNS is running at http://localhost:8080/api/v1/proxy/namespaces/kube-system/services/kube-dns

## 5.Credits

Thanks also to my partners @@Noel_illo and @M4nu_sL :)
