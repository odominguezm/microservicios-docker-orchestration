Vagrant.configure("2") do |config|
  # Usaremos Ubuntu 24.04 (Noble Numbat)
  config.vm.box = "ubuntu/jammy64"

  # Configuración de Red: Bridge (Puente) 
  # Esto le dará una IP de tu router de Cali (ej: 192.168.1.x)
  config.vm.network "public_network"

  # Recursos de la VM
  config.vm.provider "virtualbox" do |vb|
    vb.memory = "2048"
    vb.cpus = 2
    vb.name = "servidor-microservicios"
  end

  # Script de Aprovisionamiento: Instala Docker automáticamente
  config.vm.provision "shell", inline: <<-SHELL
    apt-get update
    apt-get install -y docker.io docker-compose
    usermod -aG docker vagrant
  SHELL
end
