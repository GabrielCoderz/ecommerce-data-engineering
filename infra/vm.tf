resource "google_compute_instance" "pipeline-engine" {
  name         = "pipeline-engine"
  machine_type = "e2-micro"
  zone         = "us-central1-a"

  tags = ["ecommerce", "data-engineering"]

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-11"
    }
  }

  network_interface {
    network = "default"

    access_config {
      // Ephemeral IP
    }
  }

  metadata_startup_script = file("startup-script.sh")
}

resource "google_compute_disk" "default" {
  name  = "test-disk"
  type  = "pd-ssd"
  zone  = "us-central1-a"
  image = "debian-11-bullseye-v20220719"
  size = 0
  labels = {
    environment = "dev"
  }
  physical_block_size_bytes = 4096
}